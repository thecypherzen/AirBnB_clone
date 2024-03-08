"""BaseModel of all hbnb models

Is the base class from which all other hbnb models inherit.

Classes:
	BaseModel
"""
from uuid import uuid4 as idgen
from datetime import datetime as dt

class BaseModel:
    """The base class from which all hbnb models inherit

    Variables:
    	id(:str:pub): uuid of class instance when it's created
    	created_at(:datetime:pub): datetime when instance is created
    	updated_at(:datetime:pub): datetime when instance is modified

    Methods:
	__str__(:prv): prints: str rep of class instance
	save(:pub): updates the value of the public instance attribute \
		'updated_at with the current datetime
	to_dict(:pub): returns a dictionary of keys/vaues of instance
    """


    def __init__(self):
        """Initializes the BaseModel instance

        It sets the values of all attributes.

        Attributes:
        	id(:pub): the uuid of instance
	        created_at(:pub): datetime of instance creation
        	updated_at(:pub): datetime of instance modification time

        Returns:
        	None
        """
        self.id = str(idgen())
        self.created_at = dt.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Creates a strig of the class object

        Attributes: None
        Returns: string representing the class in this format:
        	[<class name>] (<self.id>) <self.__dict__>
        """

        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = dt.now()



my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model, end='\n\n')
my_model.save()
print(my_model)
