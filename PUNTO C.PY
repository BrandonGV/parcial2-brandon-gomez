import json

data = {
  "house stark": {
    "rickard": {
      "hijos": ["bejem", "brandon", "lyanna", "wylla", "eddard"]
    },
    "wylla": {
      "hijos": ["jon snow"]
    },
    "eddard": {
      "hijos": ["robb", "sansa", "arya", "bran", "rickon"]
    }
  },
  "house tully": {
    "robik": {
      "hijos": ["catelyn", "lysa", "edmure"]
    },
    "hoster": {
      "hijos": ["catelyn", "lysa", "edmure"]
    }
  },
  "catelyn": {
    "hijos": ["robb", "sansa", "arya", "bran", "rickon"]
  },
  "robb": {
    "perro": "gray wind"
  },
  "sansa": {
    "perro": "lody"
  },
  "arya": {
    "perro": "nymeric"
  },
  "bran": {
    "perro": "summer"
  },
  "rickon": {
    "perro": "shaggydog"
  }
}

# Convertir a formato JSON
json_data = json.dumps(data, indent=4)

# Guardar en un archivo
with open("arbol_genealogico.json", "w") as file:
    file.write(json_data)
#escribir
archivo = open("arbol_genealogico.json", "r")
#leer json
contenido = json.load(archivo)
print(contenido)



print("PUNTO D.La descendencia de rickard:         ")
descendencia_rickard = data['house stark']['rickard']['hijos']
descendencia_catelyn = data['catelyn']['hijos']
descendencia_eddard = data['house stark']['eddard']['hijos']

descendencia_total = descendencia_rickard + descendencia_catelyn + descendencia_eddard
print(descendencia_total)

print("PUNTO E.LISTAR PERSONAJES SEGUN LA CASA:         ")
for house, members in data.items():
    print(f"{house}")

    # Iterate over each member in the house
    for member, details in members.items():
        print(f"Member: {member}")

        # Check if member has children
        if "hijos" in details:
            children = details["hijos"]
            print(f"Children: {', '.join(children)}")

        # Check if member has a dog
        if "perro" in details:
            dog = details["perro"]
            print(f"Dog: {dog}")

        print()  # Empty line for separation
print("PUNTO F.CREAR Y ELIMINAR LA CASA TYRELL:            ")
# Agregar la casa Tyrell
data["house tyrell"] = {
    "mace": {
        "hijos": ["margaery", "loras"]
    }
}

# Convertir el diccionario modificado de vuelta a JSON
json_data_modificado = json.dumps(data)

# Imprimir el JSON con la casa Tyrell agregada
print(json_data_modificado)

# Eliminar la casa Tyrell
del data["house tyrell"]

# Convertir el diccionario modificado de vuelta a JSON
json_data_modificado = json.dumps(data)

# Imprimir el JSON con la casa Tyrell eliminada
print(json_data_modificado)
print("PUNTO G.CREAR LA CASA UNISANGIL CON 2 PERSONAJES:        ")
# Agregar la casa Unisangil
data["house unisangil"] = {
    "member1": {},
    "member2": {}
}

# Convertir el diccionario modificado de vuelta a JSON
json_data_modificado = json.dumps(data)

# Imprimir el JSON con la casa Unisangil y sus integrantes agregados
print(json_data_modificado)
print("PUNTO G.  modificar nombre del personaje tyrion de la casa lanister por tyrion king")

# Agregar la casa Lannister con Tyrion
data["house lannister"] = {
    "tyrion": {}
}

# Cambiar el nombre de Tyrion a Tyrion King
data["house lannister"]["tyrion king"] = data["house lannister"].pop("tyrion")

# Convertir el diccionario modificado de vuelta a JSON
json_data_modificado = json.dumps(data)

# Imprimir el JSON con la casa Lannister y el cambio de nombre realizado
print(json_data_modificado)