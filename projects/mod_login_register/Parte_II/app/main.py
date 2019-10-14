# -*- coding: utf-8 -*-
import time
import bcrypt
from menu import MenuTemplate
from db_conection import MySQLConection

def main():
    menu = MenuTemplate()
    opcion = menu.main_menu()
    mysql_db = MySQLConection()

    if opcion == "1":
        ''' Sección para el registro de usuario '''
        data = menu.register()
        
        if "username" in data:
            if mysql_db.find_user_by_username(data["username"]):
                print(f'Este username: <{data["username"]}> ya se encuentra registrado.')
            elif mysql_db.find_user_by_email(data["email"]):
                print(f'Este Email: <{data["email"]}> ya se encuentra registrado.')
            else:
                password_hashed = bcrypt.hashpw(
                    data["password1"].encode('utf8'), 
                    bcrypt.gensalt()
                )
                
                new_user = mysql_db.create_user(
                    data["username"],
                    data["email"],
                    password_hashed
                )
                
                if new_user:
                    print ("Se ha registrado en el sistema.")
                else:
                    print ("Ha ocurrido un error en la base de datos.")
        else:
            print(f"\n{data}")

        input("\nPresione una tecla para continuar...")
        main()

    elif opcion == "2":
        ''' Sección para el login de usuario '''
        data = menu.login()

        result = mysql_db.find_user_by_username(data["username"])
        if result:
            if not bcrypt.checkpw(data["password"].encode('utf8'), result[2].encode('utf8')):
                print("Username o password inválido.")
            else:
                print("Usted ha ingresado al sistema.")
        else:
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