def suma(num1, num2):
    sum = int(num1) + int(num2)
    return sum

def resta(num1,num2):
    rest = int(num1) - int(num2)
    return rest

def multi(num1,num2):
    mu = int(num1) * int(num2)
    return mu

def div(num1,num2):
    di = int(num1)/int(num2)
    return di

def saber(num1):
    mensaje = ""
    if num1%2==0:
        mensaje = "par"
    else:
        mensaje = "impar"
    return mensaje

def menu():
    print(f"========================CALCULADORA========================")
    print(f"Eliga un opción:")
    print(f"1º) Suma")
    print(f"2º) Resta")
    print(f"3º) Multiplicación")
    print(f"4º) División")
    print(f"5º) Saber si es par o impar")
    print(f"6º) Salir")

while True:
    menu()
    resp = input(f"\nDigame la opción elegida: ")
    if resp == "1":
        n1 = input(f"Digame el primer número: ")
        n2 = input(f"Digame el segundo número: ")
        print(f"\nLa suma de {n1} y {2} es: {suma(n1,n2)}\n")
    elif resp == "2":
        n1 = input(f"Digame el primer número: ")
        n2 = input(f"Digame el segundo número: ")
        print(f"\nLa resta de {n1} y {2} es: {resta(n1,n2)}\n")
    elif resp == "3":
        n1 = input(f"Digame el primer número: ")
        n2 = input(f"Digame el segundo número: ")
        print(f"\nLa multiplicación de {n1} y {2} es: {multi(n1,n2)}\n")
    elif resp == "4":
        n1 = input(f"Digame el primer número: ")
        n2 = input(f"Digame el segundo número: ")
        print(f"\nLa división de {n1} y {2} es: {div(n1,n2)}\n")
    elif resp == "5":
        n1 = input(f"Digame un número número: ")
        print(f"\nEl número {n1} es: {saber(n1)}\n")
    elif resp == "6":
        break
    else:
        print(f"\nLO SENTIMOS, PERO ESA OPCIÓN NO EXISTE\n")
