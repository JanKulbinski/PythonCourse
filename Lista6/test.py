# UWAGA! W TYM PLIKU ZANJDUJE SIĘ TAKŻE ZADANIE TRZECIE!

import matplotlib.pyplot as plt
import numpy as np


class NetworkLayer:
    def __init__(self, activation_fn, shape):
        self.fn, self.fn_prim = activation_fn
        self.weights = np.random.standard_normal(shape)
        self.values = np.zeros((shape[1]))


class NeuralNetwork:
    def __init__(self, layers, eta, output_shape=(1, 1)):
        self.output_layer = np.zeros(output_shape)
        self.layers = []
        self.eta = eta

        for layer, next_layer in zip(layers[0:-1], layers[1:]):
            self.layers.append(
                NetworkLayer(layer['fn'], (next_layer['size'], layer['size']))
            )

        self.layers.append(
            NetworkLayer(layers[-1]['fn'],
                         (output_shape[0], layers[-1]['size']))
        )

    def feedforward(self, x):
        self.layers[0].values = x

        for layer, next_layer in zip(self.layers[0:-1], self.layers[1:]):
            next_layer.values = layer.fn(np.dot(layer.values, layer.weights.T))

        self.output_layer = self.layers[-1].fn(
            np.dot(self.layers[-1].values, self.layers[-1].weights.T)
        )

    def backprop(self, y):
        deltas = []

        delta = (y - self.output_layer) * \
            self.layers[-1].fn_prim(self.output_layer)
        deltas.append(self.eta * np.dot(delta.T, self.layers[-1].values))

        for layer, previous_layer in zip(reversed(self.layers[0:-1]), reversed(self.layers[1:])):
            delta = layer.fn_prim(previous_layer.values) * \
                np.dot(delta, previous_layer.weights)
            deltas.append(
                self.eta * np.dot(delta.T, layer.values)
            )

        for layer, weight in zip(self.layers, reversed(deltas)):
            layer.weights += weight

    def train(self, input, expected_output, iterations):
        for _ in range(iterations):
            self.feedforward(input)
            self.backprop(expected_output)

sig = (
    lambda x: 1./(1 + np.exp(-x)),
    lambda x: x * (1. - x)
)

relu = (
    lambda x: np.maximum(0, x),
    lambda x: 1. * (x > 0)
)

tanh = (
    lambda x: np.tanh(x),
    lambda x: 1-x**2
)


def mse(expected, actual):
    sum = 0
    for index, result in enumerate(expected):
        sum += (result - actual[index])**2
    return sum/len(expected)


def visualize(test):
    network = NeuralNetwork(test['layers'], test['eta'])
    domain = test['x']/max(test['x'])
    image = test['fn'](domain)

    X = np.reshape(domain, (len(domain), 1))
    y = np.reshape(image, (len(image), 1))

    big = test['big']/max(test['big'])
    big_image = test['fn'](big)
    test_X = np.reshape(big, (len(big), 1))

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.set_title(test['name'])
    ax1.scatter(domain, y)

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.set_title('Aproksymowane')

    for i in range(50):
        network.train(X, y, 100)
        network.feedforward(test_X)
        ax2.clear()
        ax2.set_xlabel(
            f"{i*100} iteracji\nMSE: {mse(big_image, network.output_layer.flatten())}")
        ax2.scatter(big, network.output_layer.flatten())
        plt.pause(0.016)
    plt.show()


tests = [
    {
        'name': 'Parabola, dwie warstwy',
        'layers': [
            {'fn': sig, 'size': 1},
            {'fn': tanh, 'size': 10},
        ],
        'x': np.linspace(-50, 50, 26),
        'big': np.linspace(-50, 50, 101),
        'fn': lambda x: x**2,
        'eta': 0.2
    },
    {
        'name': 'Sinus, dwie warstwy',
        'layers': [
            {'fn': tanh, 'size': 1},
            {'fn': tanh, 'size': 10}
        ],
        'x': np.linspace(0, 2, 21),
        'big': np.linspace(0, 2, 161),
        'fn': lambda x: np.sin((3*np.pi/2) * x),
        'eta': 0.01
    },
    {
        'name': 'Parabola, trzy warstwy',
        'layers': [
            {'fn': sig, 'size': 1},
            {'fn': sig, 'size': 10},
            {'fn': sig, 'size': 10},
        ],
        'x': np.linspace(-50, 50, 26),
        'big': np.linspace(-50, 50, 101),
        'fn': lambda x: x**2,
        'eta': 0.1
    },
    {
        'name': 'Sinus, trzy warstwy',
        'layers': [
            {'fn': tanh, 'size': 1},
            {'fn': tanh, 'size': 10},
            {'fn': tanh, 'size': 10}
        ],
        'x': np.linspace(0, 2, 21),
        'big': np.linspace(0, 2, 161),
        'fn': lambda x: np.sin((3*np.pi/2) * x),
        'eta': 0.01
    }
]

for test in tests:
    visualize(test)