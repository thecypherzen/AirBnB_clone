#!/usr/bin/python3
"""
This is a program that contains the entry point of the command interpreter
"""
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import system
import re


class HBNBCommand(cmd.Cmd):
    """ This is a class that defines the command interpreter """
    prompt = "(hbnb) "
    __classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                 "Place": Place, "Review": Review, "State": State,
                 "User": User}

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the program """
        print()
        return True

    def emptyline(self):
        """
            This function is called when the user\
            passes and emptyline to the console
        """
        pass

    def do_create(self, line):
        """
            Creates a new instance of BaseModel and
            saves it (to the JSON file) and prints the id.
            Ex: $ create BaseModel
        """
        if line == "":
            print("** class name missing **")
        elif line not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = self.__classes[line]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """
            Prints the string representation of an instance
            based on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234
        """
        input_args = line.split(" ")
        if self._validate(input_args):
            instance = self._get_instance(input_args[1], input_args[0])
            if instance:
                print(instance)

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file)
            Ex: $ destroy BaseModel 1234-1234-1234
        """
        input_args = line.split()
        if self._validate(input_args):
            instance = self._get_instance(input_args[1], input_args[0])
            if instance:
                storage.destroy(instance)
                storage.save()

    def do_all(self, model_name):
        """
            Prints all string representation of all instance\
            based or not on the class name.
            Ex: $ all BaseModel or $ all
        """
        if model_name:
            if model_name not in self.__classes:
                print("** class doesn't exist **")
                return
            else:
                all_models = storage.all(model_name)
        else:
            all_models = storage.all()
        models_list = [str(model) for model in all_models.values()]
        print(models_list)

    def do_update(self, line):
        """
            Updates an instance based on the class name and id by
            adding or updating attribute, and save the change into the
            JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com
        """
        input_args = line.split()
        if not self._validate(input_args):
            return
        input_len = len(input_args)
        if input_len < 4:
            if input_len == 2:
                print("** attribute name missing **")
            else:
                print("** value missing **")
            return
        instance = self._get_instance(input_args[1], input_args[0])
        if input_args[2] not in ["id", "created_at", "updated_at"]:
            if input_args[3][0] == input_args[3][-1] == '"':
                value = input_args[3][1:-1]
            else:
                value = input_args[3]
            setattr(instance, input_args[2], value)
            instance.save()

    def do_clear(self, line):
        """ Clears the screen of the console """
        system('clear')

    def _validate(self, input_args):
        """checks if class_name exists and obj_id are passed"""
        arg_len = len(input_args)
        if arg_len == 0:
            print("** class name missing **")
        elif input_args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif arg_len == 1:
            print("** instance id missing **")
        else:
            return True
        return False

    def _get_instance(self, obj_id, obj_name=None):
        instance = None
        all_objs = storage.all(obj_name).values()
        for obj in all_objs:
            if obj.id == obj_id:
                instance = obj
                break
        if not instance:
            print("** no instance found **")
        return instance

    def default(self, line):
        """Gets all instances of model by model_name"""
        regex = r'^[A-Za-z]+\.[a-z]+\(.*\)$'
        match = re.search(regex, line)
        if match:
            regex = r'[\.\(\)]'
            input = [val for val in re.split(regex, line) if val]
            if input[0] not in self.__classes:
                print("** class doesn't exist **")
                return
            if input[1] == "all":
                self.do_all(input[0])
            elif input[1] == "count":
                print(len(storage.all(input[0]).values()))
            else:
                i_len = len(input)
                if i_len < 3:
                    print("** instance id missing **")
                    return
                if input[1] == "show":
                    instance = self._get_instance(input[2], input[0])
                    print(instance)
        else:
            print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
