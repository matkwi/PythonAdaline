import random
from matplotlib import pyplot as plt
import numpy as np


class Adaline(object):

    def __init__(self, no_of_inputs, learning_rate=0.01, iterations=1000):
        self.no_of_inputs = no_of_inputs
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = [random.uniform(-0.01, 0.01) for _ in
                        range(2 * self.no_of_inputs + 2)]
        self.errors = []

    def train(self, X, Y, name, color, close_file, label):
        # X = self._standarize(X)
        X = self._normalize(X)
        for _ in range(self.iterations):
            randPick = list(range(0, len(X)))  # Pomocnicza tablica do losowości
            random.shuffle(randPick)
            e = 0
            for i in randPick:  # Zadanie: losowy wybor przykladow uczacych.
                out = self.output(X[i])
                self.weights += self.learning_rate * (Y[i] - out) * np.concatenate([X[i], self.fourier_transform(X[i])]) * self._activation_derivative(out)
                self.weights[0] += self.learning_rate * (Y[i] - out) * self._activation_derivative(out)
                e += (Y[i] - out) ** 2
            self.errors.append(e)
        plt.plot(range(len(self.errors)), self.errors, color=color, linewidth=1.5, label=label)
        plt.legend(loc="upper right")
        plt.savefig('learning_curve_' + name + '.pdf')
        if close_file:
            plt.close()

    def _standarize(self, training_data_x):
        # Zadanie: X' = (X - Mean(X))/Std(X)
        for i in range(len(training_data_x)):
            training_data_x[i] = (training_data_x[i] - np.mean(training_data_x[i])) / np.std(training_data_x[i])
        return training_data_x

    def _normalize(self, training_data_x):
        # Zadanie: X' = (X - min(X))/(max(X) - min(X))
        for i in range(len(training_data_x)):
            training_data_x[i] = (training_data_x[i] - np.min(training_data_x[i])) / (np.max(training_data_x[i]) - np.min(training_data_x[i]))
        return training_data_x

    def _activation(self, x):
        x = 1 / (1 + np.exp(-x))
        return x

    def _activation_derivative(self, x):
        x = self._activation(x) * (1 - self._activation(x))
        return x

    def fourier_transform(self, x):
        a = np.abs(np.fft.fft(x))
        a[0] = 0
        return a / np.amax(a)

    def output(self, input):
        inp = np.concatenate([input, self.fourier_transform(input)])
        summation = np.dot(self.weights, inp)
        return summation
