class Clase:

    def __init__(self, codigo, nombre, precio, hora, min, duracion, apuntadas):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.hora = hora
        self.min = min
        self.duracion = duracion
        self.apuntadas = apuntadas
    
    def verInfo(self):
        print(f"CLASE {self.nombre} con código: {self.codigo} \nPrecio: {self.precio}€ \nDuración: {self.duracion}")
