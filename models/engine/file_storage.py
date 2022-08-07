#!usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage():
    """Represent the file storage for AirBnB project.
    Initialize a new Base.
    Args:
        __file_path(str): pathname of file.
        __objects (dict): where objects of the class are stored.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set the __objects to always represent key <obj class name>.id"""
        obj_name = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects.update({obj_name: obj})

    def save(self):
        """converts object to JSON and store in file"""
        objdict = {}
        for k, v in FileStorage.__objects.items():
            objdict[k] = v.to dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """converts back to object if file exist"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                reverse_dict = json.load(f)
            
            for k, v in reverse_dict.items():
                cls_name = v.get("__class__")
                obj = eval(cls_name + '(**v)')
                FileStorage.__objects[k] = obj
        
        except FileNotFoundError:
            pass
