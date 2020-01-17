from model.connection import *

class Model_User():

    def __init__(self):
        self.conn = connection()
        self.pseudo = None
        self.password = None

    def checkout(self):
        kamel = False
        self.pseudo = input("quel est votre pseudo")
        self.password = input("quel est votre mot de passe")
        self.conn.initialize_connection()
        self.conn.cursor.execute("SELECT pseudo, password FROM users WHERE pseudo = %s AND password= %s;",(self.pseudo,self.password))
        raws = self.conn.cursor.fetchall()
        for raw in raws:
            if raw[0] == self.pseudo and raw[1] == self.password:
                kamel= True
                return raws
                break
        self.conn.close_connection()
        return kamel

    def show_account(self):
        pass
