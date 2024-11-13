"""
escribe una funcion para calcular el volumen de un cilindro 
"""
import math
def volumen_cilindro (radio,altura):
    return math.pi * radio ** 2 * altura
resultado = volumen_cilindro(3,5)
print(resultado)
