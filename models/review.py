"""Module defining a Review on the hbnb clone"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a Review

    Attributes:
        place_id(:str): the place's id. Inits empty
        user_id(:str): user's name. Inits empty
        text(:str): review text. Inits to empty
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes the Review class."""
        super().__init__(**kwargs)
