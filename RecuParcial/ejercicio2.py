import json
import requests

def pornombre(item):
    return item["name"]

def get_data(ruta):
    req = requests.get(ruta)
    if req.status_code == 200:
        dic= json.loads(req.text)
        return dic

def get_data_sw_characters():
    sw_data = []
    result = get_data("https://swapi.dev/api/people/")
    while(result["next"] is not None):
        for doc in result["results"]:
            sw_data.append(doc)
        result = get_data(result["next"])
    return sw_data

sw_data = get_data_sw_characters()

sw_data.sort(key=pornombre)

print("Respuesta 2.A")
for character in sw_data:
    print(character["name"], character["height"], "cm", len(character["films"]), "peliculas")
print("")
print("")
print("Respuesta 2.B")
for character in sw_data:
    if character["name"].startswith("D" or "C") or character["name"].endswith("s"):
        print(character["name"])