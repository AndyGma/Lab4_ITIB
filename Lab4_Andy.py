import numpy as np
import matplotlib.pyplot as plt

class Lab_4:
    def __init__(self, var):
        self.var = var

    def Fun(self, x1, x2, x3, x4):
        return (((not(x3)) or x4) and (not(x1))) or x2

    def Boolean(self):
        mass = np.zeros((16, 5), dtype=np.int32)
        mass0 = np.empty((0, 4), int)
        mass1 = np.empty((0, 4), int)

        for i in range(16):
            b = str(bin(i)[2:])
            while len(b) < 4:
                b = '0' + b
            for j in range(4):
                mass[i][j] = b[j]
            mass[i][4] = self.Fun(mass[i][0], mass[i][1], mass[i][2], mass[i][3])
            if mass[i][4] == 0:
                mass0 = np.vstack((mass0, mass[i][:-1]))
            else:
                mass1 = np.vstack((mass1, mass[i][:-1]))
        if len(mass0) <= len(mass1):
            mass_C = mass0
        else:
            mass_C = mass1
        print(f"Массив C: \n{mass_C}\n")

        return mass


# ----------------------------------------
# Запуск программы
# ----------------------------------------
if __name__ == "__main__":
    Work = Lab_4(9)
    Work.Boolean()


# ----------------------------------------
