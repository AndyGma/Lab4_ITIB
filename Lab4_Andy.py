import numpy as np
import matplotlib.pyplot as plt

class Lab_4:
    def __init__(self, var):
        self.var = var

    def Fun(self, x1, x2, x3, x4):
        return (((not(x3)) or x4) and (not(x1))) or x2

    def Boolean(self):
        self.mass = np.zeros((16, 5), dtype=np.int32)
        self.mass0 = np.empty((0, 4), int)
        self.mass1 = np.empty((0, 4), int)

        for i in range(16):
            b = str(bin(i)[2:])
            while len(b) < 4:
                b = '0' + b
            for j in range(4):
                self.mass[i][j] = b[j]
            self.mass[i][4] = self.Fun(self.mass[i][0], self.mass[i][1], self.mass[i][2], self.mass[i][3])
            if self.mass[i][4] == 0:
                self.mass0 = np.vstack((self.mass0, self.mass[i][:-1]))
            else:
                self.mass1 = np.vstack((self.mass1, self.mass[i][:-1]))
        if len(self.mass0) <= len(self.mass1):
            self.mass_C = self.mass0
        else:
            self.mass_C = self.mass1
        self.mass_X = np.delete(self.mass, -1, axis=1)
        # print(f"Массив X полный: \n{self.mass}\n")
        # print(f"Массив C: \n{self.mass_C}\n")
        # print(f"Массив X: \n{self.mass_X}\n")
        return self

    def Net(self, x, c, v):
        net = v[0]
        for i in range(1, len(self.mass_C)):
            fi = np.exp(-(((x[0] - c[0])**2) + ((x[1] - c[1])**2) + ((x[2] - c[2])**2) + ((x[3] - c[3])**2)))
            net += v[i] *


# ----------------------------------------
# Запуск программы
# ----------------------------------------
if __name__ == "__main__":
    Work = Lab_4(9)
    Work.Boolean()


# ----------------------------------------
