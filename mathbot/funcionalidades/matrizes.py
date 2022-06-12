import numpy as np
from scipy import linalg


def formatar_matriz(matriz: np.ndarray) -> str:
    matriz_formatada = np.array2string(matriz, separator='  ')[1:-1].replace(' [', '[').replace('.', ',')
    return matriz_formatada


texto1 = """
[2 1]
[1 3]
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
        for caractere in texto:
            indice_caractere = texto.index(caractere)
            if caractere.isdecimal(): texto = texto.replace(caractere, f'{caractere},', 1)

        texto = eval('[' + texto.replace(']', '],') + ']')
        self._matriz = np.array(texto)
        self.matriz_formatada = formatar_matriz(self._matriz)
        self.tamanho = self._matriz.shape

    def matriz_inversa(self):
        try:
            matriz_inversa = linalg.inv(self._matriz, overwrite_a=True, check_finite=False)
            return formatar_matriz(matriz_inversa)
        except Exception:
            return 'Ocorreu algo errado'

    def determinante(self):
        try:
            determinante = linalg.det(self._matriz, overwrite_a=True, check_finite=False)
            return determinante
        except Exception:
            return 'Ocorreu algo errado'
