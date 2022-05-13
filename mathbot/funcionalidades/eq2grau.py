def eq2grau(a, b, c):
    from cmath import sqrt
    a_eq, b_eq, c_eq = str(a).replace('.', ','), str(b).replace('.', ','), str(c).replace('.', ',')

    if '-' in str(b) and '-' in str(c):
        equacao = f'{a_eq}x²{b_eq}x{c_eq}'
    if '-' in str(b) and '-' not in str(c):
        equacao = f'{a_eq}x²{b_eq}x+{c_eq}'
    if '-' not in str(b) and '-' not in str(c):
        equacao = f'{a_eq}x²+{b_eq}x+{c_eq}'
    if '-' not in str(b) and '-' in str(c):
        equacao = f'{a_eq}x²+{b_eq}x{c_eq}'

    if a == 0:
        x1 = x2 = -c/b
        x1 = str(x1).replace('.', ',')
        x2 = str(x2).replace('.', ',')
    else:
        discriminante = b ** 2 - 4*a*c
        x1, x2 = (-b + sqrt(discriminante)) / (2*a), (-b - sqrt(discriminante)) / (2*a)
        x1 = str(x1).replace('(', '').replace(')', '').replace('.', ',').replace('j', 'i')
        x2 = str(x2).replace('(', '').replace(')', '').replace('.', ',').replace('j', 'i')

    return f'{equacao}\nx₁ = {x1}\nx₂ = {x2}'


if __name__ == '__main__':
    print(eq2grau(4.43294832, 4.4329432, 2.432423))
