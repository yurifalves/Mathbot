def grafico(angulo):
    import matplotlib.pyplot as plt
    import numpy as np
    ang = np.radians(angulo)
    x = np.linspace(angulo - 180, angulo + 180, 1000)
    y1 = np.sin(np.radians(x))
    y2 = np.cos(np.radians(x))
    y3 = np.tan(np.radians(x))
    plt.plot(x, y1, label="Seno", color="sandybrown")
    plt.plot(x, y2, label="Cosseno", color="red")
    plt.plot(x, y3, label="Tangente", color="green")
    plt.plot([angulo, angulo, angulo], [np.sin(ang), np.cos(ang), np.tan(ang)], 'bs')
    plt.legend(loc="upper left")
    plt.ylim(-1.5, 2.0)
    plt.savefig(f'trigonometria({angulo}).png')
    plt.close()
    return open(f'trigonometria({angulo}).png', 'rb')


def trig(angulo):
    import math
    ang = math.radians(angulo)
    seno, cos, tg = math.sin(ang), math.cos(ang), math.tan(ang)
    ang_congruo = angulo
    while ang_congruo > 360:
        ang_congruo -= 360
        result = f"""
        Considerando o ângulo {angulo:.2f}°
    Sen({angulo}°) = Sen({ang_congruo}°) = {seno:.2f}
    Cos({angulo}°) = Cos({ang_congruo}°) = {cos:.2f}
    Tg({angulo}°) = Tg({ang_congruo}°) = {tg:.2f}
        """
    while ang_congruo < 0:
        ang_congruo += 360
        result = f"""
        Considerando o ângulo {angulo:.2f}°
    Sen({angulo}°) = Sen({ang_congruo}°) = {seno:.2f}
    Cos({angulo}°) = Cos({ang_congruo}°) = {cos:.2f}
    Tg({angulo}°) = Tg({ang_congruo}°) = {tg:.2f}
        """
    return result
