#!/usr/bin/python3
"""Command interpreter for AirBnB project"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Custom command interpreter class for AirBnB"""
    
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program (Ctrl+D)"""
        print()  # Ensure clean exit with newline
        return True

    def emptyline(self):
        """Handles empty input lines"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
