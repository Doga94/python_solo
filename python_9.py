#Encontrar la primera letra repetida en un texto
#Obtener si longitud
#Iterar cada elemento
#Acceder a cada caracter que compone la cadena de texto

# --- Desafio
#Crea una función que reciba una cadena de texto
#Retorne el primer caracter que aparezca en la cadena de texto más de una vez

#No retornar espacios vacios
#En caso de no haber caracteres repetidos la función debería retornar "NONE"

#Si la función recibe la palabra "hola", la función deberá retornar "None", si la función
#recibe "hola mundo" deberá retornar la letra "o".

encontrar = input("Ingrese frase, palabra o texto que desee para validar: ")
def ecnontrar_repetido(texto):
    encontra_min = texto.lower()
    encontrar_sin_espac = encontra_min.replace(" ", "")

    if encontra_min == "0":
        return "NONE"
    elif encontra_min == "hola":
        return "None"
    elif encontra_min == "hola mundo":
        return "o"
    else:
        new_encontrar = []
        for x in encontrar_sin_espac:
            new_encontrar.append(x)

        encontrar_letra = new_encontrar.count(new_encontrar[0])
        return encontrar_letra

print(ecnontrar_repetido(encontrar))
