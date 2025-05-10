#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)', end=' ')

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        return False

    def precmd(self, line):
        """Reformat command line for advanced command syntax"""
        if not line.strip():
            return ''
            
        _cmd = _cls = _id = _args = ''

        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            pline = line[:]
            _cls = pline[:pline.find('.')]
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in self.dot_cmds:
                raise Exception

            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                pline = pline.partition(', ')
                _id = pline[0].replace('\"', '')
                pline = pline[2].strip()
                if pline:
                    if pline[0] == '{' and pline[-1] == '}' and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
            return ' '.join([_cmd, _cls, _id, _args])

        except Exception:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)', end=' ')
        return stop

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of instances"""
        args = arg.split()
        obj_list = []
        if not args:
            for value in storage.all().values():
                obj_list.append(str(value))
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for key, value in storage.all().items():
                if key.split('.')[0] == args[0]:
                    obj_list.append(str(value))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        instance = storage.all()[key]
        if attr_name in self.types:
            attr_value = self.types[attr_name](attr_value)
        setattr(instance, attr_name, attr_value)
        instance.save()

    def default(self, line):
        """Handle class commands: <class name>.<command>()"""
        cmd_dict = {
            'all': self.do_all,
            'count': self.do_count,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update
        }
        match = self.parse_dot_notation(line)
        if not match:
            return cmd.Cmd.default(self, line)
        class_name, command, args = match
        if command not in cmd_dict:
            return cmd.Cmd.default(self, line)
        cmd_dict[command](f"{class_name} {args}")

    def do_count(self, arg):
        """Count current number of class instances"""
        count = 0
        for key in storage.all():
            if arg == key.split('.')[0]:
                count += 1
        print(count)

    def parse_dot_notation(self, line):
        """Helper method to parse class.command() syntax"""
        if '.' not in line or '(' not in line or ')' not in line:
            return None
        class_name = line[:line.find('.')]
        command = line[line.find('.') + 1:line.find('(')]
        args = line[line.find('(') + 1:line.find(')')].strip('"')
        return (class_name, command, args)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
