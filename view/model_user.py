import psycopg2
from model.connection import *

class User():
    def __init__(self):
        self.choice = None
        self.choice = connection()

    def checkout(self,pseudo,password):
        kamel = False
        self.pseudo = input("quel est votre pseudo")
        self.password = input("quel est votre mot de passe")
        self.choice.initialize_connection()
        self.choice.cursor.execute("SELECT pseudo,password FROM users;")
        raws = self.choice.cursor.fetchall()
        for raw in raws:
            if raw[0] == pseudo and raw[1] == password:
                kamel= True
                break
        self.choice.close_connection()
        return kamel


    def create_account(self,name, firstname,pseudo,email,age,password):
        self.name = input("veuillez renseignez votre name")
        self.firstname = input("your firstname")
        self.pseudo = None
        self.email =input("your email")
        self.age =input(int(age))
        self.password = None
        self.choice.initialize_connection()
        self.choice.cursor.execute("INSERT INTO users(name,firstname,pseudo,email,age,password)VALUES(%s, %s, %s, %s, %s, %s);")
        self.choice.connection.commit()
        self.choice.close_connection()
