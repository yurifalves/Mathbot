def trig(angulo):
    import math
    import time
    start_time = time.time()
    ang = math.radians(angulo)
    seno, cos, tg = math.sin(ang), math.cos(ang), math.tan(ang)
    result = f"""
    Considerando o ângulo {angulo:.2f}° = {ang:.2f}rad
    Sen({angulo}°) = {seno:.2f}
    Cos({angulo}°) = {cos:.2f}
    Tg({angulo}°) = {tg:.2f}
    
tempo de execução: {time.time() - start_time:.3f} s
    """
    return result
