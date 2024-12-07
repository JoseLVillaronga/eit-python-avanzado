"""
Escribir un programa que le solicite al usuario
su nombre, edad, dirección y,
que, posteriormente, lo muestre por pantalla:
Ejemplo del output solicitado:
Juan tiene 25 años, y vive en Carrera 7 - Bogotá
Usar un diccionario para guardar los datos del usuario.
"""
nombre = input("Nombre: ")
print(f"El nombre ingresado es {nombre}")
edad = input("Edad: ")
print(f"La edad ingresada es {edad}")
direccion = input("Dirección: ")
print(f"La dirección ingresada es {direccion}")
datos_usuario = {"nombre": nombre,"edad": edad,"direccion": direccion}
print(datos_usuario)
# Solución clase

# Entrada
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
direccion = input("Ingrese su dirección: ")

# Crear la estructura de datos
formulario: dict[str, str]  # Anotaciones e tipo o type hints
formulario = {"nombre": nombre,"edad": edad,"direccion": direccion}

# Salida
print(f"El nombre ingresado es {formulario['nombre']}")
print(f"La edad ingresada es {formulario['edad']}")
print(f"La dirección ingresada es {formulario['direccion']}")