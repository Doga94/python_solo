def generar_triangulo_pascal(n):
    triangulo = []
    for i in range(n):
        fila = [1]  # Cada fila comienza con un 1
        if triangulo:
            fila_anterior = triangulo[-1]
            for j in range(len(fila_anterior) - 1):
                suma = fila_anterior[j] + fila_anterior[j + 1]
                fila.append(suma)
            fila.append(1)  # Cada fila termina con un 1
        triangulo.append(fila)
    return triangulo

def imprimir_triangulo_pascal(triangulo):
    for fila in triangulo:
        print(" ".join(map(str, fila)).center(60))

n = int(input("Ingrese el número de filas para el Triángulo de Pascal: "))
triangulo = generar_triangulo_pascal(n)
imprimir_triangulo_pascal(triangulo)
