import sqlite3

class SQLiteConection():
# Conexión con la Base de Datos
    def connect(self):
        self.con = sqlite3.connect('../LoginDB.db')
        self.cur = self.con.cursor()

    def create_user(self, username, email, password):
        self.connect()
        self.cur.execute(
        	'INSERT INTO users (username, email, password) VALUES (?, ?, ?);',
            (username, email, password)
        )
        result = self.cur.lastrowid
        self.con.commit()
        self.con.close()
        return result

    def find_user_by_username(self, username):
        self.connect()
        self.cur.execute('SELECT * FROM users WHERE username = "{}"'.format(username))
        result = self.cur.fetchone()
        self.con.close()
        return result

    def find_user_by_email(self, email):
        self.connect()
        self.cur.execute('SELECT * FROM users WHERE email = "{}"'.format(email))
        result = self.cur.fetchone()
        self.con.close()
        return result