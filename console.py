#!/usr/bin/python3
"""
    AirBnB Clone project - hbnb
    Command interpreter to manage our AirBnB objects.
    Entry point of the command interpreter:
"""


import cmd
import models
from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, line):
        'exit the program'
        return True

    def do_quit(self, line):
        'exit the program using quit'
        return True

    def emptyline(self):
        'Handle empty line, do not execute anything'
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel,
saves it (to the JSON file) and prints the id
        """
        if args == "":
            print("** class name missing **")
        else:
            try:
                obj = eval(args)()
                models.storage.new(obj)
                models.storage.save()
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance
based on the class name and id
        """
        argv = args.split(" ")
        if argv[0] == "":
            print("** class name missing **")
        elif len(argv) == 1:
            print("** instance id missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
