import numpy as np

np.random.seed(0)

def get_sample(W, u, n):
    '''
        input:
            W -> interaction matrix
            u -> spin site vector
            n -> number of samples
        return:
            samples (n x d matrix)
    '''
    ising_model = Ising(W, u)
    return gibbs_sampling(ising_model, n)



def gibbs_sampling(model, n):
    X = np.array([+1 if np.random.rand() < .5 else -1 for i in range(model.d)])
    samples = [np.copy(X)]
    for i in range(2*n + 100):
        for j in range(model.d):
            p = model.conditonal(j, X)
            X[j] = +1 if np.random.rand() < p else -1
        samples.append(np.copy(X))
    return np.array(samples[100::2])

class Ising:
    def __init__(self, W, u):
        assert(W.shape[0] == W.shape[1] and W.shape[0] == u.shape[0])
        assert(np.allclose(W, W.T, atol=1e-8))
        self.W = W
        self.u = u
        self.d = W.shape[0]
        self.neighbours = [[j for j in range(self.d) if W[i, j]] for i in range(self.d)]

    def conditonal(self, i, X):
        '''
            return P(x_i=+1|other)
        '''
        def sigmoid(x):
            return 1. / (1 + np.exp(-x))
        tmp = self.W[i, :].dot(X)
        return sigmoid(2 * tmp + self.u[i])

    def energy(self, X):
        return -X.dot(self.W).dot(X) - X.dot(self.u)
