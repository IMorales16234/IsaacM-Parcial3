import json

file_name= "data.json"

with open(file_name) as data:
    datos = json.load(data)
print(datos["ip"], datos["so"], datos["version"][0], datos["hostname"], datos["cpu"])