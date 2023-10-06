usuarios = {
    "usuario_1": {
        "nombre": "David G",
        "edad": 29
    },
    "usuario_2": {
        "nombre": "Laura P",
        "edad": 25
    }
}

usuarios["usuario_1"].update({"pais": "Colombia"})
usuarios["usuario_2"].update({"pais": "Mexico"})
print(usuarios["usuario_1"])
print(usuarios["usuario_2"])

for x in usuarios.items():
    usuario = dict(x)
    if x["pais"] == "Colombia":
        x["Autorizacion"] = "requerida"
    elif x["pais"] == "Mexico":
        x["Autorizacion"] = "No requiere"
    for clave, valor in usuario.items():
        usuarios[clave] = valor

print(usuarios)


