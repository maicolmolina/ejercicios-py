"""
escribe una funcion para clasificar si una sustancia es acida
basica o neutra  a partir de su ph
"""
def sustancia(ph):
    if ph < 7 :
        return "acida"
    elif ph > 7:
        return " basica"
    else:
        return "neutra"
resultado = sustancia(7)
print(resultado)
