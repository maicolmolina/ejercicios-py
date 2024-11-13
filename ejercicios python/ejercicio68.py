"""
escribe una funcion que pida por teclado
la distancia y la velocidad para 
poder calcular el tiempo de viaje 
"""
def tiempo_viaje():
    distancia = int(input("escribe la distancia"))
    velocidad = int(input("escribe la velocidad"))
    return distancia/velocidad
resultado = tiempo_viaje()
print(resultado)

    