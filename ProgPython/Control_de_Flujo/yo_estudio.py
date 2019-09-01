# -*- coding: utf-8 -*-
#yo_estudio.py
asignaturas = [
    {"catedra":"Matemática", "nota": 18},
    {"catedra":"Física","nota": 16},
    {"catedra":"Química","nota": 19},
    {"catedra":"Inglés","nota": 17},
    {"catedra":"Historia","nota": 16},
    {"catedra":"Biología","nota": 18},
]
for asign in asignaturas:
    print("Yo cursé "+str(asign["catedra"])+" y obtuve "+str(asign["nota"])+ "pts.")
