import copy
from abc import ABC

import numpy as np

from torchy.value import Value


class Layer(ABC):

    def backward(self, d_out):
        pass

    def forward(self, X):
        pass

    def __call__(self, X):
        return self.forward(X)


class NnLayer(Layer):
    def zero_grad(self):
        pass

    def params(self) -> dict[str, Value]:
        pass


class Linear(NnLayer):
    def __init__(self, n_input, n_output):
        self.W = Value(0.001 * np.random.randn(n_input, n_output))  # TODO
        self.B = Value(0.001 * np.random.randn(1, n_output))  # TODO
        self.X = None

    def forward(self, X):
        self.X = copy.deepcopy(X)

        return np.dot(self.X, self.W.data) + self.B.data

    def backward(self, d_out):
        self.W.grad = np.dot(self.X.T, d_out)

        E = np.ones(shape=(1, self.X.shape[0]))
        self.B.grad = E.dot(d_out)

        d_pred = np.dot(d_out, self.W.data.T)

        return d_pred

    def zero_grad(self):
        for _, value in self.params().items():
            value.grad = 0.0

    def params(self) -> dict[str, Value]:
        d = {
            "W": self.W,
            "B": self.B
        }

        return d


class Conv2d(NnLayer):
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int, stride: int = 1, padding: int = 0):
        self.W = Value(np.random.randn(out_channels, in_channels, kernel_size, kernel_size))  # TODO
        self.B = Value(np.zeros(out_channels))  # TODO
        self.X = None

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding

        self._padding_width = ((0, 0), (0, 0), (padding, padding), (padding, padding))

    def forward(self, X):
        self.X = np.pad(X, pad_width=self._padding_width, mode="constant", constant_values=0)
        batch_size, in_channels, height, width = X.shape

        out_height = (height + 2 * self.padding - self.kernel_size) // self.stride + 1
        out_width = (width + 2 * self.padding - self.kernel_size) // self.stride + 1

        W_flatten = np.reshape(self.W.data, (-1, self.out_channels))

        out = np.zeros(shape=(batch_size, self.out_channels, out_height, out_width))
        for y in range(0, out_height, self.stride):
            for x in range(0, out_width, self.stride):
                input_region = self.X[:, :, y:y + self.kernel_size, x:x + self.kernel_size]
                input_region_flatten = np.reshape(input_region, (batch_size, -1))
                output_feature_map = np.dot(input_region_flatten, W_flatten) + self.B.data
                out[:, :, y, x] = output_feature_map

        return out

    def backward(self, d_out):
        batch_size, out_channels, out_height, out_width = d_out.shape

        W_flatten = self.W.data.reshape(-1, self.out_channels)
        W_flatten_grad = self.W.grad.reshape(-1, self.out_channels)

        d_pred = np.zeros_like(self.X)
        for y in range(0, out_height, self.stride):
            for x in range(0, out_width, self.stride):
                output_region = self.X[:, :, y:y + self.kernel_size, x:x + self.kernel_size]
                output_region_flatten = np.reshape(output_region, (batch_size, -1))
                pixel = d_out[:, :, y, x]
                d_output_region_flatten = np.dot(pixel, W_flatten.T)
                d_output_region = np.reshape(d_output_region_flatten, output_region.shape)
                d_pred[:, :, y:y + self.kernel_size, x:x + self.kernel_size] += d_output_region

                W_flatten_grad += np.dot(output_region_flatten.T, pixel)

        self.B.grad = np.sum(d_out, axis=(0, 2, 3))

        return d_pred[:, :, 1:-1, 1:-1]

    def params(self) -> dict[str, Value]:
        d = {
            "W": self.W,
            "B": self.B
        }

        return d


class ReLU(Layer):
    def __init__(self):
        self._mask = None

    def forward(self, X):
        self._mask = X > 0
        return np.where(self._mask, X, 0)

    def backward(self, d_out):
        return d_out * self._mask


class BatchNorm1d(NnLayer):
    def __init__(self, n_output, eps=1e-5):
        self.out = None  # TODO
        self.X_norm = None  # TODO
        self.X_var = None  # TODO
        self.X_mean = None  # TODO
        self.X = None  # TODO
        self.eps = eps
        self.gamma = Value(np.ones(n_output))
        self.beta = Value(np.zeros(n_output))

    def forward(self, X):
        self.X = copy.deepcopy(X)

        self.X_mean = np.mean(X, axis=0, keepdims=True)
        self.X_var = np.var(X, axis=0, keepdims=True)
        self.X_norm = (X - self.X_mean) / np.sqrt(self.X_var + self.eps)

        self.out = self.gamma.data * self.X_norm + self.beta.data
        return self.out

    def backward(self, d_out):
        self.gamma.grad = (self.X_norm * d_out).sum(axis=0)
        self.beta.grad = d_out.sum(0)

        batch_size = self.X.shape[0]

        sqrt_var_eps = np.sqrt(self.X_var + self.eps)
        dxhat = d_out * self.gamma.data
        dvar = np.sum(dxhat * (self.X - self.X_mean), axis=0) * (-1 / 2) * (self.X_var + self.eps) ** (-3 / 2)
        dmu = np.sum(dxhat * (-1 / sqrt_var_eps), axis=0) + dvar * (-2 / batch_size) * np.sum(self.X - self.X_mean,
                                                                                              axis=0)
        dx = dxhat * (1 / sqrt_var_eps) + dvar * (2 / batch_size) * (self.X - self.X_mean) + dmu / batch_size
        return dx

    def params(self) -> dict[str, Value]:
        d = {
            "gamma": self.gamma,
            "beta": self.beta
        }

        return d


class MaxPool2d(Layer):
    def __init__(self, kernel_size, stride=None, padding=0):
        self.X = None

        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self._padding_width = ((0, 0), (0, 0), (padding, padding), (padding, padding))

    def forward(self, X):
        self.X = np.pad(X, pad_width=self._padding_width, mode="constant", constant_values=0)
        batch_size, in_channels, height, width = self.X.shape

        out_height = (height + 2 * self.padding - self.kernel_size) // self.stride + 1
        out_width = (width + 2 * self.padding - self.kernel_size) // self.stride + 1

        out = np.zeros(shape=(batch_size, in_channels, out_height, out_width))
        for y in range(0, out_height, self.stride):
            for x in range(0, out_width, self.stride):
                input_region = self.X[:, :, y:self.kernel_size + y, x:self.kernel_size + x]
                out[:, :, y, x] += np.max(input_region, axis=(2, 3))

        return out

    def backward(self, d_out):
        _, out_channels, out_height, out_width = d_out.shape

        d_pred = np.zeros_like(self.X)
        for y in range(0, out_height, self.stride):
            for x in range(0, out_width, self.stride):
                output_region = self.X[:, :, y:y + self.kernel_size, x:x + self.kernel_size]
                grad = d_out[:, :, y, x][:, :, np.newaxis, np.newaxis]
                mask = (output_region == np.max(output_region, (2, 3))[:, :, np.newaxis, np.newaxis])
                d_pred[:, :, y:y + self.kernel_size, x:x + self.kernel_size] += grad * mask

        return d_pred
