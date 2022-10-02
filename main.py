import os
from prettytable import PrettyTable
from colorama import Fore, Back, Style




class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")








x = PrettyTable()
def menu():
    print("\t\nSelecciona una opcion\n")
    print("\t#############################################################################################")
    wd = os.getcwd()
    print(Fore.GREEN + "\t# Entorno de trabajo ")
    print("\t#")

    print("\t#")
    print("\t1.- Simple Python Script")
    print("\t2.- Simple Empty Flask Application")
    print("\t3.- Simple Empty Flask Application with Virtual Environment (venv)")
    print("\t4.- Flask Aplication with V/e + Boostrap v4/v5")
    print("\t5.- Flask Aplication with V/e + Boostrap v4/v5 + Login Module and Templates (Basic)")
    print("\t6.- Flask Aplication with V/e + Boostrap v4/v5 + Login Module and Templates (Login + Sidebar and/or Navbar)")
    print("\t7.- Salir")


def simple_script():
    print("Creacíon de estructura de proyecto para script siemple")
    __project_name__ = input("Ingrese el nombre del proyecto: ")
    print("El nombre del proyecto es " +str(__project_name__) )


while(True):

    menu()
    opcionMenu = input("\n Opción >>> ")

    if opcionMenu == "1":
        simple_script()

    elif opcionMenu == "2":
        print("")
    elif opcionMenu == "3":
        print("")
    elif opcionMenu == "4":
        print("")
    elif opcionMenu == "5":
        print("")
    elif opcionMenu == "6":
        print("")
    elif opcionMenu == "9":
        break
    else:
        print("")
        input("Ingrese ...\npulsa una tecla para continuar")


