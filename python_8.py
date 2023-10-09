#Palindromo
'''
def palindromos():
    palindromo = input("Ingrese una palabra o frase: ")
    palindromo_min = palindromo.lower()
    palindromo_min_esp = palindromo_min.replace(" ", "")
    palindromo_1 = []
    for x in palindromo_min_esp:
        palindromo_1.append(x)
    if palindromo_1 == palindromo_1[::-1]:
        print(f"Es palindromo: {palindromo}")
    elif palindromo_1[::-1] == palindromo_1:
        print(f"Es palindromo: {palindromo}")
    else:
        print(f"No es palindromo: {palindromo}")

palindromos()
'''

def es_poli():
    poli = input("Ingrese una palabra o frase: ")
    poli_min = poli.lower()
    poli_sin_esp = poli_min.replace(" ", "")
    return poli_sin_esp == poli_sin_esp[::-1]

es_poli()