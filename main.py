import os
#import psycopg2
#from model.connection import *
from view.model_view import *
#from view.model_view import *


if __name__ == '__main__':
    show = User()
    user_choice = ""


    while user_choice != "q":
        user_choice = input("tapez (a) pour acceder a votre compte ou (b) pour creer un compte ou tapez (q)pour quitter:")
        if user_choice == "b":
            show.to_create_account()
            show = View()
            if user_choice == "a":
                show.login()
                if user_choice == "q":
                    print("a bientot")
