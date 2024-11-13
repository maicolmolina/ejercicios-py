"""
crear una clase circulo con los siguientes atributos
* radio_ radio del circulo
la clase denbe tener los siguientes metodos 
*_init_(self, radio): inicializa los atributos de la clase 
calcular_area(self): calcula y devuelve el area del circulo
calcular_perimetro(self): clacula y devuelve el perimetro del circulo
"""

import math
class circulo:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area (self):
         return math.pi * self.radio ** 2
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
circulo1 = circulo(5)

print(f"el area es:{circulo1.calcular_area()}")
print(f"perimetro:{circulo1.calcular_perimetro()}")
