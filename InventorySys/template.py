import os

class TextTemplate():
    def __init__(self,
                 business_name = "Tratado Tecnologico"):
        self.business_name = business_name
        self.clean = "clear" if os.name == "posix" else "cls"
    
    def head(self):
        print("\t-------------------------------------------------------")
        print("\tSistema de Inventario de {}".format(self.business_name))
        print("\t-------------------------------------------------------")

    def welcome(self):
        os.system(self.clean)
        print("\t \t \t Bienvenidos al")
        self.head()
        print("\n")
        print("Presione cualquier tecla para continuar")
        input()

    def main_menu(self):
        os.system(self.clean)	
        self.head()
        print("1.- Mostrar el inventario de productos")
        print("2.- Buscar un producto")
        print("3.- Agregar nuevos productos")
        print("Seleccione una opción -->")

    def first_menu(self):
        os.system(self.clean)	
        self.head()
        print("1.- Mostrar el inventario de productos")
        print("Seleccione una opción -->")

    def second_menu(self):
        os.system(self.clean)	
        self.head()
        print("2.- Buscar un producto")
        print("Seleccione una opción -->")

    def third_menu(self):
        os.system(self.clean)	
        self.head()
        print("1.- Mostrar el inventario de productos")
        print("2.- Buscar un producto")
        print("3.- Agregar nuevos productos")
        print("Seleccione una opción -->")

    def select_template(menu):
        if menu="welcome":
            welcome()
        elif menu="menu":
            main_menu()
        elif menu="first":
            first_menu()
        elif menu="second":
            second_menu()
        elif menu="third":
            third_menu()
        else:
        	error()