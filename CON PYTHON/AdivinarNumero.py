#Agregamos las librerias necesarias
import random

#Agregamos las variables necesarias
numero = random.randint(1, 30)
intentos = 0
acertaste = False

while not acertaste:
    intentos+=1
    num = int(input("Digame un número entre el 1 y el 30: "))
    if num > numero:
        print(f"Un número más bajo")
    elif num < numero:
        print(f"Un número más alto")
    elif num == numero:
        print(f"MUY BIEN!!! ACERTASTE en {intentos} intentos\nEl número es: {numero}")
        break
