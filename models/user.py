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
        """Initializes the User class.

        Sets all attributes empty strings
        """
        k_email = kwargs.pop("email", "")
        k_password = kwargs.pop("password", "")
        k_first_name = kwargs.pop("first_name", "")
        k_last_name = kwargs.pop("last_name", "")

        super().__init__(**kwargs)
        User.email = k_email
        User.password = k_password
        User.first_name = k_first_name
        User.last_name = k_last_name
