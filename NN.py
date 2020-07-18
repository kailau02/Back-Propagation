from Matrix import *
import math


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def dsigmoid(y):
    return y * (1.0 - y)


class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = Matrix(self.hidden_nodes, 1)
        self.bias_o = Matrix(self.output_nodes, 1)
        self.bias_h.randomize()
        self.bias_o.randomize()

        self.learning_rate = 0.1

    def feedforward(self, input_array):
        # Generate the hidden outputs
        inputs = Matrix.fromArray(input_array)
        hidden = Matrix.multiplyMatrices(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        # Activation function
        hidden.map(sigmoid)

        outputs = Matrix.multiplyMatrices(self.weights_ho, hidden)
        outputs.add(self.bias_o)
        outputs.map(sigmoid)

        return Matrix.toArray(outputs)

    def train(self, input_array, target_array):

        # Generate the hidden outputs
        inputs = Matrix.fromArray(input_array)
        hidden = Matrix.multiplyMatrices(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        # Activation function
        hidden.map(sigmoid)

        # Generate the output's output
        outputs = Matrix.multiplyMatrices(self.weights_ho, hidden)
        outputs.add(self.bias_o)
        outputs.map(sigmoid)

        # Convert array to matrix object
        targets = Matrix.fromArray(target_array)

        # Calculate error
        output_errors = Matrix.subtract(targets, outputs)

        # Calculate gradient
        gradients = Matrix.mapMatrix(outputs, dsigmoid)
        gradients.multiply(output_errors)
        gradients.multiply(self.learning_rate)

        # Calculate deltas
        hidden_T = Matrix.transpose(hidden)
        who_deltas = Matrix.multiplyMatrices(gradients, hidden_T)

        # Adjust weights and biases by their deltas
        self.weights_ho.add(who_deltas)
        self.bias_o.add(gradients)

        # Calculate the hidden layer errors
        who_t = Matrix.transpose(self.weights_ho)
        hidden_errors = Matrix.multiplyMatrices(who_t, output_errors)

        # Calculate hidden gradient
        hidden_gradient = Matrix.mapMatrix(hidden, dsigmoid)
        hidden_gradient.multiply(hidden_errors)
        hidden_gradient.multiply(self.learning_rate)

        # Calculate ih deltas
        inputs_T = Matrix.transpose(inputs)
        weight_ih_deltas = Matrix.multiplyMatrices(hidden_gradient, inputs_T)

        # Adjust weights and biases by their deltas
        self.weights_ih.add(weight_ih_deltas)
        self.bias_h.add(hidden_gradient)
