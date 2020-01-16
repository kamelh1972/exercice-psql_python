import psycopg2
from view.model_user import User


class View():
    """class  """
    def __init__(self):
        self.model = User()



    def show_account(self,pseudo,password):
        self.pseudo = None
        self.password = None
        user = self.model.checkout(pseudo,password)
        pass
