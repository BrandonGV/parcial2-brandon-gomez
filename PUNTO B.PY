import json

data = {
    "raza": {
        "orcos": {
            "clases": {
                "guerrero": {
                    "vida": 100,
                    "id": 1,
                    "ataque": 50,
                    "defensa": 30,
                    "poder mágico": 20
                },
                "chaman": {
                    "vida": 80,
                    "id": 2,
                    "ataque": 20,
                    "defensa": 40,
                    "poder mágico": 60
                },
                "jinete": {
                    "vida": 120,
                    "id": 3,
                    "ataque": 70,
                    "defensa": 20,
                    "poder mágico": 10
                }
            }
        },
        "humanos": {
            "clases": {
                "guerrero": {
                    "vida": 90,
                    "id": 1,
                    "ataque": 40,
                    "defensa": 35,
                    "poder mágico": 15
                },
                "jinete": {
                    "vida": 100,
                    "id": 2,
                    "ataque": 60,
                    "defensa": 25,
                    "poder mágico": 5
                },
                "mago": {
                    "vida": 70,
                    "id": 3,
                    "ataque": 30,
                    "defensa": 20,
                    "poder mágico": 80
                },
                "recolector": {
                    "vida": 80,
                    "id": 4,
                    "ataque": 20,
                    "defensa": 15,
                    "poder mágico": 10
                },
                "observador": {
                    "vida": 60,
                    "id": 5,
                    "ataque": 10,
                    "defensa": 10,
                    "poder mágico": 40
                }
            }
        }
    }
}
#escribir
archivo = open("razas.json", "r")
#leer json
contenido = json.load(archivo)
print(contenido)

archivo.close()



# Convertir a formato JSON
json_data = json.dumps(data, indent=4)

# Guardar en un archivo
with open("razas.json", "w") as file:
    file.write(json_data)
