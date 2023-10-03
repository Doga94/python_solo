'''
tuplar = (1, "Hola", True)
print(f"Esta es la tupla original {tuplar}")

lista = list(tuplar)
lista[1] = "Saludo"
print(f"Esta es la lista modificada {lista}")

tupla_1 = tuple(lista)
print(f"Esta es la nueva tupla {tupla_1}")
print(type(tupla_1))


continentes = ("Asia", "África", "Europa", "Oceanía", "América")

#Encuentra el índice del continente "Europa".
print(continentes.index("Europa"))
#Cuenta el número de veces que aparece el continente "África".
print(continentes.count("África"))
#Ordena la tupla de menor a mayor.
tupla_ordenada = sorted(continentes)
print(tupla_ordenada)
'''


tupla_numeros = tuple(range(1,10))
print(tupla_numeros)

print(tupla_numeros.index(5))
print(tupla_numeros.count(2))

for x in tupla_numeros:
    print(x)

if 10 in tupla_numeros:
    print("Esta el numero buscado")
else:
    print("No esta el numero deseado")