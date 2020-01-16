import os
import psycopg2
from model.connection import *
from view.model_user import *
from view.model_view import *


if __name__ == '__main__':
    show = User()
    show.checkout()
    user_choice = ""
    while user_choice !="q":
        user_choice = input("tapez (a) pour acceder a votre compte ou (b) pour creer un compte:")
        choice = User()

    if user_choice == "a":
        show.checkout()
        user_choice = input("tapez (a) pour acceder a votre compte ou (b) pour creer un compte:")
        pass
