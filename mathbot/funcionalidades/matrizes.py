def forma_escalonada_reduzida(matriz):
    import sympy
    import numpy as np
    matriz = np.array(matriz)
    M = sympy.Matrix(matriz)
    forma_escalonada_reduzida = np.array(M.rref(pivots=False), dtype=float)
    return forma_escalonada_reduzida


def determinante(matriz):
    from scipy import linalg
    import numpy as np
    matriz = np.array(matriz)
    determinante = linalg.det(matriz, overwrite_a=True, check_finite=False)
    return determinante


def matriz_inversa(matriz):
    from scipy import linalg
    import numpy as np
    matriz = np.array(matriz)
    matriz_inversa = linalg.inv(matriz, overwrite_a=True, check_finite=False)
    return matriz_inversa


def matriz_transposta(matriz):
    import numpy as np
    matriz = np.array(matriz)
    matriz_transposta = matriz.T
    return matriz_transposta


def matriz_adjunta(matriz):
    from scipy import linalg
    import numpy as np
    matriz = np.array(matriz)
    determinante = linalg.det(matriz, overwrite_a=True, check_finite=False)
    matriz_inversa = linalg.inv(matriz, overwrite_a=True, check_finite=False)

    matriz_adjunta = determinante * matriz_inversa
    return matriz_adjunta


def matriz_dos_cofatores(matriz):
    from scipy import linalg
    import numpy as np
    matriz = np.array(matriz)
    determinante = linalg.det(matriz, overwrite_a=True, check_finite=False)
    matriz_inversa = linalg.inv(matriz, overwrite_a=True, check_finite=False)

    matriz_adjunta = determinante * matriz_inversa

    matriz_dos_cofatores = matriz_adjunta.T
    return matriz_dos_cofatores


if __name__ == '__main__':
    A = [[1, 4, 5, 7],
         [2, 9, 5, 0],
         [2, 9, 9, 0],
         [-1, -4, -5, 0]]
    print(matriz_dos_cofatores(A))
