import numpy as np
from scipy import linalg
import sympy


def texto_para_matriz(texto: str) -> np.ndarray:
    """
    Converte um texto para uma matriz, eliminando espaços e quebras de linha em excesso.

    Ex:

    '''
    1 2    3,21 7          np.array([[1, 2, 3.21, 7],
    4  5 6  20     --->              [4, 5, 6, 20],
    7 8 9   1                        [7, 8, 9, 1]])
    '''

    :param texto: String a ser convertida.
    :return: array 2-D.
    """
    texto = texto.strip().replace(',', '.')

    def remove_element(element, the_list):
        while element in the_list: the_list.remove(element)
        return the_list

    vetores_linha_str = remove_element('', texto.splitlines())  # ['4 11 62', '-8 0 1', '3 3 0']
    vetores_linha = [np.fromstring(linha, sep=' ') for linha in
                     vetores_linha_str]  # [array([ 4., 11., 62.]), array([-8.,  0.,  1.]), array([3., 3., 0.])]
    matriz = np.array(vetores_linha)
    return matriz


def matriz_para_texto(matriz: np.ndarray) -> str:
    """
    np.array([[a11, a12, a13],       '[a11  a12  a13]
              [a21, a22, a23],  --->  [a21  a22  a23]
              [a31, a32, a33]])       [a31  a32  a33]'
    :param matriz: array 2-D.
    :return: O array convertido e formatado em string.
    """
    return np.array2string(matriz, separator='  ')[1:-1].replace(' [', '[')


class Matriz:
    """
    formato da string:

    [a11 a12 a13 ... a1n]
    [a21 a22 a23 ... a2n]
    [a31 a32 a33 ... a3n]
              .
              .
              .
    [am1 am2 am3 ... amn]
    """

    def __init__(self, texto: str):
        lista_numeros = []
        for caractere in texto:
            if (caractere.isdecimal() and caractere not in lista_numeros) and (
                    not texto[texto.index(caractere) + 1].isdecimal()): texto = texto.replace(caractere,
                                                                                              f'{caractere},')
            lista_numeros.append(caractere)

        texto = eval('[' + texto.replace(']', '],') + ']')
        self._matriz = np.array(texto)
        self.matriz_formatada = matriz_para_texto(self._matriz)
        self.tamanho = self._matriz.shape

    def forma_reduzida(self):
        M = sympy.Matrix(self._matriz)
        forma_reduzida = np.array(M.rref(pivots=False))
        return matriz_para_texto(forma_reduzida)

    def inversa(self):
        try:
            matriz_inversa = linalg.inv(self._matriz, overwrite_a=True, check_finite=False)
            return matriz_para_texto(matriz_inversa)
        except Exception:
            return 'Nâo foi possível realizar a operação'

    def transposta(self):
        return matriz_para_texto(self._matriz.T)

    def determinante(self):
        try:
            determinante = linalg.det(self._matriz, overwrite_a=True, check_finite=False)
            return determinante
        except Exception:
            return 'Nâo foi possível realizar a operação'


if __name__ == '__main__':
    texto = """
    [1 2 3]
    [4 5 6]
    """

    A = Matriz(texto)
    print(A.forma_reduzida())
