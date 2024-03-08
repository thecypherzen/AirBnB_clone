"""BaseModel of all hbnb models

Is the base class from which all other hbnb models inherit.

Classes:
	BaseModel
"""
from uuid import uuid4 as idgen
from datetime import datetime as dt

class BaseModel:
    """The base class from which all hbnb models inherit

    Methods:
    	__init__(:prv): instantiates the class
	__str__(:prv): prints: str rep of class instance
	save(:pub): updates the value of the public instance attribute \
		'updated_at with the current datetime
	to_dict(:pub): returns a dictionary of keys/vaues of instance
    """


    def __init__(self):
        """Initializes the BaseModel instance

        It sets the values of all attributes.

        Attributes:
        	id(:str:pub): uuid of class instance when it's created
        	created_at(:datetime:pub): datetime when instance is created
	    	updated_at(:datetime:pub): datetime when instance is modified

        Returns:
        	None
        """
        self.id = str(idgen())
        self.created_at = str(dt.now())
        self.updated_at = self.created_at

    def __str__(self):
        """Creates a strig of the class object

        Attributes: None
        Returns: string representing the class in this format:
        	[<class name>] (<self.id>) <self.__dict__>
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates class's 'updated_at' to current datetime"""
        self.updated_at = dt.now()

    def to_dict(self):
        """Returns a dictionary of class's __dict__

        It's the first piece of the serialization/deserialization process:\
		creating a dictionary representation of 'BaseModel'

        Notes:
        	* A key '__class__' must be added to the dictionary with the \
		class name of the object
        	* Values of 'created_at' and 'updated_at' are converted \
			to ISO format: %Y-%m-%dT%H:%M:%S.%f \
			(ex: 2017-06-14T22:31:03.285259)
        """
        temp = self.__dict__
        temp['__class__'] = self.__class__.__name__
        return temp
