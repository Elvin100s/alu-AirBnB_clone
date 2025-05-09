#!/usr/bin/python3
"""
Module for FileStorage class that handles object serialization and deserialization
"""
import json
import os
from datetime import datetime


class FileStorage:
    """
    FileStorage class for serializing instances to JSON file
    and deserializing JSON file to instances
    """
    # Path to the JSON file
    __file_path = "file.json"
    # Dictionary that will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized = {}
        for key, obj in self.__objects.items():
            serialized[key] = obj.to_dict()
        
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        Only if the JSON file exists; otherwise, do nothing.
        No exception should be raised if the file doesn't exist.
        """
        # Import here to avoid circular import
        from models.base_model import BaseModel
        
        # Dictionary of supported classes
        classes = {
            'BaseModel': BaseModel
        }
        
        # Check if file exists
        if os.path.isfile(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    for key, value in data.items():
                        class_name = value["__class__"]
                        if class_name in classes:
                            # Recreate the instance using the dictionary
                            self.__objects[key] = classes[class_name](**value)
            except Exception:
                # If any error occurs, do nothing as per requirements
                pass
