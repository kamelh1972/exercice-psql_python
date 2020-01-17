import os
import psycopg2
from model.connection import *
from view.model_user import *
from view.model_view import *


if __name__ == '__main__':
    show = View()
    show1 = Model_User()
    user_choice = ""

    while user_choice != "q":
        user_choice = input("tapez (a) pour acceder a votre compte ou (b) pour creer un compte ,q:")
        if user_choice == "b":
            show.to_create_account()
        if user_choice == "a":
            show1.checkout()
        if user_choice == "q":
            print("a bientot")
            exit()
