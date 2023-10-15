'''
Desafío

Crear un función que permita identificar si un número entero es primo.

Debe retornar True si es primo y si no False
En caso que la función reciba el número 1 = False
'''
num = int(input("Digite un numero entero: "))

def es_primo(numero):
    if numero == 1:
        return False
    elif numero % 2 == 0:
        return True
    else:
        return False

print(es_primo(num))