'''
Anagramas:

Palabras direfentes que contienen las mismas letras pero en diferente orden.

Desafío
Crea una función que determine si dos palabras son anagramas.

Debe retornar en booleano True si son anagramas o False si no son anagramas
No debe haber distinción entre mayúsculas y minúsculas
Se pueden convertir todas las letras a minúsculas
'''
anagrama_1 = input("Ingrese la primera palabra: ")
anagrama_2 = input("Ingrese la segunda palabra: ")
def anagrama(texto_1, texto_2):
    #los pasamos a minusculas
    anagrama_1_minu = texto_1.lower()
    anagrama_2_minu = texto_2.lower()

    #eliminaremos espacios si los llegran a ver
    anagrama_1_sin_esp = anagrama_1_minu.replace(" ", "")
    anagrama_2_sin_esp = anagrama_2_minu.replace(" ", "")

    # Almacenamos las letras en listas
    anagrama_1_val = list(anagrama_1_sin_esp)
    anagrama_2_val = list(anagrama_2_sin_esp)

    # Ordenamos las letras en las listas
    anagrama_1_val.sort()
    anagrama_2_val.sort()

    #Condicion
    if anagrama_1_val == anagrama_2_val:
        print(True)
    else:
        print(False)

anagrama(anagrama_1, anagrama_2)

