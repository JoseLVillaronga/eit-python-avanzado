"""
Crear una tupla que represente un cajón de verduras
Crear otra tupla que represente un cajón de frutas
Crear una tupla llamada camion, que contenga los dos cajones anteriores
Mostrar los datos
"""
cajon_verduras = ("zanahorias", "papas", "repollo", "cebollas")
cajon_frutas = ("manzanas", "naranjas", "peras", "uvas")
# Cargarmos el camión 1
camion1 = (cajon_frutas, cajon_verduras)
print("Camión 1:", camion1)
# Descargamos camión 1
frutas, verduras = camion1
print("Cajón de verduras:", verduras)
print("Cajón de frutas:", frutas)
# Cargamos camión 2
camion2 = cajon_frutas + cajon_verduras
print("Camión 2", camion2)
# Cargamos camión 3
camion3 = (*cajon_frutas, *cajon_verduras)
print("Camión 3", camion3)

cajon_verduras = ("zanahorias", "papas", "repollo", "cebollas")
cajon_frutas = ("manzanas", "naranjas", "peras", "uvas")
# Cargarmos el camión 1
camion1 = (cajon_frutas, cajon_verduras)
print("Camión 1:", camion1)
# Descargamos camión 1
frutas, verduras = camion1
print("Cajón de verduras:", verduras)
print("Cajón de frutas:", frutas)
# Cargamos camión 2
camion2 = cajon_frutas + cajon_verduras
print("Camión 2", camion2)
# Cargamos camión 3
camion3 = (*cajon_frutas, *cajon_verduras)
print("Camión 3", camion3)

# alt 1

cajon_verduras = ("zanahorias", "papas", "repollo", "cebollas")
cajon_frutas = ("manzanas", "naranjas", "peras", "uvas")

# Cargarmos el camión 1
camion1 = (cajon_frutas, cajon_verduras)
print("Camión 1:", camion1)

# Descargamos camión 1
frutas, verduras = camion1
print("Cajón de verduras:", verduras)
print("Cajón de frutas:", frutas)

# Cargamos camión 2
camion2 = cajon_frutas + cajon_verduras
print("Camión 2", camion2)

# Cargamos camión 3
camion3 = (*cajon_frutas, *cajon_verduras)
print("Camión 3", camion3)