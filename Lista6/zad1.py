import numpy as np

'''
1) odpowiedz do pytania z treści:
    jedynki na koncu danych dodajemy, aby otrzymać nie tylko gradient,
    ale też przesunięcie (bias)

'''
def ReLU(x):
    return x * (x > 0)

def ReLU_derivative(x):
    # przyjmuje wygodne założenie, że pochodna w 0 istnieje i równa jest 0 
    return 1. * (x > 0)


def sigmoid(x):
    return (1.0 / (1.0 + np.exp(-x)))

def sigmoid_deravtive(x):
    return x * (1.0 - x)


class NeuralNetwork:
    def __init__(self, x, y, eta):
        self.input = x
        self.weights1 = np.random.rand(4, self.input.shape[1])
        self.weights2 = np.random.rand(1, 4)
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

class ResultSample:
    def __init__(self, name, table):
        self.name = name
        self.table = table

def learn(x, y, func, func2, func_deravative, func_deravative2, eta):
    nn = NeuralNetwork(x,y, eta)
    for i in range(5000):
        nn.feedforward(func,func2)
        nn.backprop(func_deravative,func_deravative2)
    return nn.output

if __name__ == "__main__":
    x = np.array([
        [0,0,1],
        [0,1,1],
        [1,0,1],
        [1,1,1]])
    y = []
    y.append(ResultSample('XOR', np.array([[0],[1],[1],[0]])))
    y.append(ResultSample('AND', np.array([[0],[0],[0],[1]])))
    y.append(ResultSample('OR', np.array([[0],[1],[1],[1]])))

    np.set_printoptions(precision=3, suppress=True)
    for index, value in enumerate(y):
        np.random.seed(0)
        r1 = learn(x, value.table, sigmoid, sigmoid, sigmoid_deravtive, sigmoid_deravtive, 0.5)
        print(f'{value.name}: sigmoid sigmoid\n{r1}\n')
    
        np.random.seed(17)
        if(index == 2): 
            np.random.seed(8)
        r2 = learn(x, value.table, ReLU, ReLU, ReLU_derivative, ReLU_derivative, 0.01)
        print(f'{value.name}: ReLU ReLU\n{r2}\n')

        np.random.seed(9)
        r3 = learn(x, value.table, ReLU, sigmoid, ReLU_derivative, sigmoid_deravtive, 0.01)
        print(f'{value.name}: ReLU sigmoid\n{r3}\n')
    
        np.random.seed(18)
        r4 = learn(x, value.table, sigmoid, ReLU, sigmoid_deravtive, ReLU_derivative, 0.01)
        print(f'{value.name}: sigmoid ReLU\n{r4}\n')

    print('Dla kazdej funkcji, po optymalnym dobraniu seed\'u\
 i wspolczynnika uczenia, najlepsze jest uzycie dla obu warstw funkcji ReLU')