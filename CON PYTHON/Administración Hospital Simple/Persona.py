class Persona:

    def __init__(self, codigo, nombre, apes, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.apes = apes
        self.edad = edad
    
    def verInfo(self):
        print(f"Cliente:\n{self.nombre} {self.apes}\nEdad: {self.edad}\nCódigo: {self.codigo}")
