# -*- coding: utf-8 -*-
#juego_de_adivinanza.py
numero_adivinar = 55
intentos = 3
while True:
    num = int(input("Intente adivinar el número: "))
    if num == numero_adivinar:
        print("¡Felicitaciones lo ha logrado!")
        break
    elif num > numero_adivinar:
        print("Error: Este número es mayor al que debe adivinar")
    else:
        print("Error: Este número es menor al que debe adivinar")
    intentos = intentos - 1
    if intentos == 0:
        print("Ha usado todos sus intentos. Mejor suerte a la próxima")
        break
