#!/usr/bin/python3
"""
This is a program that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ This is a class that defines the command interpreter """
    prompt = "(hbnb) "
    classes = ["BaseModel", "Amenity", "City", "Place",
               "Review", "State", "User"]

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the program """
        print()
        return True

    def emptyline(self):
        """ This function is called when the user\
            passes and emptyline to the console """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel,\
            saves it (to the JSON file) and prints the id.
            Ex: $ create BaseModel """
        if line == "":
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            basemodel = BaseModel()
            basemodel.save()
            print(basemodel.id)

    def do_show(self, line):
        """ Prints the string representation of an instance\
            based on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234 """
        input = line.split()
        keys_dict = self.get_objects()
        if not input:
            print("** class name missing **")
        else:
            if input[0] in keys_dict.values() and len(input) == 1:
                print("** instance id missing **")
            elif input[0] not in keys_dict.values() and len(input) == 1:
                print("** class doesn't exist **")
            elif input[1] in keys_dict.keys():
                if input[0] not in keys_dict.values():
                    print("** no instance found **")
                else:
                    file_storage = FileStorage()
                    file_storage.reload()
                    all_objs = file_storage.all()
                    print(all_objs[".".join(input)])

    def get_objects(self):
        """
        This is a method that gets all the objects\
            that are currently in the storage.
            Return:
                A dictionary of the names\
                and ids of objects in the memory.
        """
        file_storage = FileStorage()
        file_storage.reload()
        all_objs = file_storage.all()
        keys = []
        for key in all_objs.keys():
            keys.append(key)
        keys_dict = {}
        for item in keys:
            key_value = item.split(".")
            keys_dict[key_value[1]] = key_value[0]
        return keys_dict

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id\
            (save the change into the JSON file)
            Ex: $ destroy BaseModel 1234-1234-1234 """
        pass

    def do_all(self, line):
        """ Prints all string representation of all instance\
            based or not on the class name.
            Ex: $ all BaseModel or $ all """
        pass

    def do_update(self, line):
        """ Updates an instance based on the class name and id by\
            adding or updating attribute,\
            (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com' """
        pass


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        # Implementation of non interactive mode
        HBNBCommand().onecmd(''.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
