"""
A partir de dos variables llamadas nombre y edad:
crear una variable que almacene si se cumplen las siguientes condiciones,
y mostrar al usuario True o False:
    - nombre sea diferente de cuatro asteriscos ****
    - edad sea mayor que 5 y a su vez menor que 20
    - Que la longitud de nombre sea mayor o igual a 4 pero a la vez menor que 8
    - No debes usar funciones, condicionales, bucles o cualquier
    - otra instrucción que no hayamos visto
"""
nombre=str(input("Ingresa nombre: "))
edad=int(input("Ingresa edad: "))

usuario=""
if(nombre != '****' and edad > 5 and edad < 20 and len(nombre) >= 4 and len(nombre) < 8):
    usuario=True
else:
    usuario=False

print(usuario)


# Resolución profe

# Entrada
nombre = input("Nombre: ")
edad = int(input("Edad: "))

# Operaciones
validacion_nombre = nombre != "****"
validacion_nombre_len = len(nombre) >= 4 and len(nombre) < 8
validacion_edad = edad > 5 and edad < 20

validacion = validacion_nombre and validacion_nombre_len and validacion_edad

# Salida
print(validacion)

# MVC
# Modelo: datos-> tablas de bases de datos
# Vista: visualización -> HTML, CSS
# Controlador: operaciones -> Python