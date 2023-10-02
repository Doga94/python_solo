'''
lista = []

lista.append(2)
lista.append(3)
lista.append(1)
lista.append(3)

print(lista)
#print(lista[1])

#for x in lista:
# print(x)

print(f"La longitud de la lista es: {len(lista)}")
print(f"El indice de la del numero deseado es: {lista.index(1)}")
print(f"Cuantos 3 hay : {lista.count(3)}")
print(f"Vamos a ordenar la lista: {lista} va a salir ordenada asi: lista.sort()")
lista.sort()
print(f"Quedo ordenada: {lista}")
print(f"Vamos a desordenar la lista: {lista} va a salir ordenada asi: reverse.sort()")
lista.reverse()
print(f"Quedo ordenada: {lista}")



lista_2 = [1, 2, 3, 4, 5]
lista_par = list(filter(lambda x: x % 2 == 0, lista_2))
print(lista_par)


lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista.sort()

print(f"Vamos a sacar de esta lista {lista} los numeros que sean divisibles en 3")
for x in lista:
    if x % 3 == 0:
        print(x)
'''
print("Crearemos un rango de 2 a 6")
rango = range(2,7)
for x_1 in rango:
    print(x_1)

print("Imprimiremos un rango de 2 a 10 de 2 en 2:")
for i in range(2, 11, 2):
    print(i)
