import requests
from datetime import datetime

API_KEY = "77e0ef2391beb0447e0edefa6ccc134b"
ciudad = "Rafael Calzada"
URL = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
)
amenecer = ""
anochecer = ""

respuesta = requests.get(URL)
if respuesta.status_code == 200:
    diccionario = respuesta.json()
    temperatura = diccionario["main"]["temp"]
    clima = diccionario["weather"][0]["description"]
    amanecer = datetime.fromtimestamp(diccionario["sys"]["sunrise"])
    amanecer = amanecer.strftime('%Y-%m-%d %H:%M:%S')
    anochecer = datetime.fromtimestamp(diccionario["sys"]["sunset"])
    anochecer = anochecer.strftime('%Y-%m-%d %H:%M:%S')
    humedad = diccionario["main"]["humidity"]
    presion = diccionario["main"]["pressure"]
    print(f"En la ciudad de {ciudad} hay una temperatura de {temperatura}ºC, humedad {humedad}% y la presión es {presion}Hp")
    print(f"Clima: {clima}")
    print(f"Amanecer de hoy {amanecer} anochecer de hoy {anochecer}")
else:
    print(respuesta.status_code)