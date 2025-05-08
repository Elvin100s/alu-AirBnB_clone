"""Persistent JSON storage engine"""
import json
from datetime import datetime, timezone
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all stored objects"""
        return self.__objects

    def new(self, obj):
        """Add object with key format <class name>.<id>"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to JSON file with ISO datetime strings"""
        serialized = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserialize JSON file to objects with UTC datetime conversion"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    cls_name = val.pop('__class__')
                    for time_attr in ['created_at', 'updated_at']:
                        if time_attr in val:
                            val[time_attr] = datetime.strptime(
                                val[time_attr], '%Y-%m-%dT%H:%M:%S.%f'
                            ).replace(tzinfo=timezone.utc)
                    self.__objects[key] = eval(cls_name)(**val)
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            pass
