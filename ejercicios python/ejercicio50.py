"""
mostrar los numero del 1 al 100
pero remplazando los multiplos de 3
por fizz y los multiplos de 5 por buzz
"""
numero = 1

while numero <= 100:
    if numero % 3 == 0 and numero % 5 == 0:
        print("fizzbuzz")
    elif numero % 3 == 0:
     print("fizz")
    elif numero % 5 == 0:
       print(numero)
    numero = numero + 1
    
       