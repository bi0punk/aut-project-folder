import os
from prettytable import PrettyTable
from colorama import Fore, Back, Style
import platform



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


my_os = platform.system()


if my_os == 'Linux':
    aa = 'Sistema Linux......Version'


wd = os.getcwd()
""" print("working directory is ", wd) """

filePath = __file__
""" print("This script file path is ", filePath) """

absFilePath = os.path.abspath(__file__)
""" print("This script absolute path is ", absFilePath) """

path, filename = os.path.split(absFilePath)
""" print("Script file path is {}, filename is {}".format(path, filename)) """

x = PrettyTable()
def menu():


    print(bcolors.HEADER + "\t#############################################################################################" + bcolors.ENDC)
    wd = os.getcwd()
    print(bcolors.HEADER + "\t#" +  bcolors.ENDC)
    print(bcolors.HEADER + "\t#" +  bcolors.ENDC)
    print(bcolors.HEADER + "\t#" +  bcolors.ENDC)
    """ print(bcolors.OKGREEN + "Warning: No active frommets remain. Continue?" + bcolors.ENDC) """
    print(bcolors.HEADER + "\t#" +  bcolors.ENDC + bcolors.OKGREEN +  "\tSistema operativo detectado: " + bcolors.OKBLUE + str(my_os))
    print(bcolors.HEADER + "\t#" +  bcolors.ENDC + bcolors.OKGREEN + "\tEntorno de Trabajo : " + bcolors.ENDC + bcolors.WARNING  + " {}".format(path))
    print(bcolors.HEADER + "\t#" +  bcolors.ENDC)
    print(bcolors.HEADER + "\t#" +  bcolors.ENDC)
    print("\t#")
    print("\t#")
    print("\t#" + bcolors.WARNING  + "   1.- " + bcolors.ENDC +  bcolors.OKBLUE + "Simple Python Script" + bcolors.ENDC) 
    print("\t#" + bcolors.WARNING  + "   2.- " + bcolors.ENDC +  bcolors.OKBLUE +"Simple Empty Flask Application")
    print("\t#" + bcolors.WARNING  + "   3.- " + bcolors.ENDC +  bcolors.OKBLUE +"Simple Empty Flask Application with Virtual Environment (venv)")
    print("\t#" + bcolors.WARNING  + "   4.- " + bcolors.ENDC +  bcolors.OKBLUE +"Flask Aplication with V/e + Bootstrap v4/v5")
    print("\t#" + bcolors.WARNING  + "   5.- " + bcolors.ENDC +  "Flask Aplication with V/e + Bootstrap v4/v5 + Login Module and Templates (Basic)")
    print("\t#" + bcolors.WARNING  + "   6.- " + bcolors.ENDC +  "Flask Aplication with V/e + Bootstrap v4/v5 + Login Module and Templates (Login + Sidebar and/or Navbar)")
    print("\t#" + bcolors.WARNING  + "   7.- " + bcolors.ENDC +  "Salir")
    print("\t#")
    print("\t#")
    print("\t#")


def simple_script():
    print("\tCreacíon de estructura de proyecto para script siemple")
    __project_name__ = input("Ingrese el nombre del proyecto: ")
    print("\tEl nombre del proyecto es " +str(__project_name__) )
    print("\tIngrese la ruta en cual decea crear el proyecto \ si decea mantener esta ruta presione 'Y' ")



while(True):
    menu()
    opcionMenu = input("\n Opción >>>>>: ")
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


""" print(bcolors.HEADER + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(bcolors.OKBLUE + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(bcolors.OKCYAN + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(bcolors.OKGREEN + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(bcolors.FAIL + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(bcolors.ENDC + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(bcolors.BOLD + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(bcolors.UNDERLINE + "Warning: No active frommets remain. Continue?" + bcolors.ENDC) """

""" print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}") """