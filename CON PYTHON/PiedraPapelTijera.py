#Importamos las librerias necesarias
import random

#Declaramos las variables necesarias
opciones = ["piedra", "papel", "tijera"]
scorePc = 0
scoreUser = 0
veces = 0

#Pedimos el número de juegos que quiere el usuario
veces = int(input("Cuantas partidas quieres hechar? "))
print()

#Hacemos el bucle principal
while veces != 0:
    veces -= 1
    bot = random.choice(opciones)
    user = input("Ingrese piedra, papel o tijera: ").lower()
    if bot == user:
        print(f"EMPATE\n")
    elif (bot == "piedra" and user == "tijera") or (bot == "papel" and user == "piedra") or (bot == "tijera" and user == "papel"):
        print(f"El bot eligio {bot} - PERDISTE!!\n")
        scorePc += 1
    else:
        print(f"El bot eligio {bot} - GANASTE!!\n")
        scoreUser += 1

# Cuando sale del bucle imprimimos quien ha ganado o si han empatado
print(f"\n================== FINAL DE LA PARTIDA ==================")
if scoreUser > scorePc:
    print(f"HA GANDO EL USUARIO\nRESULTADO:\tUSER: {scoreUser}\tPC: {scorePc}")
elif scoreUser < scorePc:
    print(f"HA GANDO EL PC\nRESULTADO:\tUSER: {scoreUser}\tPC: {scorePc}")
else:
    print(f"HAN EMPATADO\nRESULTADO:\tUSER: {scoreUser}\tPC: {scorePc}\n")
