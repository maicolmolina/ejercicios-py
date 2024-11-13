"""
simular un lanzamiento de dado hasta obtener 6
"""
import random
numero = 0
while numero !=6:
    numero = random.randint(1,6)
print(f"has sacado un {numero}")
print("sacaste un 6")
