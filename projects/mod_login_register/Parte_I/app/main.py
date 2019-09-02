# -*- coding: utf-8 -*-
import time
from menu import MenuTemplate


def main():
    menu = MenuTemplate()
    opcion = menu.main_menu()

    if opcion == "1":
        data = menu.register()
        print("Los datos de registro son: ")
        print(data)
    elif opcion == "2":
     	data = menu.login()
     	print("Los datos de ingreso son: ")
     	print(data)
    elif opcion == "3":
        menu.exit_text()
        time.sleep(2)
        menu.clean_screen()
    else: 
        print("\n Opción incorrecta. Intente de nuevo")
        time.sleep(2)
        main()

main()