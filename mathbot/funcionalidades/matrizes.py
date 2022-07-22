import numpy as np
from scipy import linalg
import sympy


class Matriz:

    def __init__(self, matriz):
        self._matriz = matriz
        self.tamanho = matriz.shape

    def forma_escalonada_reduzida(self):
        M = sympy.Matrix(self._matriz)
        forma_escalonada_reduzida = np.array(M.rref(pivots=False))
        return forma_escalonada_reduzida

    def inversa(self):
            matriz_inversa = linalg.inv(self._matriz, overwrite_a=True, check_finite=False)
            return matriz_inversa

    def transposta(self):
        return self._matriz.T

    def determinante(self):
        determinante = linalg.det(self._matriz, overwrite_a=True, check_finite=False)
        return determinante


if __name__ == '__main__':
    A = np.array([
        [1, 0, 0],
        [4, 5, 6],
        [7, 7, 9]
    ])

    A = Matriz(A)
    print(A.forma_escalonada_reduzida())
