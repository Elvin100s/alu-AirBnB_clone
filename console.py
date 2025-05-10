#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for AirBnB clone."""
    prompt = '(hbnb) '
    valid_classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            instance = self.valid_classes[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in storage.all().items()
                  if key.split('.')[0] == args[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3].strip('"')
                if attr_name not in ["id", "created_at", "updated_at"]:
                    setattr(obj, attr_name, attr_value)
                    obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
