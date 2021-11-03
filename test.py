import numpy as np

a = np.empty((0, 2), int)
b = np.array([[5, 6], [7, 8]])
c = np.array([[9, 10], [11, 12]])
res_v = np.vstack((a, b, c))
print("res_v = ", res_v)
