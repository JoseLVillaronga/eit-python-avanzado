"""
A partir de la siguiente lista:
matriz:
matriz = [
    [1, 20, 3],
    [4, 3, 2],
    [10, 4, 1],
]
Sumar los elementos de cada lista y agregar el resultado
al final de cada lista. Debe quedar de la siguiente forma:
matriz = [
    [1, 20, 3, 24],
    [4, 3, 2, 9],
    [10, 4, 1, 15],
]
Puedes usar la función sum(<lista>)
"""
# Se define "matriz"
matriz = [
    [1, 20, 3],
    [4, 3, 2],
    [10, 4, 1],
]
# Muestra "matriz"
print(matriz)

# Se suma los elementos de las listas y se agrega el resultado al final de la lista 
for lista in matriz:
    lista.append(sum(lista))

# Muestra resultado
print(matriz)