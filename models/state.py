"""Module defining a state on the hbnb clone"""


from models.base_model import BaseModel


class State(BaseModel):
    """Defines a State

    Attributes:
        name(:str): name of state
    """
    def __init__(self, *args, **kwargs):
        """Initializes the State class.

        Sets name to empty string at initialization
        """
        name = kwargs.pop("name", "")
        super().__init__(**kwargs)
        self.name = name
