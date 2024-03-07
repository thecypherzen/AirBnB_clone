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
	save(:pub): updates the public instance attribute's 'updated_at' \
		value with the current datetime
	to_dict(:pub): returns a dictionary of keys/vaues of instance
    """
    from uuid import uuid4 as idgen


    def __get_time__(offset=0):
        """Gets an aware time from a naive one

        Attributes:
		offset(:int): UTC offset
        Returns:
        	Aware time from datetime.now()
        """
        from datetime import datetime, timedelta, timezone

        time_now = datetime.now()
        delta = timedelta(hours=offset)
        time_now = time_now.astimezone(timezone(delta))
        return time_now

    id = str(idgen())
    created_at = __get_time__()
    updated_at = created_at


