'''
Desafío

Crear una función que permita identificar los elementos duplicados de una lista.

La función recibira una lista de elementos
Retornara una nueva lista únicamente con los elementos repetidos de la lista recibida

En caso de que la lista no tenga elementos repetidos, la función deberá retorna una lista vacía.
'''

lista_veri = input("Ingrese numeros entero dejando un espacio entre ellos o una coma : ")

def elem_repetidos(lista):
    lista_sin_espa = lista.replace(" ", "")
    lista_sin_coma = lista_sin_espa.replace(",", "")

    lista_1 = []
    lista_repetidos = []
    for x in lista_sin_coma:
        if x in lista_1:
            lista_repetidos.append(x)
        lista_1.append(x)
    return lista_repetidos

repetidos_son = elem_repetidos(lista_veri)
print(repetidos_son)