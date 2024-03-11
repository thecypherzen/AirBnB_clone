"""Module defining a Review on the hbnb clone"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a Review

    Attributes:
        place_id(:str): the place's id. Inits empty
        user_id(:str): user's name. Inits empty
    	text(:str): review text. Inits to empty
    """
    def __init__(self, *args, **kwargs):
        """Initializes the Review class.

        Sets all attributes empty strings
        """
        print("...Initializing Review...")
        place_id = kwargs.pop("place_id", "")
        user_id = kwargs.pop("user_id", "")
        text = kwargs.pop("text", "")

        super().__init__(**kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
