#UN SISTEMA DE BANCO EN DONDE INICIAMOS SESIÓN Y PODEMOS VER NUESTRO SALDO, HACER INGRESO Y RETIROS PASANDO POR
#UNOS FILTROS PARA EVITAR ERRORES
#Declaramos las variables
usuario = "admin"
clave = 123456
saldo = 1000
op = 0

#Función del menu principal
def menuPrincipal():
    print(f"\n################# BANCO ESPAÑA #####################")
    print(f"Elija una opción:")
    print(f"\n1º Ver Saldo\n2º Hacer Ingreso\n3º Retirar Dinero\n4º Salir")
    opcion = input("¿Que opción desea? ")
    opcion = int(opcion)
    print(f"\n")
    return opcion

#Función para ver tu saldo
def verSaldo():
    print(f"{saldo} €")

#Función para hacer un ingreso
def ingreso(saldo1):
    print(f"\nUsted ha señalado hacer un ingreso")
    ingre = input("¿Cuánto desea ingresar? ")
    ingre = int(ingre)
    if ingre==0:
        print(f"NO PUEDES INGRESAR 0 €")
    elif ingre < 0:
        print(f"NO PUEDES INGRESAR UNA CANTIDAD NEGATIVA")
    else:
        saldo1 += ingre
        return saldo1


#Función para hacer un retiro
def retiro(saldo1):
    print(f"\nUsted ha señalado hacer un retiro")
    reti = input("¿Cuánto desea retirar? ")
    reti = int(reti)
    if reti==0:
        print(f"NO PUEDES RETIRAR 0 €")
    elif reti < 0:
        print(f"NO PUEDES RETIRAR UNA CANTIDAD NEGATIVA")
    elif reti > saldo:
        print(f"NO TIENES SUFICIENTE SALDO EN LA CUENTA")
    else:
        saldo1 -= reti
        return saldo1


#Hacemos un bucle para pedir las claves y el username y volver a pedirlo en caso de que no seán correctas, indicamos cual es la incorrecta
while True:
    aux_user = input("Digame el nombre del usuario: ")
    aux_clave = input("Digame la clave del usuario: ")
    aux_clave = int(aux_clave)
    if aux_user == usuario:
        if aux_clave == clave:
            print(f"Bienvenido al Sistema del Banco\n")
            break;
        else:
            print(f"La clave no es la correcta")
    else:
        print(f"No es correcto el usuario")

#Hacemos el bucle principal en donde ejecutamos el programa hasta que se pida salir
while True:
    op = menuPrincipal()
    if op == 1:
        verSaldo()
    elif op == 2:
        saldo = ingreso(saldo)
    elif op == 3:
        saldo = retiro(saldo)
    elif op == 4:
        break
    else:
        print(f"Esa opción no está disponible, lo sentimos")
    print(f"\n")
