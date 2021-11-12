import numpy as np
import matplotlib.pyplot as plt

class Lab_4:
    def __init__(self, var):
        self.var = var
        self.n = 0.3
        self.N = 0

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
        self.v = np.zeros(len(self.mass_C) + 1)
        self.y_pr = np.zeros(len(self.mass_X), dtype=np.int32)
        self.y_t = self.mass[:, 4]
        self.fi = np.zeros(len(self.mass_C), dtype=np.int32)

        print(f"Массив X полный: \n{self.mass}\n")
        print(f"Массив C: \n{self.mass_C}\n")
        print(f"Массив X: \n{self.mass_X}\n")
        return self

    def Net(self):
        for i_y16 in range(len(self.mass_X)):  # от 0 до 15
            # на входе X = 0000 (меняется) и C = 0010, 1000, 1001, 1010, 1011 (не меняются)

            for i_fi in range(len(self.mass_C)):  # от 0 до 4
                self.fi[i_fi] = np.exp(-(
                        ((self.mass_X[i_y16][0] - self.mass_C[i_fi][0]) ** 2) +
                        ((self.mass_X[i_y16][1] - self.mass_C[i_fi][1]) ** 2) +
                        ((self.mass_X[i_y16][2] - self.mass_C[i_fi][2]) ** 2) +
                        ((self.mass_X[i_y16][3] - self.mass_C[i_fi][3]) ** 2)))


            net = np.dot(self.fi, self.v[1:])
            net += self.v[0]

            if net >= 0:
                self.y_pr[i_y16] = 1
            else:
                self.y_pr[i_y16] = 0
            self.Teach(i_y16)

        self.Err = 0
        for i_check in range(len(self.y_t)):
            self.Err += np.abs(self.y_t[i_check] - self.y_pr[i_check])

    def Teach(self, i):
        # Здесь я должен обновлять веса
        delta = self.y_t[i] - self.y_pr[i]
        update = self.n * delta
        self.v[0] += update
        for j in range(1, len(self.mass_C)+1):
            self.v[j] += update * self.fi[j-1]

    def Epoch(self):
        self.Boolean()

        while True:
            self.Net()
            self.N += 1
            if self.Err == 0:
                break
        print(f"Кол-во эпох N = {self.N}")
        print(f"Значения целевые self.y_t : \n{self.y_t}")
        print(f"Значения полученые self.y_pr : \n{self.y_pr}")
        print(f"Синаптические веса self.v = \n{self.v}")

# ----------------------------------------
# Запуск программы
# ----------------------------------------
if __name__ == "__main__":
    Work = Lab_4(9)
    Work.Epoch()


# ----------------------------------------
