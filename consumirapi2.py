# cliente.py

import requests

url = 'http://127.0.0.1:5000/tasks'  # URL de tu API

# Realizar la solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Imprimir el contenido de la respuesta (lista de diccionarios)
    datos = response.json()
    for d in datos:
        print(f"ID: {d['id']}, Nombre: {d['nombre']}")
else:
    # Imprimir un mensaje de error en caso de que la solicitud falle
    print('Error al llamar a la API:', response.status_code)
