"""
A partir del código anterior (13_colecciones) solicitar al usuario un nombre a buscar
Si lo encuentra, mostrar sus nacionalidades
"""
usuarios = [
    {
        "nombre": "Cintia",
        "nacionalidades": ["argentina", "italiana"],
    },
    {
        "nombre": "Juan",
        "nacionalidades": ["española"],
    },
    {
        "nombre": "Liam",
        "nacionalidades": [],
    },
]
inexistente = True
nombre = input("Nombre: ")
for usuario in usuarios:
    if nombre == usuario["nombre"]:
        print(f"Usuario '{nombre}' encontrado ...")
        print(f"Su nacionalidad es {usuario.get('nacionalidades')}")
        inexistente = False

if inexistente:
    print("El nombre no existe en la lista ...")