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


def resolver_sistemalinear(matriz_aumentada):
    import numpy as np

    matriz_aumentada = np.array(matriz_aumentada)

    A = matriz_aumentada[:, :-1]
    b = matriz_aumentada[:, -1]

    x = np.linalg.solve(A, b)
    return x



if __name__ == '__main__':
    import numpy as np

    matriz_aumentada = np.array([
        [5, -2, 5, -5, 6, -8, -9],
        [-6, 6, -3, 1, 4, -8, -5],
        [-5, 5, -7, 3, -4, 3, 21],
        [-1, -4, -9, 6, 9, 5, 26],
        [7, 5, -8, -4, 7, -6, 65],
        [4, -1, -3, 5, -3, -5, 149]
    ])
    print(resolver_sistemalinear(matriz_aumentada))
