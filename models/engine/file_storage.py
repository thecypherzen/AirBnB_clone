"""A module where file storage class is defined
"""

class FileStorage:
    """The hbnb filestorage handler

    It handles serialization of objects into json strings as well as the\
	the deserialization of the json strings to thier respective object.\
    It also takes care of persisting these objects to file, therefore\
	abstracting this layer of operation.

    Attributes:
    	__file_path(var:str): path to the JSON file; acts as local storage
    	--objects(var:dict): stores all objects by <class name>.id, eg.\
    		to store a 'BaseModel' object with 'id=1212', the key \
		will be BaseModel.1212
    	all(method): returns the dictionary __objects
	new(method): sets a new obj in __objects with key <obj class name>.id
    	save(method): serializes __objects to the JSON file (path: __file_path)
	reload(method): deserializes the JSON file to __objects \
		(iff the JSON file exists; otherwise, do nothing. \
		If the file doesn’t exist, no exception is raised)
    """
    __file_path = ".hbnb_storage.json"
    __objects = {}

    def all(cls):
        """Class method that returns all objects in the FileStorage class"""
        return cls.__objects

    def
