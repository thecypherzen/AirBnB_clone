"""Module defining an amenity on the hbnb clone"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines a Amenity

    Attributes:
        name(:str): amenity name
    """
    def __init__(self, *args, **kwargs):
        """Initializes the Amenity class.

        Sets all attributes to empty strings
        """
        name = kwargs.pop("name", "")
        super().__init__(**kwargs)
        self.name = name
