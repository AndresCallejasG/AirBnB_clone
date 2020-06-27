#!/usr/bin/python3
"""
    AirBnB Clone project - hbnb
    Command interpreter to manage our AirBnB objects.
    Entry point of the command interpreter:
"""


import cmd
import models


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
