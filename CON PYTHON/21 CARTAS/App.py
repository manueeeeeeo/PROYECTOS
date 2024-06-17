from Carta import Carta

# Función para hacer un jugada
def jugada(carta, total):
    carta.extraerCarta()
    print(f"{carta.numero} {carta.palo}")
    total += carta.numero
    print(f"Suma Jugador: {total}")
    return total

# Función para saber si continua o no
def continuar(op):
    if op == "Si" or op == "si" or op == "S" or op == "s":
        return 1
    elif op == "No" or op == "no" or op == "N" or op == "n":
        return 0
    else:
        return 2

# Función para definir quien ha ganado
def ganado(total1, total2):
    print(f"\n=============== JUEGO FINALIZADO ===============\n")
    # Si un jugador pasa de 21 y el otro no, el que no pasa de 21 gana
    if total1 > 21 and total2 <= 21:
        print(f"HA GANADO EL JUGADOR 2\nJUGADOR 1\t{total1} : {total2} \tJUGADOR2")
    elif total2 > 21 and total1 <= 21:
        print(f"HA GANADO EL JUGADOR 1\nJUGADOR 1\t{total1} : {total2} \tJUGADOR2")
    # Si ambos están por debajo o igual a 21, el que tenga mayor puntaje gana
    elif total1 > total2 and (total1 <= 21):
        print(f"HA GANADO EL JUGADOR 1\nJUGADOR 1\t{total1} : {total2} \tJUGADOR2")
    elif total2 > total1 and (total2 <= 21):
        print(f"HA GANADO EL JUGADOR 2\nJUGADOR 1\t{total1} : {total2} \tJUGADOR2")
    else:
        print(f"HAN EMPATADO\nJUGADOR 1\t{total1} : {total2}\tJUGADOR2")

# Creamos los objetos
carta1 = Carta()
carta2 = Carta()

# Creamos las variables necesarias
total1 = 0
total2 = 0
num1 = 1
num2 = 1
op1 = ""
op2 = ""

print(f"================== TURNO JUGADOR 1 ==================")
while total1 < 21 and num1 == 1:
    total1 = jugada(carta1, total1)
    op1 = input("¿Quires continuar? S/n ")
    num1 = int(continuar(op1))
    print()

print(f"================== TURNO JUGADOR 2 ==================")
while total2 < 21 and num2 == 1:
    total2 = jugada(carta2, total2)
    op2 = input("¿Quires continuar? S/n ")
    num2 = int(continuar(op2))
    print()

# Para decidir el ganador
ganado(total1, total2)
