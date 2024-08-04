"""A module where file storage class is defined
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os
import json


class FileStorage:
    """The hbnb filestorage handler

    It handles serialization of objects into json strings as well as the
        the deserialization of the json strings to thier respective object.
    It also takes care of persisting these objects to file, therefore
        abstracting this layer of operation.

    Attributes:
        __file_path(var:str): path to the JSON file; acts as local storage
        __objects(var:dict): stores all objects by <class name>.id, eg.
                to store a 'BaseModel' object with 'id=1212', the key
                will be BaseModel.1212
        all(method): returns the dictionary __objects
        new(method): sets a new obj in __objects with key <obj class name>.id
        save(method): serializes __objects to the JSON file (path: __file_path)
        reload(method): deserializes the JSON file to __objects
                (if the JSON file exists; otherwise, do nothing.
                If the file doesn’t exist, no exception is raised)

    """
    folder = os.path.dirname(os.path.abspath(__file__))
    __classes = {"BaseModel": BaseModel, "User": User}
    __file_path = f"{folder}/.hbnb_storage.json"
    __objects = {}

    def all(self, class_name=None):
        """Class method that returns all objects in FileStorage that match
        class_obj or all objects in FileStorage if class_obj is None
        """
        if not class_name:
            return self.__objects

        all_objs = {}
        for key, obj in self.__objects.items():
            if obj.__class__.__name__ == class_name:
                all_objs[key] = obj
        return all_objs

    def destroy(self, obj):
        """ deletes an object from storage objects """
        for key in self.__objects:
            if self.__objects[key] == obj:
                del self.__objects[key]
                break

    def new(self, obj):
        """Changes content of __objects dict

        In the __objects dictionary, it changes or sets the value of the key
                '<object_name.id>.id' to 'obj' accordingly.
        Return:
                None
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def reload(self):
        """JSON deserializer of storage objects

        Converts(deserializes) a JSON file in '--file_path' into objects
                and stores them in the '__objects' dict.
            * if the path to JSON file doesn't exist, it does nothing.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)

            for key, model in self.__objects.items():
                class_name = key.split('.')[0]
                self.__objects[key] = self.__classes[class_name](**model)

    def save(self):
        """Saves all objects to file

        Serializes '__objects' and saves in '__file_path'
        Returns:
                None
        """
        __objects_copy = {}
        for key, obj in self.__objects.items():
            __objects_copy[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(__objects_copy, file, indent=4)
