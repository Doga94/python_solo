class Persona():
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"mi nombre es {self.nombre} y tengo {self.edad}, es un placer")

#Esto es una forma de agregar documento
'''
class Documento(Persona):
    def __init__(self, nombre, edad, cedula) -> None:
        super().__init__(nombre, edad)
        self.cedula = cedula

    def ingresar_documento(self):
        print(f"El documento de {self.nombre} es: {self.cedula}")
'''
class Documento(Persona):
    def __init__(self, nombre, edad) -> None:
        super().__init__(nombre, edad)
        self.cedula = None

    def ingresar_documento(self):
        if self.cedula is None:
            self.cedula = input("Ingrese documento: ")
        print(f"El documento de {self.nombre} es {self.cedula}")

perosna_1 = Persona("David", 29)
perosna_1.saludar()
print(perosna_1.edad)


perosna_1 = Documento(perosna_1.nombre, perosna_1.edad)
perosna_1.ingresar_documento()
print(perosna_1.cedula)


'''
documento_1 = Documento(perosna_1.nombre, perosna_1.edad, 12355555)
documento_1.ingresar_documento()
'''

