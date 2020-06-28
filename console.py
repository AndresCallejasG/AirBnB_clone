#!/usr/bin/python3
"""
    AirBnB Clone project - hbnb
    Command interpreter to manage our AirBnB objects.
    Entry point of the command interpreter:
"""


import cmd
import models
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    classes = ["BaseModel"]

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
        argv = shlex.split(args)
        if len(argv) == 0:
            print("** class name missing **")
            return
        elif argv[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(argv) == 1:
            print("** instance id missing **")
            return

        required_key = argv[0] + "." + argv[1]
        try:
            required_obj = (models.storage.all())[required_key]
            print(required_obj.to_dict())
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the
class name and id (save the change into the JSON file).
        """
        argv = shlex.split(args)
        if len(argv) == 0:
            print("** class name missing **")
            return
        elif argv[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(argv) == 1:
            print("** instance id missing **")
            return

        required_key = argv[0] + "." + argv[1]
        try:
            models.storage.destroy(required_key)
            models.storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation
of all instances based or not on the class name
        """
        argv = shlex.split(args)
        all_obj = models.storage.all()
        my_list = []
        if len(argv) != 0:
            if argv[0] not in self.classes:
                print("** class doesn't exist **")
                return
            for k, v in all_obj.items():
                if type(v) is eval(argv[0]):
                    my_list.append(v.__str__())
        else:
            for k, v in all_obj.items():
                my_list.append(v.__str__())

        print(my_list)

    def do_update(self, args):
        """Updates an instance based on the class
name and id by adding or updating attribute (save the change into the JSON file)
        """
        argv = shlex.split(args)
        if len(argv) == 0:
            print("** class name missing **")
            return
        elif argv[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(argv) < 2:
            print("** instance id missing **")
            return
        elif len(argv) < 3:
            print("** attribute name missing **")
            return
        elif len(argv) < 4:
            print("** value missing **")
            return
        try:
            required_key = argv[0] + "." + argv[1]
            print(required_key)
            required_obj = (models.storage.all())[required_key]
            setattr(required_obj, argv[2], argv[3])
            models.storage.save()
        except KeyError:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
