"""
crear una clase rectangulo con los siguientes atributos 
base : base del rectangulo
altura: altura del rectangulo
la clase debe tener los siguientes metodos
**_init_(self,base,altura): inicializa
los atributos de la clase
** calcular:area(self): calcula y devuelve el perimetro del rectangulo
"""

class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
rec1 = rectangulo(5, 3)
print(f"area:{rec1.calcular_area()}")
print(f"perimetro:{rec1.calcular_perimetro()}")

