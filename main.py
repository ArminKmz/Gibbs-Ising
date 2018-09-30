import sample_ising
import numpy as np
import matplotlib.pyplot as plt


W = np.array([[0, -1, 0, 0, 0, 0, 0],
              [-1, 0, 1.5, 1, 0, 0, 0],
              [0, 1.5, 0, 0, 1.5, 2, -2],
              [0, 1, 0, 0, 0, 0, 0],
              [0, 0, 1.5, 0, 0, 0, 0],
              [0, 0, 2, 0, 0, 0, 0],
              [0, 0, -2, 0, 0, 0, 0]])
u = np.zeros(7)
d = W.shape[0]
n = 10000

samples = sample_ising.get_sample(W, u, n)

model = sample_ising.Ising(W, u)

X = [i+1 for i in range(n)]
Y = [model.energy(samples[i]) for i in range(n)]

plt.plot(X, Y, 'b')
plt.xlabel('samples')
plt.ylabel('energy')
plt.show()
