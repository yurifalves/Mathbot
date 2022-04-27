def eq2grau(a, b, c):
    from cmath import sqrt
    equacao = f'{a}x²+{b}x+{c}'
    discriminante = b**2 - 4*a*c
    x1, x2 = (-b + sqrt(discriminante))/2, (-b - sqrt(discriminante))/2
    if x1.imag == 0:
        x1 = x1.real
    else:
        x1 = f'{x1.real} + {x1.imag}i'
    if x2.imag == 0:
        x2 = x2.real
    else:
        x2 = f'{x2.real} + {x2.imag}i'
    return f'{equacao}\nx1 = {x1}, x2 = {x2}'


if __name__ == '__main__':
    print(eq2grau(1, -3, -4))
