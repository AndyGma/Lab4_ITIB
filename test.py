import numpy as np

a = np.empty((0), int)
a = np.hstack((a, 5))
a = np.hstack((a, 6))

print(a)
