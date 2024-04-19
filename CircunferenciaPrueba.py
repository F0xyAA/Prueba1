import math

def calcular_circunferencia(radio):
    pi = round(math.pi, 6)  # Valor de pi redondeado a 6 decimales
    circunferencia = 2 * pi * radio
    return circunferencia

radios = [3, 8, 10]

for radio in radios:
    circunferencia = calcular_circunferencia(radio)
    mensaje = f"Para un radio de {radio}, la circunferencia es aproximadamente {circunferencia:.6f}"
    print(mensaje)