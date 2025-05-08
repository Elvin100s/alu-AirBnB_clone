#!/usr/bin/python3
""" Enhanced HBNB Console Module """
import cmd
import sys
import ast
import shlex
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Enhanced HBNB console with security fixes and new features """

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def precmd(self, line):
        """Secure command reformatter with AST-based parsing"""
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            pline = line[:]
            _cls = pline[:pline.find('.')]
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            
            if _cmd not in ['all', 'count', 'show', 'destroy', 'update']:
                return line

            # Secure argument parsing with ast.literal_eval
            args_str = pline[pline.find('(') + 1:pline.find(')')]
            if args_str:
                try:
                    args = ast.literal_eval(f'[{args_str}]')
                except (ValueError, SyntaxError):
                    return line
                
                if isinstance(args, list):
                    args = ' '.join(f'"{x}"' if ' ' in str(x) else str(x) 
                                  for x in args)
                elif isinstance(args, dict):
                    args = ' '.join(f'{k}="{v}"' if ' ' in str(v) else f'{k}={v}'
                                  for k, v in args.items())
                return f'{_cmd} {_cls} {args}'
            return f'{_cmd} {_cls}'
        except Exception:
            return line

    def _convert_value(self, value):
        """Safe type conversion for attribute values"""
        if value.startswith('"') and value.endswith('"'):
            return value[1:-1].replace('_', ' ')
        try:
            return ast.literal_eval(value)
        except (ValueError, SyntaxError):
            return value

    def do_create(self, arg):
        """Secure object creation with parameter validation"""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        cls_name = args[0]
        
        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return

        params = {}
        for param in args[1:]:
            if '=' not in param:
                continue
            key, value = param.split('=', 1)
            params[key] = self._convert_value(value)

        new = self.classes[cls_name](**params)
        storage.new(new)
        print(new.id)
        storage.save()

    def do_show(self, arg):
        """Improved show with better error handling"""
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
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    # ... (other methods like destroy, all, count with similar security improvements)

    def do_update(self, arg):
        """Secure update with dictionary support"""
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
        if key not in storage.all():
            print("** no instance found **")
            return

        obj = storage.all()[key]
        if len(args) >= 3 and args[2].startswith('{') and args[2].endswith('}'):
            try:
                updates = ast.literal_eval(args[2])
                if isinstance(updates, dict):
                    for k, v in updates.items():
                        setattr(obj, k, self._convert_value(str(v)))
                    obj.save()
                    return
            except (ValueError, SyntaxError):
                pass

        if len(args) < 4:
            print("** attribute name missing **" if len(args) < 3 
                  else "** value missing **")
            return

        attr_name = args[2]
        attr_value = self._convert_value(args[3])
        setattr(obj, attr_name, attr_value)
        obj.save()

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_quit(self, arg):
        """Exit the console"""
        return True

    def do_EOF(self, arg):
        """Handle EOF signal"""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
