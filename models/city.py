"""Module defining a city on the hbnb clone"""


from models.base_model import BaseModel


class City(BaseModel):
    """Defines a City

    Attributes:
        state_id(:str): state's id
        name(:str): city name
    """
    def __init__(self, *args, **kwargs):
        """Initializes the City class.

        Sets all attributes empty strings
        """
        state_id = kwargs.pop("state_id", "")
        name = kwargs.pop("name", "")
        super().__init__(**kwargs)
        self.state_id = state_id
        self.name = name
