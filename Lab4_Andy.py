import numpy as np
import matplotlib.pyplot as plt

class Lab_4:
    def __init__(self, var):
        self.var = var

    def Fun(self, x1, x2, x3, x4):
        return (((not(x3)) or x4) and (not(x1))) or x2

    def Boolean(self):
        mass = np.zeros((16, 5), dtype=np.int32)
        J0 = 0
        J1 = 0
        for i in range(16):
            b = str(bin(i)[2:])
            while len(b) < 4:
                b = '0' + b
            for j in range(4):
                mass[i][j] = b[j]
            mass[i][4] = self.Fun(mass[i][0], mass[i][1], mass[i][2], mass[i][3])
            if mass[i][4] == 0:
                J0 += 1
            J1 = 16 - J0
        return mass, J0, min(J0, J1)








# ----------------------------------------
# Запуск программы
# ----------------------------------------

Work = Lab_4(9)
Work.Boolean()

# ----------------------------------------
