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


class HBNBCommand(cmd.Cmd):
    """ This is a class that defines the command interpreter """
    prompt = "(hbnb) "
    __classes = {"BaseModel": BaseModel}

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
            Prints the string representation of an instance\
            based on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234 """
        instance = self.do_check(line)
        if instance:
            print(instance)

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file)
            Ex: $ destroy BaseModel 1234-1234-1234
        """
        instance = self.do_check(line)
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
        instance = self.do_check(line)
        if not instance:
            return
        input = line.split()
        input_len = len(input)
        if input_len < 4:
            if input_len == 2:
                print("** attribute name missing **")
            else:
                print("** value missing **")
            return
        if input[2] not in ["id", "created_at", "updated_at"]:
            if input[3][0] == input[3][-1] == '"':
                value = input[3][1:-1]
            else:
                value = input[3]
            setattr(instance, input[2], value)
            instance.save()

    def do_clear(self, line):
        """ Clears the screen of the console """
        system('clear')

    def do_check(self, line):
        """checks if class_name exists or obj_id matches for instance"""
        instance = None
        input = line.split()
        arg_len = len(input)
        if arg_len == 0:
            print("** class name missing **")
        elif input[0] not in self.__classes:
            print("** class doesn't exist **")
        elif arg_len == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all().values()
            for obj in all_objs:
                if obj.id == input[1]:
                    instance = obj
                    break
            if instance is None:
                print("** no instance found **")
        return instance


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        # Implementation of non interactive mode
        HBNBCommand().onecmd(''.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
