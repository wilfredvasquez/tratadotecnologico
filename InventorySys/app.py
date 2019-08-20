import time
from template import TextTemplate

def main(template):
    template.main_menu()
    opcion_main = input()
    if opcion_main == "1":
        template.first_menu()
    elif opcion_main == "2":
        template.second_menu()
    elif opcion_main == "3":
        template.third_menu()
    else:
        print("\n Opcion incorrecta. Intente de nuevo")
        time.sleep(2)
        main(template)

template = TextTemplate("Diego Shop")
template.welcome()
main(template)