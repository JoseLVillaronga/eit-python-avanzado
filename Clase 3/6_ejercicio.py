"""
✨ EJERCICIO ✨
A partir del siguiente diccionario, realizar los ejercicios propuestos:
inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 8
}
1. Se compraron 5 manzanas.
2. Se vendieron 3 naranjas.
3. Se compraron 5 uvas.
4. Solicitar al usuario qué producto está buscando, y, si está disponible,
pedir la cantidad, venderlo y mostrar el inventario. La cantidad no debe superar el stock.
"""
inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 8
}
inventario['manzanas']+=5
inventario['naranjas']-=3
inventario['uvas'] = 5
busca = input("Que producto esta buscando ?")
if str(busca) in inventario:
    print(f"{busca} esta disponible")
    cantidad = input("Cuantas quiere ? ")
    if (inventario[busca] - int(cantidad)) >= 0:
        inventario[busca] = inventario[busca] - int(cantidad)
    else:
        print(f"No hay suficientes{busca}")
else:
    print(f"{busca} no esta disponible")

print(inventario)