# -*- coding: utf-8 -*-
import time
import bcrypt
from menu import MenuTemplate

username = []
email = []
password = []

def main():
    menu = MenuTemplate()
    opcion = menu.main_menu()

    if opcion == "1":
        ''' Sección para el registro de usuario '''
        data = menu.register()
        
        if "username" in data:
            if data["username"] in username:
                print(f'Este username: <{data["username"]}> ya se encuentra registrado.')
            elif data["email"] in email:
                print(f'Este Email: <{data["email"]}> ya se encuentra registrado.')
            else:
                password_hashed = bcrypt.hashpw(
                    data["password1"].encode('utf8'), 
                    bcrypt.gensalt()
                )
                
                username.append(data["username"])
                email.append(data["email"])
                password.append(password_hashed)

                print ("Se ha registrado en el sistema.")
        else:
            print(f"\n{data}")

        input("\nPresione una tecla para continuar...")
        main()

    elif opcion == "2":
        ''' Sección para el login de usuario '''
        data = menu.login()
        index = 0
        try:
            index = username.index(data['username'])
            
            password_hashed = password[index]
            if not bcrypt.checkpw(data["password"].encode('utf8'), password_hashed):
                print("Username o password inválido.")
            else:
                print("Se ha autenticado de forma correcta.")

        except ValueError as e:
            print("Username o password inválido.")

        input("\nPresione una tecla para continuar...")
        main()

    elif opcion == "3":
        ''' Sección para salir del sistema'''
        menu.exit_text()
        time.sleep(2)
        menu.clean_screen()

    else:
        ''' En caso de no coincidir la opciones anteriores '''
        print("\n Opción incorrecta. Intente de nuevo")
        time.sleep(2)
        main()

main()