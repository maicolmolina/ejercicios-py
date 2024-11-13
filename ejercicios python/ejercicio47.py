"""
hacer un menu de opciones que incluya la opcion 
de salir del programa

"""
while True:
    print("1 sumar")
    print("2 restar")
    print("3 salir")

opcion = int(input("escriba tu opcion"))

if opcion == 1:
    print ("usted esta sumando ")
elif opcion == 2:
    print ("usted esta restando")
elif opcion == 3: 
    break
else:
    print(" no es una opcion valida")

print("vuelve pronto")


    
    