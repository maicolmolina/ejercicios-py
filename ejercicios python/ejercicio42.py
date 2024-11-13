"""
solicita al usuario ingresar un numero n y luego imprima la suma de todos los numeros 
desde 1 hasta n
"""
numero = int(input("ingrese un numero"))
suma = 0
i = 1
while i <= numero:
    suma += i
    i += 1
print("la suma es",suma)  
