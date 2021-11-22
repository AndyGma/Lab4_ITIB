import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Lab_4:
    def __init__(self, var, method):
        self.var = var
        self.method = method
        self.n = 0.1
        self.n_it = 100
        self.N = 0
        self.Error = np.array([], int)

    def Fun(self, x1, x2, x3, x4):
        if self.var == 2:  # Аня
            return (((not (x3)) or x4) and (not (x1))) or x2
        if self.var == 9:  # Андрей
            return (x1 or x2 or x3) and (x2 or x3 or x4)

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

    def gauss_FA(self, X):
        fj_x = []
        for ci in self.mass_C:
            fj_x.append(np.exp(-np.sum((X - ci) ** 2)))
        return fj_x

    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.v[1:]) + self.v[0]

    def kvant(self, x):
        return 1 if x >= 0 else 0

    def predict(self, X):
        """Return class label after unit step"""
        return 1 if self.net_input(self.gauss_FA(X)) >= 0 else 0

    def Net_porog(self):
        self.Boolean()
        self.errors_ = []
        report = []
        print(self.mass_X.shape)
        for _ in range(self.n_it):
            errors = 0
            for xi, target in zip(self.mass_X, self.y_t):
                fj_x = np.array(self.gauss_FA(xi))
                predict = self.net_input(fj_x)
                # print(predict, target)
                update = self.n * (target - self.kvant(predict))
                self.v[1:] += update * fj_x
                self.v[0] += update
                errors += int((update != 0))
            report.append([np.round(self.v, 3), errors])
            self.errors_.append(errors)
            if errors == 0:
                break
            pd.DataFrame(report).to_html("Пороговая ФА.html")
        return self


    def Paint(self):
        plt.title(f"График суммарной ошибки НС по эпохам обучения")
        plt.xlabel("N, эпоха обучения")
        plt.ylabel("Error, кол-во ошибок")
        plt.grid()
        plt.plot(range(1, self.N + 1), self.Error, '-o', c='deepskyblue', label='Y_ist')
        plt.legend()
        plt.show()

# ----------------------------------------
# Запуск программы
# ----------------------------------------
if __name__ == "__main__":
    """Пороговая ФА"""
    Work = Lab_4(9, 1)  # var, method
    Work.Net_porog()
    print(Work.errors_)

    for xi, target in zip(Work.mass_X, Work.y_t):
        print(f"{xi} --> {Work.predict(xi)}; Целевое = {target}")
    print(Work.v)

    plt.plot(range(1, len(Work.errors_) + 1), Work.errors_, marker='o')

    plt.show()


# ----------------------------------------
