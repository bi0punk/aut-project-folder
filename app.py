
import os






def pedirNumeroEntero():

    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


salir = False
opcion = 0

while not salir:
    print(chr(27)+"[1;33m"+"Texto en negrita de color amarillo")
    print("\x1b[1;33m"+"Texto en negrita de color amarillo")
    print("\033[4;35m"+"Texto en negrita y subrayado de color morado")
    
    print("\033[4;35m"+"Texto en negrita y subrayado de color morado")

    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Opcion 3")
    print("4. Salir")

    print("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        print("Opcion 1")
        if not os.path.exists('parentdirectory/mydirectory'):
            os.makedirs('parentdirectory/mydirectory')
    elif opcion == 2:
        print("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        salir = True
    else:
        print("Introduce un numero entre 1 y 3")

print("Fin")
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))


def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))


def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))


def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))


def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


prCyan("Hello World, ")
prYellow("It's")
prGreen("Geeks")
prRed("For")
prGreen("Geeks")
nombre = "Luis"
print("{:>20}|".format(nombre))