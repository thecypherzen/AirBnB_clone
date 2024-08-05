"""Module defining an amenity on the hbnb clone"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines a Amenity

    Attributes:
        name(:str:pub): amenity name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the Amenity class.

        Sets all attributes to empty strings
        """
        super().__init__(**kwargs)
