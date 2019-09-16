# -*- coding: utf-8 -*-
import sqlite3

#Crea el archivo de Base de Datos si no ha sido creada
conn = sqlite3.connect('LoginDB.db') 
c = conn.cursor()

# Creación de la Tabla - USER
c.execute('''
	CREATE TABLE users (
	    username text PRIMARY KEY,
	    email text NOT NULL,
	    password text NOT NULL
	 )'''
)
                 
conn.commit()