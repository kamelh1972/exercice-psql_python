
from view.model_user import *


class View():

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
                print(kamel)
        self.conn.close_connection()
        return kamel

    def view_profll(self):
        profil = []
        self.pseudo = None
        self.conn.initialize_connection()
        self.conn.cursor.execute("SELECT * FROM users WHERE pseudo = %s;",(self.pseudo))
        raws = self.conn.cursor.fetchall()
        for raw in raws:
            if raw[0] == self.pseudo:
                profil = profil.append()
                print(profil)
        self.conn.close_connection()
        return profil
