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
    def __init__(self, *args, **kwargs):
        """Initializes the User class.

        Sets all attributes empty strings
        """
        email = kwargs.pop("email", "")
        password = kwargs.pop("password", "")
        first_name = kwargs.pop("first_name", "")
        last_name = kwargs.pop("last_name", "")

        super().__init__(**kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
