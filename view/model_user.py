import psycopg2
from model.connection import *


class User():
    def __init__(self):
        self.choice = None
        self.choice = connection()

    def existant(self,pseudo,password):
        kamel = False
        self.choice.initialize_connection()
        self.choice.cursor.execute("SELECT pseudo,password FROM users;")
        raws = self.choice.cursor.fetchall()
        for raw in raws:
            if raw[0] == pseudo and raw[1] == pseudo:
                kamel= True
                break

        self.choice.close_connection()
        return kamel
