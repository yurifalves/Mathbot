import numpy as np
from scipy import linalg


def formatar_matriz(matriz: np.ndarray) -> str:
    matriz_formatada = np.array2string(matriz, separator='  ')[1:-1].replace(' [', '[')
    return matriz_formatada


texto1 = """
[3 5 7 0 8 1]
[1 2 8 9 11]
"""


class Matriz:
    """
    formato do texto:

    Uma matriz de ordem m x n, aij ∈ ℝ
    [a11 a12 a13 ... a1n]
    [a21 a22 a23 ... a2n]
    [a31 a32 a33 ... a3n]
              .
              .
              .
    [am1 am2 am3 ... amn]
    """

    def __init__(self, texto):
        lista_numeros = []
        for caractere in texto:
            if caractere.isdecimal() and caractere not in lista_numeros: texto = texto.replace(caractere, f'{caractere},')
            lista_numeros.append(caractere)

        texto = eval('[' + texto.replace(']', '],') + ']')
        self._matriz = np.array(texto)
        self.matriz_formatada = formatar_matriz(self._matriz)
        self.tamanho = self._matriz.shape

    def matriz_inversa(self):
        try:
            matriz_inversa = linalg.inv(self._matriz, overwrite_a=True, check_finite=False)
            return formatar_matriz(matriz_inversa)
        except Exception:
            return 'Nâo foi possível realizar a operação'

    def matriz_transposta(self):
        return self._matriz.T

    def determinante(self):
        try:
            determinante = linalg.det(self._matriz, overwrite_a=True, check_finite=False)
            return determinante
        except Exception:
            return 'Nâo foi possível realizar a operação'


print(Matriz(texto1).matriz_transposta())
