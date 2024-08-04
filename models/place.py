"""Module defining a Place on the hbnb clone"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Defines a Place.

    Inherits from the BaseModel parent class

    Public Class Attributes:
        city_id(:str): The City.id - inits to empty str
        user_id(:str): The User.id - inits to empty str
        name(:str): Place name - inits to empty string
        description(:str): Place's description - inits to empty str
        number_rooms(:int): Inits to 0
        number_bathrooms(:int): Inits to 0
        max_guest(:int): Maximum guets possible - inits to 0
        price_by_night(:int): Inits to 0
        latitude(:float): Inits to 0.0
        longitude(:float): Inits to 0.0
        amenity_ids(:list:str): List of strings of `Amenity.id`s

    """
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""

    def __init__(self, *args, **kwargs):
        """Initializes the Place class.

        Sets all attributes empty or null values
        """
        super().__init__(**kwargs)
