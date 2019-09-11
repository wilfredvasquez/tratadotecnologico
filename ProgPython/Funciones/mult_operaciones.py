# -*- coding: utf-8 -*-
def operacion(num1, num2, oper = 'suma'):
    if oper.lower() == "suma":
        return num1 + num2
    elif oper.lower() == "resta":
        return num1 - num2
    elif oper.lower() == "division":
        return num1 / num2
    elif oper.lower() == "multiplicacion":
        return num1 * num2
    else:
        return "Operación inválida"

oper = input("Qué desea hacer: suma, resta, division o multiplicacion: ")
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
result = operacion(n1, n2, oper)
print(result)