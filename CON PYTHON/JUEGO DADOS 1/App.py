from Dado import Dado

# Función para ver quien ha ganado
def ganado(num1, num2):
    print(f"\n================= FINAL PARTIDA =================\n")
    if num1 > num2:
        print("Ha ganado el Jugador 1")
    elif num1 < num2:
        print("Ha ganado el Jugador 2")
    else:
        print("Han empatado")

# Función para lanzar los dados de un jugador
def lanzar_dados():
    num = 0
    jug = []
    for _ in range(7):
        dado = Dado()
        dado.lanzarDado()  # Llamar a la función lanzarDado
        if dado.nCara == 6:
            num += 1
        jug.append(dado.nCara)
    return num, jug

print(f"\n======================== JUEGO DE LOS DADOS ========================")

# Lanzar dados para los dos jugadores
num1, jug1 = lanzar_dados()
num2, jug2 = lanzar_dados()

# Mostrar resultados
print(f"Resultados Jugador 1: {jug1} - Número de 6s: {num1}")
print(f"Resultados Jugador 2: {jug2} - Número de 6s: {num2}")

# Determinar quién ha ganado
ganado(num1, num2)
