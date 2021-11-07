import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], int)
print(f"Массив a:\n{a}\n")
b = np.delete(a, -1, axis=1)
print(f"Массив b:\n{b}\n")