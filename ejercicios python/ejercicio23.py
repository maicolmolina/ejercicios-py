"""
verifica si una palabra es un palindromo
sabemos que es palindromo cuando se lea de adelante asia atras
la misma palabra 
"""
palabra="radar"

es_pa=palabra == palabra[::-1]

print("es palindromo",es_pa)
