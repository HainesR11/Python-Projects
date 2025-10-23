import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("./train.csv")

data = np.array(data)
m, n = data.shape
np.random.shuffle(data)  # shuffle before splitting into dev and training sets

data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]
X_dev = X_dev / 255.0

data_train = data[1000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]
X_train = X_train / 255.0
_, m_train = X_train.shape


def init_params():
    W1 = np.random.rand(10, 784) - 0.5
    b1 = np.zeros((10, 1)) - 0.5
    W2 = np.random.rand(10, 10) - 0.5
    b2 = np.zeros((10, 1)) - 0.5

    return W1, b1, W2, b2


# Relu (Rectified Linear Unit) is a common activation function used in neural networks.
# It outputs the input directly if it is > 1; otherwise, it outputs zero.
def Relu(Z):
    return np.maximum(0, Z)


# Caclulates a soft probability percentage
def softmax(Z):
    A = np.exp(Z) / np.sum(np.exp(Z), axis=0)
    return A


# Z1 = Hidden layer linear transform
# A1 = Hidden layer activation
# Z2 = Output layer linear transform
# A2 = Output layer activation
def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = Relu(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)

    return Z1, A1, Z2, A2


def one_hot(Y):
    one_hot_y = np.zeros((Y.size, Y.max() + 1))
    one_hot_y[np.arange(Y.size), Y] = 1
    one_hot_y = one_hot_y.T
    return one_hot_y


def deriv_Relu(Z):
    return Z > 0


def backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y):
    one_hot_Y = one_hot(Y)
    dZ2 = A2 - one_hot_Y
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2)
    dZ1 = W2.T.dot(dZ2) * deriv_Relu(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    db1 = 1 / m * np.sum(dZ1)
    return dW1, db1, dW2, db2


def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1
    W2 = W2 - alpha * dW2
    b2 = b2 - alpha * db2
    return W1, b1, W2, b2


def gradient_descent(X, Y, alpha, num_iterations):
    W1, b1, W2, b2 = init_params()
    for i in range(num_iterations):
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y)
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)
        if i % 50 == 0:
            print("Iteration: ", i)
            print("Accuracy: ", np.sum(np.argmax(A2, 0) == Y) / Y.size)
            print()
    return W1, b1, W2, b2


W1, b1, W2, b2 = gradient_descent(X_train, Y_train, 0.10, 500)
print(W1, b1, W2, b2)
