import numpy as np
from scipy import linalg


def texto_para_matriz(texto):
    """

    Converte um texto para uma matriz, eliminando espaços e quebras de linha em excesso.

    Ex:

    '''
    1 2    3,21 7        np.array([[1, 2, 3.21, 7],
    4  5 6  20   --->              [4, 5, 6, 20],
    7 8 9   1                      [7, 8, 9, 1]])
    '''

    :param texto: string no formato

    a11 a12 ... a1n
    a21 a22 ... a2n
    am1 am2 ... amn

    :return: matriz no formato

    np.array([[a11, a12, ... a1n],
              [a21, a22, ... a2n],
              [a31, a32, ... amn]])

    """
    texto = texto.strip().replace(',', '.')
    
    
    def remove_element(element, the_list):
        while element in the_list: the_list.remove(element)
        return the_list

    vetores_linha_str = remove_element('', texto.splitlines())  # ['4 11 62', '-8 0 1', '3 3 0']
    vetores_linha = [np.fromstring(linha, sep=' ') for linha in vetores_linha_str]  # [array([ 4., 11., 62.]), array([-8.,  0.,  1.]), array([3., 3., 0.])]
    matriz = np.array(vetores_linha)
    return matriz



def formatar_matriz(matriz: np.ndarray) -> str:
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
            if (caractere.isdecimal() and caractere not in lista_numeros) and (not texto[texto.index(caractere)+1].isdecimal()): texto = texto.replace(caractere, f'{caractere},')
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
        return formatar_matriz(self._matriz.T)

    def determinante(self):
        try:
            determinante = linalg.det(self._matriz, overwrite_a=True, check_finite=False)
            return determinante
        except Exception:
            return 'Nâo foi possível realizar a operação'

    def solucao_sistemalinear(self):
        """
        Ax = b
        A: Matriz de coeficientes
        b: Vetor coluna
        x: Resposta procurada

        Só funcionará para uma matriz de ordem m x n, com m=n-1

        :return: Matriz reduzida por linhas.
        """
        try:
            A = self._matriz  # Matriz aumentada
            num_linhas, num_colunas = A.shape[0], A.shape[1]
            b = A[:, num_colunas-1:].T[0]
            A = A[:, 0:num_colunas-1]

            x = linalg.solve(A, b, overwrite_a=True, overwrite_b=True)  # array([x1, x2, x3, ...])

            solucao = str()
            for i in range(x.size):
                solucao += f'x{i + 1} = {x[i]}\n'

            return solucao
        except Exception:
            return 'Algum erro ocorreu. Tente novamente.'


if __name__ == '__main__':
    texto = """
    [1 1 1]
    [1 1 1]
    """
    A = Matriz(texto)
    print(A.solucao_sistemalinear())
