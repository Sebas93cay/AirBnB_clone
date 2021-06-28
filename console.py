#!/usr/bin/python3
"""
This module contains the console
"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg:
            arg = [arg]

        if self.validation_arguments(arg, 1):
            b = BaseModel()
            b.save()
            print(b.id)

        return False

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if arg:
            arg = arg.split(' ', 2)

        if self.validation_arguments(arg, 2):
            print(storage.all()[arg[0] + "." + arg[1]])

        return False

    def do_destroy(self, arg):
        """Delete an instance of the stored instance"""
        if arg:
            arg = arg.split(' ', 2)

        if self.validation_arguments(arg, 2):
            del storage.all()[arg[0] + "." + arg[1]]
            storage.save()

        return False

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if not arg:
            print(storage.all())
        elif self.validation_arguments([arg], 1):
            objects = {k: v for k, v in storage.all().items() if arg in k}
            print(objects)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute
        """

        if arg:
            arg = arg.split(' ')

        if self.validation_arguments(arg, 3):
            b = storage.all()[arg[0] + "." + arg[1]]
            setattr(b, arg[2], arg[3])
            b.save()
            print(b)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        self.close()
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print("")
        self.close()
        return True

    def validation_arguments(self, args_array, maxValidations):
        """validate array of arguments"""

        if 1 <= maxValidations and len(args_array) < 1:
            print("** class name missing **")
            return False
        elif 1 <= maxValidations and args_array[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return False
        elif 2 <= maxValidations and len(args_array) < 2:
            print("** instance id missing **")
            return False
        elif 2 <= maxValidations and \
                args_array[0] + "." + args_array[1] not in \
                storage.all().keys():
            print("** no instance found **")
            return False
        elif 3 <= maxValidations and len(args_array) < 3:
            print("** attribute name missing **")
            return False
        elif 3 <= maxValidations and len(args_array) < 4:
            print("** value missing **")
            return False

        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    # where HBNBCommand.function is:
    def function(self):
        return int(input("prompt> "))


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
