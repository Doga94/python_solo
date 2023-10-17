'''
Desafío
Ordenar una lista de números enteros de menor a mayor usando un algoritmo "ordenamiento burbuja"
'''

def ordena_burbuja(lista):
    longitud = len(lista)

    for x in range(longitud - 1):
        for y in range(longitud -1 -x):
            if lista[y] > lista[y+1]:
                lista[y], lista[y+1] = lista[y+1], lista[y]

lista_num = [1,7,6,3,9,2]
ordena_burbuja(lista_num)

print(lista_num)