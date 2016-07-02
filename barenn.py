import numpy as np

#sigmoid
def nonlin(x,deriv = False):
    if(deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

#input dataset
X = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]])

y = np.array([[0, 0, 1, 1]]).T

#random seed
np.random.seed(1)

#initialize weights
syn0 = 2 * np.random.random((3, 1)) - 1

for iter in range(10000):

    #forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))

    #sum miss
    l1_error = y - l1

    l1_delta = l1_error * nonlin(l1, True)

    #update weights
    syn0 += np.dot(l0.T, l1_delta)

print("Output After Training:")
print(l1)
