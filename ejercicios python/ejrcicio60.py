"""
imprimir la suma de los numeros pares del 1 al 10 utilizando el ciclo for 
"""

suma_pares = 0
for i in range(1, 11):
    if i % 2 == 0:
        suma_pares =suma_pares + i
print("suma de pares es", suma_pares)
