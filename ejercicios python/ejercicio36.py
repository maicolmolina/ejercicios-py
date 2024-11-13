"""
pide un caracter y determine si es una vocal
"""
caracter=input("ingresa caracter")
vocales =["a","e","i","o","u"]
if caracter.lower()in vocales:
    print("es una vocal")
else:
    print("no es una vocal")
