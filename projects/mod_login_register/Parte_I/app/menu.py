# -*- coding: utf-8 -*-
import os

class MenuTemplate():
    def __init__(self,
                 title = "Tratado Tecnologico"):
        self.title = title
        self.clean = "clear" if os.name == "posix" else "cls"
    
    def clean_screen(self):
        os.system(self.clean)

    def head(self):
        print("\t-------------------------------------------------------")
        print("\t\t\t{}".format(self.title))
        print("\t Bienvenido al Módulo de Lógin y Registro de Usuarios")
        print("\t-------------------------------------------------------")
 
    def main_menu(self):
        self.clean_screen()
        self.head()
        print("1.- Registrar")
        print("2.- Logear")
        print("3.- Salir")
        opcion = input("Seleccione una opción --> ")
        return opcion

    def register(self):
        self.clean_screen()
        self.head()
        username = input("Ingrese username: ")
        email = input("Ingrese email: ")
        password1 = input("Ingrese password: ")
        password2 = input("Repita el password: ")
        return {
            "username": username,
            "email": email,
            "password1": password1,
            "password2": password2,
        }

    def login(self):
        self.clean_screen()
        self.head()
        username = input("Ingrese username: ")
        password = input("Ingrese password: ")
        return {
            "username": username,
            "password": password,
        }

    def exit_text(self):
        self.clean_screen() 
        self.head()
        print("\n")
        print("Gracias por usar nuestro sistema")