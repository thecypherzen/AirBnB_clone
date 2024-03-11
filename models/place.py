"""Module defining a Place on the hbnb clone"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Defines a Place.

    Inherits from the BaseModel parent class

    Attributes:
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
    def __init__(self, *args, **kwargs):
        """Initializes the Place class.

        Sets all attributes empty or null values
        """
        city_id = kwargs.pop("city_id", "")
        user_id = kwargs.pop("user_id", "")
        description = kwargs.pop("description", "")
        number_rooms = kwargs.pop("number_rooms", 0)
        number_bathrooms = kwargs.pop("number_bathrooms", 0)
        max_guest = kwargs.pop("max_guest", 0)
        price_by_night = kwargs.pop("price_by_night", 0)
        latitude = kwargs.pop("latitude", 0.0)
        longitude = kwargs.pop("longitude", 0.0)
        amenity_ids = kwargs.pop("amenity_ids", [])

        super().__init__(**kwargs)
        self.city_id = city_id
        self.user_id = user_id
        self.description = description
        self.number_rooms = number_rooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids
