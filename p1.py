import numpy as np

inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]
weights = [weights1, weights2, weights3]
# we have 3 neurons in the layer, each with its own set of weights

bias1 = 2
bias2 = 3
bias3 = 0.5
biases = [bias1, bias2, bias3]

# This code calculates the output of a simple neural network layer
# every input has its own unique weight but they all share the same bias

# layer_outputs = []
# for neuron_weights, bias in zip(weights, biases): # zip combines weights and biases
#     neuron_output = 0
#     for input_value, weight in zip(inputs, neuron_weights): # zip combines inputs and weights
#         neuron_output += input_value * weight
#     neuron_output += bias
#     layer_outputs.append(neuron_output)
# Example: adding another layer

# Layer 2
weights2 = [
    [0.1, -0.14, 0.5],
    [-0.5, 0.12, -0.33],
    [-0.44, 0.73, -0.13]
]
biases2 = [-1, 2, -0.5]

layer2_output = np.dot(weights2, output) + biases2
print(layer2_output)

output = np.dot(weights, inputs) + biases

print(output)

