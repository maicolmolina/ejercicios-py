"""
escribe una funcion para verificar si un numero es par
o impar
"""
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
resultado = es_par(7)
print(resultado)