# A simple two-layer feed forward network with manual backpropagation and gradient check in Pytorch

import torch
import numpy as np

# Input sample
x = np.random.randn(1, 5) # One sample with five features
# Output label
y = np.array(1.0) 

# Weight matrices and biases of first and second layer
W1 = np.random.randn(5, 3) * 0.01 # Three neurons in hidden layer
W2 = np.random.randn(3, 1) * 0.01
b1 = np.zeros((1, 3))
b2 = np.zeros((1, 1))

# Forward pass in numpy
z1 = np.dot(x, W1) + b1 # Hidden layer pre-activation
a1 = z1 * (z1 > 0) # Hidden layer ReLU activation
z2 = np.dot(a1, W2) + b2 # Output layer pre-activation
a2 = np.exp(z2) / (1 + np.exp(z2)) # Output layer sigmoid activation
loss = -(y * np.log(a2) + (1-y)*np.log(1-a2)) # Binary cross entropy loss

# Manual backward pass
# It's probably best to try to derive these by hand on paper, I find it difficult to follow from the code, and different ways of writing exist.
da2 = (1-y)/(1-a2) - y/a2 # dL/da2
dz2 = da2 * np.exp(z2) / (1 + np.exp(z2))**2 # dL/dz2, derivative of sigmoid is sigmoid * (1 - sigmoid)
db2 = dz2 # Increasing bias of the 1-dimensional output layer increases the output preactivation by the same amount
dW2 = dz2 * a1.T # Changing the weights of the hidden layer changes the pre-activation proportional to the inputs of the hidden layer (the a1). dz2 is broadcast.
da1 = dz2 * W2.T # Similar as for dW2, just that a1 'moves' and W2 is seen as fixed
dz1 = np.dot(da1, np.diag(z1.squeeze() > 0)) # ReLU has derivative of 1 if the input is > 0; np.diag takes the diagonal of a matrix, but we want to construct a matrix with a given diagonal, so we need a 1-dim vector as input
db1 = dz1 # Similar as above, just here we have a vector of shape (1, hidden_dim)
dW1 = np.dot(x.T, dz1) # Shapes (5, 1) x (1, 3) gives (5, 3)


# Gradient checking with Pytorch

# Tensor initializations with the same numpy random arrays
W1 = torch.tensor(W1, requires_grad=True)
W2 = torch.tensor(W2, requires_grad=True)
b1 = torch.tensor(b1, requires_grad=True)
b2 = torch.tensor(b2, requires_grad=True)
x = torch.tensor(x)
y = torch.tensor(y)

# # Note to self:
# # Alternative initialization with .retain_grad():
# W1 = torch.randn(5, 3, requires_grad=True) * 0.01
# W1.retain_grad() # Need this to access the gradient later: because we multiplied by 0.01, W1 is no longer considered to be a leaf node
# # Alternative initialization with torch.nn.init:
# W1 = torch.nn.init.normal_(torch.empty(5, 3, requires_grad=True), std=0.01)

# Forward pass in Pytorch
z1 = torch.matmul(x, W1) + b1 # Hidden layer pre-activation
a1 = z1 * (z1 > 0) # ReLU activation. Also: z1.relu() (will have different gradient function)
z2 = torch.matmul(a1, W2) + b2
a2 = z2.sigmoid() # Like torch.exp(z2) / (1 + torch.exp(z2)), but with a different backward gradient function
loss = -(y * a2.log() + (1-y)*(1-a2).log())

# We need to explicitly tell Pytorch that we want to inspect the gradients of intermediate steps as well
z1.retain_grad()
a1.retain_grad()
z2.retain_grad()
a2.retain_grad()

# Automatic backward pass
loss.backward(retain_graph=True)

# Tests
for own, automatic in zip([da2, dz2, db2, dW2, da1, dz1, db1, dW1],
                          [a2, z2, b2, W2, a1, z1, b1, W1]):
    np.allclose(own, automatic.grad)