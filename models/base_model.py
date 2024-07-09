"""BaseModel of all hbnb models

Is the base class from which all other hbnb models inherit.

Classes:
        BaseModel
"""
from datetime import datetime as dt, timedelta as td
from uuid import uuid4 as idgen
from models import storage


class BaseModel:
    """The base class from which all hbnb models inherit

    Methods:
        __init__(:prv): instantiates the class
        __str__(:prv): prints: str rep of class instance
        save(:pub): updates the value of the public instance attribute \
                'updated_at' with the current datetime
        to_dict(:pub): returns a dictionary of keys/values of instance
    """
    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel instance

        It sets the values of all attributes.
                - If kwargs is passed, new instance is created from its values
                - Else, instance is created from scratch

        Args:
                args(:obj:tup): tuple of all unamed args
                kwargs(:obj:dict): dict of all named args

        Attributes:
                id(:str:pub): uuid of class instance when it's created
                created_at(:datetime:pub): datetime when instance is created
                updated_at(:datetime:pub): datetime when instance is modified

        Returns:
                None
        """
        if kwargs:
            keys = kwargs.keys()
            if "id" in keys:
                self.id = kwargs['id']
            else:
                self.id = str(idgen())

            if "created_at" in keys:
                self.created_at = dt.fromisoformat(kwargs['created_at'])
            else:
                self.created_at = dt.now()

            if "updated_at" in keys:
                self.updated_at = dt.fromisoformat(kwargs['updated_at'])
            else:
                self.updated_at = self.created_at

            to_skip = ["id", "created_at", "updated_at", "__class__"]
            for key in kwargs.keys():
                if key not in to_skip:
                    setattr(self, key, kwargs[key])
            if "id" not in kwargs.keys():
                storage.new(self)
        else:
            self.id = str(idgen())
            self.created_at = dt.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Creates a string of the class object

        Attributes: None
        Returns: string representing the class in this format:
                [<class name>] (<self.id>) <self.__dict__>
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates class' 'updated_at' to current datetime"""

        self.updated_at = dt.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns a dictionary of class's __dict__

        It's the first piece of the serialization/deserialization process:\
                creating a dictionary representation of 'BaseModel'

        Notes:
                * A key '__class__' is added to the dictionary with the \
                class name of the object
                * Values of 'created_at' and 'updated_at' are converted \
                        to ISO format: %Y-%m-%dT%H:%M:%S.%f \
                        (ex: 2017-06-14T22:31:03.285259)
        """
        # update timestamp values
        obj_copy = self.__dict__.copy()
        obj_copy["created_at"] = obj_copy["created_at"].isoformat()
        obj_copy["updated_at"] = obj_copy["updated_at"].isoformat()
        obj_copy['__class__'] = self.__class__.__name__
        return obj_copy
