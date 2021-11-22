import numpy as np

a = np.array([1, 2, 3, 4, 5], int)
fnet = 1 / (1 + np.exp(-(a)))
print(fnet)