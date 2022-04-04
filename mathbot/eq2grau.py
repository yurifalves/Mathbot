def eq2grau(a, b, c):
    import math
    discriminante = b ** 2 - 4 * a * c
    if discriminante >= 0:
        x1, x2 = (-b + math.sqrt(discriminante)) / (2 * a), (-b - math.sqrt(discriminante)) / (2 * a)
        return f'X1 = {x1:.2f}\nX2 = {x2:.2f}'
    else:
        discriminante = abs(discriminante)
        x1_a, x1_b = -b / (2 * a), math.sqrt(discriminante) / (2 * a)
        x2_a, x2_b = -b / (2 * a), -math.sqrt(discriminante) / (2 * a)
        if x1_b < 0:
            x1 = f'{x1_a:.2f} - {abs(x1_b):.2f}i'
        else:
            x1 = f'{x1_a:.2f} + {x1_b:.2f}i'
        if x2_b < 0:
            x2 = f'{x2_a:.2f} - {abs(x2_b):.2f}i'
        else:
            x2 = f'{x2_a:.2f} + {x2_b:.2f}i'
        return f'X1 = {x1}\nX2 = {x2}'
