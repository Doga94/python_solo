'''
Convertir una lista anidada en una lista unidimensional

'''

lista_dos_dimensiones = [[1,2,3],[4,5,6],[7,8,9]]

#Lista vacia donde almacenare la lista unidimensional
lista_unidimensional = []

#recorrer la lista de dos dimensiona para ingresarlas a la lista vacia unidimensional
for x in lista_dos_dimensiones:
    for e in x:
        lista_unidimensional.append(e)

#validamos si quedo ok la lista unidimensional
print(f"Lista unidimensional {lista_unidimensional}")
print(f"Lista normal {lista_dos_dimensiones}")