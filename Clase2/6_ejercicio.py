"""
Una empresa debe aprobar o no un crédito para un cliente.
Las condiciones son las siguientes:
    - El cliente debe ser mayor de edad.
    - Debe tener una antigüedad en el sistema financiero mínimo de 3 años
    y un ingreso mayor a 2500 dólares.
    - En caso de que no tenga la antigüedad suficiente,
    su ingreso mensual debe ser como mínimo 4000 dólares.
Si no cumple ninguna de las condiciones, no se aprueba el crédito.
"""
edad = int(input("Ingresa edad: "))
antiguedad = int(input("Ingresa antiguedad: "))
ingreso = int(input("Ingresa Sueldo: "))

if edad < 19:
    print("rechazado")
elif antiguedad > 2 and ingreso > 2500:
    print("concedido")
elif ingreso > 4000 and antiguedad < 3:
    print("concedido")
else:
    print("rechazado")

# Alt 1

"""
Convertir el siguiente código con bloques if-elif-else
para evitar anidaciones

edad = int(input("Edad: "))

if edad < 13:
    print("eres niño")
else:
    if edad < 18:
        print("eres adolescente")
    else:
        if edad < 65:
            print("eres adulto")
        else:
            if edad < 130:
                print("eres anciano")
"""

edad = int(input("Edad: "))

if edad < 0 or edad >= 130:
    print("Datos incorrectos")
elif edad < 13:
    print("eres niño")
elif edad < 18:
    print("eres adolescente")
elif edad < 65:
    print("eres adulto")
elif edad < 130:
    print("eres anciano")