import pymysql

DB_HOST = "localhost"
DB_USER = "your_user"
DB_PASS = "your_password"

db = pymysql.connect(DB_HOST, DB_USER, DB_PASS)
cursor = db.cursor()
cursor.execute('CREATE DATABASE LoginDB')
cursor.execute('USE LoginDB')
cursor.execute('''
	CREATE TABLE users (
       username VARCHAR(50) PRIMARy KEY,
       email VARCHAR(50) NOT NULL,
       password VARCHAR(200) NOT NULL
       )
       '''
)