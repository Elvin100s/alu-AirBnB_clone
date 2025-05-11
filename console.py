#!/usr/bin/python3
"""Console Module"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    # ... (keep all your existing methods exactly as they are)

    def do_create(self, arg):
        """Create an object of any class"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[args[0]]()
        print(new_instance.id)
        storage.save()

    # ... (rest of your existing console implementation)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
