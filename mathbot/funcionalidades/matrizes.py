import numpy as np
from scipy import linalg
import sympy


class Matriz:

    def __init__(self, matriz):
        self._matriz = matriz
        self.tamanho = f'{matriz.shape[0]}×{matriz.shape[1]}'
        self.determinante = linalg.det(self._matriz, overwrite_a=True, check_finite=False)

    def forma_escalonada_reduzida(self):
        M = sympy.Matrix(self._matriz)
        forma_escalonada_reduzida = np.array(M.rref(pivots=False))
        return forma_escalonada_reduzida

    def matriz_inversa(self):
        matriz_inversa = linalg.inv(self._matriz, overwrite_a=True, check_finite=False)
        return matriz_inversa

    def matriz_transposta(self):
        return self._matriz.T

    def matriz_adjunta(self):
        adjunta = self.determinante * self.matriz_inversa()
        return adjunta

    def matriz_dos_cofatores(self):
        cofatores = self.matriz_adjunta().T
        return cofatores

if __name__ == '__main__':
    A = np.array([
        [1, 2],
        [3, 4]
    ])

    A = Matriz(A)
    print(A.matriz_dos_cofatores())
