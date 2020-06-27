import numpy as np
import math
from matplotlib import pyplot as plt

'''
Niestety nie znalazlem parametrow (seed, eta), dla ktorych siec dobrze odwzorowalaby podane funkcje
'''
def ReLU(x):
    return x * (x > 0)

def ReLU_derivative(x):
    # przyjmuje wygodne założenie, że pochodna w 0 istnieje i równa jest 0 
    return 1. * (x > 0)

def sigmoid(x):
    return (1.0 / (1.0 + np.exp(-x)))

def sigmoid_derivative(x):
    return x * (1.0 - x)

def tgh(x):
    return math.tan(x)

def tgh_derivative(x):
    return (1 - (x**2))

class NeuralNetwork:
    def __init__(self, x, y, eta, size):
        self.input = x
        self.weights1 = np.random.rand(size, self.input.shape[1])
        self.weights2 = np.random.rand(1, size)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = eta

    def feedforward(self, func1, func2):
        self.layer1 = func1(np.dot(self.input, self.weights1.T))
        self.output = func2(np.dot(self.layer1, self.weights2.T))

    def backprop(self, func1, func2):
        delta2 = (self.y - self.output) * func2(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = func1(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2


def learn(ax, x, y, func, func2, func_deravative, func_deravative2, eta, size, min, max):
    x_axis = x
    x = np.c_[x]
    y = np.c_[y]
    np.set_printoptions(precision=3, suppress=True)

    nn = NeuralNetwork(x,y, eta, size)
    for i in range(10000):
        nn.feedforward(func,func2)
        nn.backprop(func_deravative,func_deravative2)
        if i % 100 == 0:
            ax.clear()
            ax.set_ylim([min,max])
            ax.scatter(x_axis, nn.output, color="blue")
            plt.pause(0.05)
            print(f'Krok:{i} Blad sredniokwadratowy:{np.sum((nn.output - nn.y) ** 2) / (len(x_axis))}')

if __name__ == "__main__":
    # function 1
    fig, axes = plt.subplots(2)
    x = np.linspace(-50,50,26)
    y = x ** 2
    axes[0].scatter(x, y)

    x = np.linspace(-50,50,101)
    y = x ** 2
    tgh = np.vectorize(tgh) 
    learn(axes[1], x, y, tgh, tgh, tgh_derivative, tgh_derivative, 0.5, 10, 0, 25000)

    #function 2
    fig, axes = plt.subplots(2)
    x = np.linspace(0,2,21)
    y = np.sin((3*np.pi/2) * x)
    axes[0].scatter(x, y)

    x = np.linspace(0,2,161)
    y = x ** 2
    learn(axes[1], x, y, tgh, tgh, tgh_derivative, tgh_derivative, 0.5, 10, -1, 1)

    