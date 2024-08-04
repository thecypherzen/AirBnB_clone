"""Module defining a user on the hbnb clone"""


from models.base_model import BaseModel


class User(BaseModel):
    """Defines a User

    Attributes:
        email(:str): user's email
        password(str): user's password
        first_name(:str): user's first name
        last_name(:str): user's lastname
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the User class."""
        super().__init__(**kwargs)
