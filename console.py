#!/usr/bin/python3
"""
This module contains the console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome babe'
    prompt = '(hbnb) '
    file = None

    # def do_help(self, arg):
    #    print('I\'ll help you out')

    def do_quit(self, arg):
        """Quit command to exit the program"""
        self.close()
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print("")
        self.close()
        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
