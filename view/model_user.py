from model.connection import *




class User():
    """class  """
    def __init__(self):
        self.conn = connection()
        self.name = None
        self.firstname = None
        self.pseudo = None
        self.email = None
        self.age = None
        self.password = None

    def checkout(self):

        self.conn.initialize_connection()
        self.conn.cursor.execute("SELECT pseudo, password FROM users WHERE pseudo = %s AND password= %s;"(pseudo,password,))
        result = self.conn.cursor.fetchall()
        self.conn.close_connection()
        return result

    def to_create_account(self):
        self.name = input("veuillez renseignez votre name")
        self.firstname = input("your firstname")
        self.pseudo =input("tapez votre pseudo")
        self.email =input("your email")
        self.age =int(input("quel est votre age"))
        self.password = input("tapez votre password")
        self.conn.initialize_connection()
        self.conn.cursor.execute("INSERT INTO users(name,firstname,pseudo,email,age,password)VALUES(%s,%s,%s,%s,%s,%s);",(self.name,self.firstname,self.pseudo,self.email,self.age,self.password))
        self.conn.connection.commit()
        self.conn.close_connection()
