from view.model_user import *

class View():
    """class  """
    def __init__(self):
        self.model = User()
    def show_account(self,pseudo,password):
        """display all messages """
        # get the messages from the model
        name = self.model.existant(pseudo,password)
        print("")
        if name:
            for name in users:


)
