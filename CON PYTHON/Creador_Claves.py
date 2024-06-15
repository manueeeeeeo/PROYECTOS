import random

caracteres = 'abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY!@$%^*&().,)0123456789'

print(f"GENERADOR DE CONTRASEÑAS\n=================================\n")

numero = input("¿Cuantas claves quieres generar? ")
numero = int(numero)
longitud = input("¿Qué longitud quiere que tengan las claves? ")
longitud = int(longitud)

print(f"\nAquí tiene sus contraseñas: ")

for pwd in range(numero):
    claves = ''
    for c in range(longitud):
        claves += random.choice(caracteres)
    print(claves)
