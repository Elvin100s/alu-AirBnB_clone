#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        """Ignore empty lines."""
        pass

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit on EOF (Ctrl+D)."""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of a class."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.__classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, arg):
        """Delete an instance by class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()  # Critical: Ensure changes persist

    def do_all(self, arg):
        """Print all instances (optionally filtered by class)."""
        args = arg.split()
        all_objs = storage.all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in all_objs.items()
              if key.split('.')[0] == args[0]])

    def do_update(self, arg):
        """Update an instance's attribute."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = all_objs[key]
        attr_name = args[2]
        attr_value = args[3]
        # Convert attr_value to correct type (e.g., int, float, or str)
        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()

    def default(self, arg):
        """Handle advanced commands like <class>.all()."""
        methods = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        match = re.fullmatch(r"(\w+)\.(\w+)\((.*)\)", arg)
        if not match:
            return super().default(arg)
        class_name, method_name, args_str = match.groups()
        if method_name not in methods:
            return super().default(arg)
        if method_name in ["all", "count"]:
            return methods[method_name](class_name)
        args = args_str.split(", ")
        if len(args) == 1 and args[0].strip('"') == "":
            args = []
        elif len(args) >= 1:
            args[0] = args[0].strip('"\'')
        if method_name in ["show", "destroy"]:
            return methods[method_name](f"{class_name} {args[0]}")
        if method_name == "update":
            if len(args) >= 2:
                args[1] = args[1].strip('"\'')
            if len(args) >= 3:
                args[2] = args[2].strip('"\'')
            return methods[method_name](f"{class_name} {' '.join(args)}")

    def do_count(self, arg):
        """Count instances of a class."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for key in storage.all() if key.split('.')[0] == args[0])
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
