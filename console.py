#!/usr/bin/python3
"""Console module for HBNB project with exact validation formatting"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """Command interpreter with exact validation formatting"""
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def _key_value_parser(self, args):
        """Helper method to parse key-value pairs"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Correct output - console: create User"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        
        # Handle both traditional and key=value creation
        if len(args) > 1:
            new_dict = self._key_value_parser(args[1:])
            instance = self.classes[args[0]](**new_dict)
        else:
            instance = self.classes[args[0]]()
        
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Correct output - console: show User "existing ID\""""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
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
        """Correct output - console: destroy User "existing ID\""""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
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
        storage.save()

    def do_all(self, arg):
        """Correct output - console: all User"""
        args = shlex.split(arg)
        obj_list = []
        all_objs = storage.all()
        
        if not args:
            for obj in all_objs.values():
                obj_list.append(str(obj))
            print(obj_list)
            return
        
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        
        for key, obj in all_objs.items():
            if key.split('.')[0] == args[0]:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Correct output - console: update User "existing ID" attribute_name attribute_value"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        
        obj = all_objs[key]
        attr_name = args[2]
        attr_value = args[3]
        
        # Handle type conversion
        try:
            if '.' in attr_value:
                attr_value = float(attr_value)
            else:
                attr_value = int(attr_value)
        except ValueError:
            pass
        
        setattr(obj, attr_name, attr_value)
        obj.save()

    def default(self, arg):
        """Handle <class name>.<command>() syntax"""
        cmd_dict = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'count': self.do_count
        }
        
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg[:arg.index('.')]
            command = arg[arg.index('.') + 1:arg.index('(')]
            args = arg[arg.index('(') + 1:arg.index(')')]
            
            if command in cmd_dict:
                if command == "update":
                    if '{' in args and '}' in args:
                        # Handle dictionary update
                        obj_id = args.split(',')[0].strip('"\' ')
                        dict_str = args[args.index('{'):args.index('}') + 1]
                        return cmd_dict[command](f"{cls} {obj_id} {dict_str}")
                    else:
                        # Handle normal update
                        args = args.replace(',', '')
                return cmd_dict[command](f"{cls} {args}")
        
        print(f"*** Unknown syntax: {arg}")
        return False

    def do_count(self, arg):
        """Count instances of a class"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        
        count = 0
        for key in storage.all():
            if key.split('.')[0] == args[0]:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
