from NN import *


def save_nn(nn):
    # Get all matrices as arrays
    w_ih = Matrix.toArray(nn.weights_ih)
    w_ho = Matrix.toArray(nn.weights_ho)
    b_h = Matrix.toArray(nn.bias_h)
    b_o = Matrix.toArray(nn.bias_o)

    # Get all arrays as strings
    w_ih = ",".join([str(x) for x in w_ih])
    w_ho = ",".join([str(x) for x in w_ho])
    b_h = ",".join([str(x) for x in b_h])
    b_o = ",".join([str(x) for x in b_o])
    data = "\n".join([w_ih,w_ho,b_h,b_o])

    # Save data to file
    file = open("Data.txt", "w")
    file.write(data)
    file.close()


def read_nn(input_nodes, hidden_nodes, output_nodes):
    # Get saved data
    file = open("Data.txt", "r")
    data = file.read()
    file.close()

    # Separate data
    data = data.split('\n')
    w_ih = [float(x) for x in data[0].split(",")]
    w_ho = [float(x) for x in data[1].split(",")]
    b_h = [float(x) for x in data[2].split(",")]
    b_o = [float(x) for x in data[3].split(",")]

    try:
        # Get all arrays as matrices
        w_ih = Matrix.fromCondensedArray(w_ih, hidden_nodes, input_nodes)
        w_ho = Matrix.fromCondensedArray(w_ho, output_nodes, hidden_nodes)
        b_h = Matrix.fromCondensedArray(b_h, hidden_nodes, 1)
        b_o = Matrix.fromCondensedArray(b_o, output_nodes, 1)
    except:
        return NeuralNetwork(input_nodes, hidden_nodes, output_nodes)

    # Create neural network with these variables
    nn = NeuralNetwork(input_nodes, hidden_nodes, output_nodes)
    nn.weights_ih = w_ih
    nn.weights_ho = w_ho
    nn.bias_h = b_h
    nn.bias_o = b_o
    return nn
