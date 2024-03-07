"""BaseModel of all hbnb models

Is the base class from which all other hbnb models inherit.

Classes:
	BaseModel
"""

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
        from uuid import uuid4 as idgen
        import datetime as dt

        self.id = str(idgen())
        self.created_at = dt.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Creates a 
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"
