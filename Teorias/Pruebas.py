import json

# Lista de números enteros
numeros = [1, 2, 3, 4, 5]

# Serializar la lista en formato JSON
json_string = json.dumps(numeros)

print(json_string) # "[1, 2, 3, 4, 5]"
