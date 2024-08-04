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

    def do_all(self, line):
        """
            Prints all string representation of all instance\
            based or not on the class name.
            Ex: $ all BaseModel or $ all
        """
        if line:
            if line not in self.__classes:
                print("** class doesn't exist **")
            else:
                file_storage = FileStorage()
                file_storage.reload()
                all_objs = file_storage.all()
                for key in all_objs.keys():
                    key_list = key.split(".")
                    if key_list[0] == line:
                        print(f'["{all_objs[key]}"]')
                    else:
                        continue
        else:
            file_storage = FileStorage()
            file_storage.reload()
            all_objs = file_storage.all()
            for key in all_objs.keys():
                print(all_objs[key])

    def do_update(self, line):
        """
            Updates an instance based on the class name and id by\
            adding or updating attribute,\
            (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com'
        """
        input = line.split()
        input_len = len(input)
        keys_dict = self.get_objects()
        if not input:
            print("** class name missing **")
            return
        if input[0] in self.__classes and input_len == 1:
            print("** instance id missing **")
            return
        if input[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if input[1] not in keys_dict.keys() or \
                input[0] != keys_dict[input[1]]:
            print("** no instance found **")
            return
        if input_len == 2:
            print("** attribute name missing **")
            return
        if input_len == 3:
            print("** value missing **")
            return
        key = input[0] + '.' + input[1]
        fs = FileStorage()
        fs.reload()
        all_objs = fs.all()
        setattr(all_objs[key], input[2], input[3])
        fs.save()

    def do_clear(self, line):
        """ Clears the screen of the console """
        system('cls' if name == 'nt' else 'clear')

    def do_check(self, line):
        """checks if class_name exists or obj_id matches for instance"""
        instance = None
        input = line.split()
        if len(input) == 0:
            print("** class name missing **")
        elif len(input) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all().values()
            if input[0] not in [obj.__class__.__name__ for obj in all_objs]:
                print("** class doesn't exist **")
            else:
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
