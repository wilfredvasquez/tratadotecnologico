# -*- coding: utf-8 -*-
def pasar_mayuscula(texto):
    return texto.upper()

def pasar_minuscula(texto):
    return texto.lower()

t = input("Ingrese el texto a formatear: ")
t_may = pasar_mayuscula(t)
print("El texto en mayúscula es: "+t_may)
t_min = pasar_minuscula(t)
print("El texto en minúscula es: "+t_min)