from simple_term_menu import TerminalMenu

def main():
    options = ["1.- Simple Python Project", "2.- Simple Python Project w/ virtual env", "3.- Flask Project with virtual env", "4.- Flask Project with virtual env and Boostrap 4/5"]
    terminal_menu = TerminalMenu(options)
    print("-----------------------------------------------------")
    print("|                                                    |")
    print("|                                                    |")
    print("|      Python Project Automated Folder Creator       |")
    print("|                                                    |")
    print("|                                                    |")
    print("-----------------------------------------------------")
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

if __name__ == "__main__":
    main()
