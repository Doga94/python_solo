def lo_que_sea():
    return "Lo que sea"

print(lo_que_sea())

#Return en funciones
def sumar(a,b):
    return a + b
print(f"La respuesta de la suma es: {sumar(5,6)}")

def multiplicar(a, b):
    return a*b
print(f"La respuesta de la multiplicación es: {multiplicar(5,6)}")

def maximo(a,b):
    if a > b:
        return a
    else:
        return b
print(f"El mayor es: {maximo(5,6)}")

def minimo(a,b):
    if a < b:
        return a
    else:
        return b
print(f"El menor es: {minimo(5,6)}")

#Invertir lista
lista = [1,2,3,4,5,6,7,8,9]
def invertir_lista(lista):
    lista_invertida = []
    for x in lista[::-1]:
        lista_invertida.append(x)
    return lista_invertida
print(f"Esta esa la lista original {lista}")
print(f"Esta es la lista invertida {invertir_lista(lista)}")

#Invertir Diccionario
diccionario = {
    "1": "Nombre",
    "2": "Edad",
    "3": "Ciudad"}

def invertir_dic(diccionario):
    dic_invertido = {}
    for clave, valor in diccionario.items():
        dic_invertido[valor] = clave
    return dic_invertido

print(f"Diccionario ral es {diccionario}")
print(f"El diccionario invertido es {invertir_dic(diccionario)}")