#!/usr/bin/python3
"""Initialize the models package and create storage instance"""
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for the application
storage = FileStorage()
# Load all objects from the JSON file at startup
storage.reload()
