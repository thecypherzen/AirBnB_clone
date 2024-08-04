"""Module defining a state on the hbnb clone"""


from models.base_model import BaseModel


class State(BaseModel):
    """Defines a State

    Attributes:
        name(:str:publc): name of state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the State class. """
        super().__init__(**kwargs)
