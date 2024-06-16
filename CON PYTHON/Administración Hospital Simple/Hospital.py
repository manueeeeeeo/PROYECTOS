#Importamos las librerias necesarias
import csv
from Persona import Persona

#Declaro las variables
op = 0

#Función que imprime el menu principal
def menuPrincipal():
    print(f"========== SISTEMA HOSPITAL ==========")
    print(f"Opciones: ")
    print(f"1º Ver Todos Los Clientes\n2º Ver Un Cliente\n3º Agregar Nuevo Cliente\n4º Salir")
    opcion = input("Digame la opción: ")
    opcion = int(opcion)
    return opcion

#Función para ver todos los clientes
def verTodosLosClientes():
    print(f"\nCLIENTES:")
    with open('DIRECCION/SISTEMA HOSPITAL/Clientes.csv/SISTEMA HOSPITAL/Clientes.csv') as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            print("-{0} {1} {2}".format(row[0], row[1], row[2]))
    print()

#Ver un cliente en especifio con su codigo
def verUnCliente(cod):
    print(f"\nCLIENTE CON CÓDIGO {cod}:")
    with open('DIRECCION/SISTEMA HOSPITAL/Clientes.csv/SISTEMA HOSPITAL/Clientes.csv') as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            if cod == row[0]:
                print("-{0} {1} {2} \n Edad: {3}".format(row[0], row[1], row[2], row[3]))
    print()

#Función para agregar un nuevo cliente a la lista
def agregarCliente():
    print(f"\nAGREGAR CLIENTE:")
    nombre = input("Digame el nombre: ")
    apes = input("Digame el apellido: ")
    edad = input("Digame la edad: ")
    codig = input("Digame el código: ")
    per = Persona(codig, nombre, apes, edad)
    with open('DIRECCION/SISTEMA HOSPITAL/Clientes.csv', "a", newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow([per.codigo, per.nombre, per.apes, per.edad])
    print(f"Agregado Cliente Correctamente")
    print()

#Bucle principal de la app
while True:
    op = menuPrincipal()
    if op == 1:
        verTodosLosClientes()
    elif op == 2:
        ide = input("Digame el código: ")
        verUnCliente(ide)
    elif op == 3:
        agregarCliente()
    elif op == 4:
        print()
        break
    else:
        print(f"Esa opción no existe, lo sentimos")
