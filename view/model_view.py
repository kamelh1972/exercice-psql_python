import hashlib
import os
#from getpass import getpass
from view.model_user import *


class View():

    def __init__(self):
        self.pseudo = None
        self.password = None


    def login(self):
        model = model_user()
        self.pseudo = input("quel est votre pseudo")
        self.password = input("quel est votre mot de passe")
        user = model.checkout(pseudo,password)
        for raw in raws:
            if raw[0] == self.pseudo and raw[1] == self.password:
                self.profil(user)
            else:
                print ("vos identifiants sont incorrects")

    def profil(self, user):
        """Display information about a given user from the database
        Let the user delete or update his profile
           Afficher des informations sur un utilisateur donné à partir de la base de données
           Laisser l'utilisateur supprimer ou mettre à jour son profil"""

        # Instanciate the model to operate queries on users table
        # Instancier le modèle pour exécuter des requêtes sur la table des utilisateurs
        model = model_user()

        # Show user
        print("Bonjour voici nos informations sur vous : ")
        print(
            "nom : {}\nprénom : {}\nage : {}\npseudo : {}\nemail : {}\n"
            .format(user['name'], user['firstname'], user['age'], user['pseudo'], user['email'])
        )
        # Get action from user
        # Obtenir une action de l'utilisateur
        print("Actions possible s: supprimer son compte, m: modifier une information, tapez entrée pour revenir à l'accueil")
        pass
        #action = input(": ")
        # Call the right method based on the action
        # Appeler la bonne méthode en fonction de l'action
        #if action == "s":
            #model.delete_user(user)
        #elif action == "m":
            # Ask which column to change and the new value to set
            # Demandez quelle colonne modifier et quelle nouvelle valeur définir
            #column = input("Que voulez-vous modifier ? (name, firstname, email, age, password, pseudo) : ")
            #value = input("Nouvelle valeur : ")
            # If the user changes the password with crypt it
            # Si l'utilisateur change le mot de passe avec crypt il
            #if column == "password":
                #value = hashlib.sha256(bytes(value, encoding="ascii")).hexdigest()
            # Update the dictionnary representing the user
            # Mettre à jour le dictionnaire représentant l'utilisateur
            #user[column] = value
            # Update the database
            # Mettre à jour la base de données
            #model.update_user(user)
