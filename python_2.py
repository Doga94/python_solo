'''
numero = int(input("Ingrese un numero mayor a 15: "))

while numero <= 15:
    print(f"El numero ingresado fue: {numero}")
    numero = int(input("Ingrese un numero mayor a 15: "))

print("El numero proporcionado es mayor a 15, Excelente")


print("Adivine el numero\ndel 1 al 15\n  ¡Suerte!")
numero_2 = int(input("Digite numero: "))
encontrar_num = int(8)

while True:
    print(f"El numero ingresado fue: {numero_2}")
    if numero_2 == encontrar_num:
        print("Felicidades encontro el numero escondido")
        break
    else:
        print("Siga intentando")
        numero_2 = int(input("Digite numero: "))
print("Esperamos que lo haya dosfrutado")

'''

print("En esta parte hare que cuente del 1 al 10")
num_ini = 0

while num_ini <= 10:
    print(num_ini)
    num_ini += 1
print(f"Llegamos al numero deseado")
