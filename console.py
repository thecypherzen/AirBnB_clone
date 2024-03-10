#!/usr/bin/python3
"""
This is a program that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ This is a class that defines the command interpreter """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        print()
        """ EOF command to exit the program """
        return True

    def do_create(self, line):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel """
        if line == "":
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            basemodel = BaseModel()
            basemodel.save()
            print(basemodel.id)

    def do_show(self, line):
        """  Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234 """


    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234 """
        pass

    def do_all(self, line):
        """ Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all """
        pass

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com' """
        pass

if __name__ == '__main__':
        HBNBCommand().cmdloop()
