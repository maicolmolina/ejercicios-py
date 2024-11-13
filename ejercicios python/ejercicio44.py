"""
genera un numero aleatorio entre 1 y 10
luego pide al ususari adivinar el numero
hasta que lo haga correctamente
"""
import random
numero_secreto = random.randint (1,10)
intentos = 0

while True:
    intentos =int(input("adivina el numero"))
    intentos = intentos + 1
    if intentos == numero_secreto:
        print(f"exito tomo {intentos} intentos")
        break
    