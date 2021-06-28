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
            b = storage.classes[arg[0]]()
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
            print([str(o) for o in storage.all().values()])
        elif self.validation_arguments([arg], 1):
            print([str(o)
                  for o in storage.all().values() if arg == type(o).__name__])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute
        """

        if arg:
            arg = arg.split(' ')

        if self.validation_arguments(arg, 3):
            try:
                b = storage.all()[arg[0] + "." + arg[1]]
                clsAttr = type(getattr(b, arg[2], ""))
                setattr(b, arg[2], clsAttr(arg[3]))
                b.save()
            except ValueError as e:
                print(e)

#            print(b)

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
# update [class, id, attr, val]
        if 1 <= maxValidations and len(args_array) < 1:
            print("** class name missing **")
            return False
        elif 1 <= maxValidations and args_array[0] not in storage.classes.keys():
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

    def do_User(self, arg):
        """Function to User command in console"""
        self.class_functions(storage.classes['User'], arg)

    def do_City(self, arg):
        """Function to City command in console"""
        self.class_functions(storage.classes['City'], arg)

    def do_BaseModel(self, arg):
        """Function to BaseModel command in console"""
        self.class_functions(storage.classes['BaseModel'], arg)

    def do_State(self, arg):
        """Function to State command in console"""
        self.class_functions(storage.classes['State'], arg)

    def do_Amenity(self, arg):
        """Function to Amenity command in console"""
        self.class_functions(storage.classes['Amenity'], arg)

    def do_Place(self, arg):
        """Function to Place command in console"""
        self.class_functions(storage.classes['Place'], arg)

    def do_Review(self, arg):
        """Function to Review command in console"""
        self.class_functions(storage.classes['Review'], arg)

    def class_functions(self, cls, arg):
        if arg == '.all()':
            self.do_all(cls.__name__)
        elif arg == '.count()':
            print(sum([1 for o in storage.all().values() if type(o) == cls]))


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
