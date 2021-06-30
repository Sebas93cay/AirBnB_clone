#!/usr/bin/python3
"""
This module contains the console
"""


import cmd
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is the console inherinted from cmd
    """
    prompt = '(hbnb) '
    # file = None

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg:
            arg = [arg]

        if self.validation_arguments(arg, 1):
            obj = storage.classes[arg[0]]()
            obj.save()
            print(obj.id)

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
            arg = '["' + arg[0] + '","' + arg[1] + \
                '","' + arg[2] + '", ' + arg[3] + "]"
            try:
                arg = json.loads(arg)
            except Exception as e:
                print(e)
                print("Value not supported")
                return False
            self.update(arg[0], arg[1], arg[2], arg[3])

    def update(self, cls_s, id_s, attribute, value):
        """
        Update an object of type cls_s and id id_s
        both cls_s and id_s are strings
        """
        obj = storage.all()[cls_s+"."+id_s]
        if attribute in obj.__class__.__dict__.keys():
            clsAttr = type(getattr(obj, attribute, ""))
            setattr(obj, attribute, clsAttr(value))
        else:
            setattr(obj, attribute, value)
        obj.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        # self.close()
        return True

    def emptyline(self):
        """Do nothing when line is empty"""
        pass

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        # print("")
        # self.close()
        return True

    def validation_arguments(self, args_array, maxValidations):
        """
        validate array of arguments
        args_array is an array of string with format:
        [class, id, attribute, value]
        """

        if 1 <= maxValidations and len(args_array) < 1:
            print("** class name missing **")
            return False
        elif 1 <= maxValidations and args_array[0] not in\
                storage.classes.keys():
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

    def act_one_method_class(self, cls, method, text):
        """
        This functions execute the method method
        of the class cls with the arguments text
        """
        text = text.replace("'", '"')
        try:
            args_parsed = json.loads("[" + text + "]")
        except Exception as e:
            print("Argument Error")
            print(e)
            args_parsed = False

        if args_parsed:
            method(cls.__name__+" "+args_parsed[0])

    def class_functions(self, cls, arg):
        """
        method for sintax: <clasname>.<method>
        """
        if arg == 'all()':
            self.do_all(cls.__name__)
        elif arg == 'count()':
            print(sum([1 for o in storage.all().values() if type(o) == cls]))
        elif arg[:5] == 'show(':
            self.act_one_method_class(cls, self.do_show, arg[5:-1])
        elif arg[:8] == 'destroy(':
            self.act_one_method_class(cls, self.do_destroy, arg[8:-1])
        elif arg[:7] == 'update(':
            entrada = arg[7:-1].replace("'", '"')
            try:
                list_arg = json.loads("[" + entrada + "]")
            except Exception as e:
                print("Argument Error")
                print(e)
                return False
            if len(list_arg) < 3:
                if len(list_arg) > 1 and type(list_arg[1]) == dict:
                    for key, value in list_arg[1].items():
                        if self.validation_arguments(
                                [cls.__name__, list_arg[0], key,
                                 str(value)], 3):
                            self.update(
                                cls.__name__, list_arg[0], key, value)
                else:
                    print("** arguments missing")
                    return False
            elif type(list_arg[1]) == str:
                if self.validation_arguments(
                        [cls.__name__, list_arg[0], list_arg[1],
                         str(list_arg[2])], 3):
                    self.update(
                        cls.__name__, list_arg[0], list_arg[1], list_arg[2])
            else:
                print("** wrong type of arguments")
                return False
        else:
            print("** not recognized method")

    def default(self, arg):
        """
        This functions validate if input does not
        match with any of the do_methods
        This functions checks if sintax is <classname>.<method>
        """
        args = arg.split('.')
        if args[0] in storage.classes.keys():
            self.class_functions(storage.classes[args[0]], args[1])
        else:
            print("*** Unknown syntax: {}".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
