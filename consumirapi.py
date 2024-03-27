import requests
#libreria para consumir API
#se ocupa url de la API
url = "https://127.0.0.1:5000/tasks"
#el request va a hacer un get hacia la url y traera datos. Response es la variable y url
response = requests.get(url)

#verificar si esta activo (200)
if response.status_code == 200:
    data = response.json()
    #imprime si estuvoexitosa la conexion
    print("Solicitud exitosa")
    #imprime el json que se esta generando
    print("Datos: ", data)
else:
    #el text traera devuleta el error o porque no se consumió la API
    print("Error en la solicitud ", response.text)