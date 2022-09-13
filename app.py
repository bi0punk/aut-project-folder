from consolemenu import *
from consolemenu.items import *

# Create the menu
# Crea el menú
menu = ConsoleMenu("Automatic Project Folder Creator", "Automatic creation of project structure dir")

# Create some items
# Crear algunos elementos


# MenuItem es la clase base para todos los elementos, no hace nada cuando se selecciona
menu_item = MenuItem("Menu Item")


# Un elemento de función ejecuta una función de Python cuando se selecciona
function_item = FunctionItem("Call a Python function", input, ["Enter an input"])


# Un CommandItem ejecuta un comando de consola
command_item = CommandItem("Run a console command",  "touch hello.txt")


# Un SelectionMenu construye un menú a partir de una lista de cadenas
selection_menu = SelectionMenu(["item1", "item2", "item3"])


# Un SubmenuItem le permite agregar un menú (el menú de selección anterior, por ejemplo)
# como submenú de otro menú
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)
# Una vez que hayamos terminado de crearlos, solo agregamos los elementos al menú
menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
# Finalmente, llamamos show para mostrar el menú y permitir que el usuario interactúe
menu.show()