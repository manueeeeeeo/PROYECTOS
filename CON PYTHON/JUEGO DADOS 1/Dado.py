# Importamos las librerias necesarias
import random

# Creamos una clase
class Dado:

    def __init__(self):
        self.nCara = 0

    def lanzarDado(self):
        self.nCara = random.randint(1, 6)
