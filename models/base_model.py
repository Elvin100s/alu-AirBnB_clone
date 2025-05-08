#!/usr/bin/python3
"""Defines the FileStorage class with all fixes for datetime and reload"""
import json
from datetime import datetime

class FileStorage:
    """Manages persistent storage in JSON format with UTC datetime handling"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns filtered or full object dictionary"""
        if cls:
            return {k: v for k, v in self.__objects.items() 
                   if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds object with composite key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON with ISO-8601 timestamps"""
        serialized = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserializes JSON with proper datetime reconstruction"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    cls_name = obj_dict['__class__']
                    if cls_name in classes:
                        # Convert ISO strings to datetime objects
                        for time_attr in ['created_at', 'updated_at']:
                            if obj_dict.get(time_attr):
                                obj_dict[time_attr] = datetime.strptime(
                                    obj_dict[time_attr],
                                    '%Y-%m-%dT%H:%M:%S.%f'
                                )
                        self.__objects[key] = classes[cls_name](**obj_dict)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def delete(self, obj=None):
        """Removes object from storage"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """Reloads storage for fresh data"""
        self.reload()
