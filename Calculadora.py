def suma(n1,n2):
    return print(n1+n2)

def resta(n1,n2):
    return print(n1-n2)

def multiplicacion(n1,n2):
    a = n1 * n2
    return a

def division(n1,n2):
    a = n1 / n2
    return a

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
while True:
    opcion = int(input("Que quieres hacer con los numeros?4\n1.-Sumar\n2.-Restar\n3.-Multiplicar\n4.-Dividir\n0.-Salir"))

    if (opcion == 1):
        suma(n1,n2)

    elif (opcion == 2):
        suma(n1,n2)

    elif (opcion == 3):
        suma(n1,n2)

    elif (opcion == 4):
        suma(n1,n2)

    elif (opcion == 0):
        break
