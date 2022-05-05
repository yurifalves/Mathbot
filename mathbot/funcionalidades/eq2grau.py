def eq2grau(a, b, c):
    from cmath import sqrt

    discriminante = b**2 - 4*a*c
    x1, x2 = (-b + sqrt(discriminante))/2, (-b - sqrt(discriminante))/2
    if '-' in str(b) and '-' in str(c):
        equacao = f'{a}x²{b}x{c}'
    if '-' in str(b) and '-' not in str(c):
        equacao = f'{a}x²{b}x+{c}'
    if '-' not in str(b) and '-' not in str(c):
        equacao = f'{a}x²+{b}x+{c}'
    if '-' not in str(b) and '-' in str(c):
        equacao = f'{a}x²+{b}x{c}'

    if x1.imag == 0:
        x1 = x1.real
    else:
        x1 = str(x1).replace('(', '').replace(')', '').replace('j', 'i')
    if x2.imag == 0:
        x2 = x2.real
    else:
        x2 = str(x2).replace('(', '').replace(')', '').replace('j', 'i')

    return f'{equacao}\nx1 = {x1}, x2 = {x2}'


if __name__ == '__main__':
    print(eq2grau(4, -4, 2))
