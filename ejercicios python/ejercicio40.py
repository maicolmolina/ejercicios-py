"""
calcular el imc e intrepetarlo
el imc es peso sobre altura al cuadrado

para interpetarlo se tomo los datos de la tablara imc 
"""
peso= 80
altura= 1.75

imc=peso/(altura**2)
print(imc)
"""
los datos siguientes son los datos que nos dan la tabla para que el peso y la atura nos 
diga si esta pasado de peso o no 
"""
if imc < 18.5:
    print("bajo peso")
elif imc < 25:
    print("peso normal")
elif imc < 30:
    print("sobre peso")
elif imc < 35:
    print("obesidad grado 1")
elif imc < 40:
    print("obesidad grado 2")
else:
    print("obesidad grado 3")
 