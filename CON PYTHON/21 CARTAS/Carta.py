# Agregamos las librerias necesarias
import random

# Creamos una clase
class Carta:

    def __init__(self):
        self.numero = 0
        self.palo = ""
    
    def extraerCarta(self):
        aleatorio = 8
        palo1 = ""
        Palos = ["Oros", "Bastos", "Espadas", "Copas"]
        while (aleatorio==8 or aleatorio==9):
            aleatorio = random.randint(1, 12)
        palo1 = random.choice(Palos)
        self.numero = aleatorio
        self.palo = palo1
