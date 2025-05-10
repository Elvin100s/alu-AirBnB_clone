#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for AirBnB clone."""
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
