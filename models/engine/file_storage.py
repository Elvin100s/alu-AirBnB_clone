#!/usr/bin/python3
"""Defines the FileStorage class for object persistence"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns dictionary of all objects or filtered by class"""
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            return {k: v for k, v in self.__objects.items()
                    if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds object to storage with key <class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON file"""
        serialized = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserializes JSON file to objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key, val in data.items():
                    cls = val['__class__']
                    del val['__class__']
                    self.__objects[key] = eval(cls)(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Removes object from storage"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """Reloads objects from file"""
        self.reload()
