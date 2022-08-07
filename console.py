#!/usr/bin/python3
"""Defines the hbnb console."""
import cmd
import models
from shlex import split
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Defines the hbnb command interpreter.

        Attributes:
        prompt (str): The command prompt.
    """

    prompt = '(hbnb) '
    __classes = ['BaseModel',
                 'User',
                 'Place',
                 'State',
                 'City',
                 'Amenity',
                 'Review'
                 ]

    def emptyline(self):
        """do nothing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        raise SystemExit

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def do_help(self, args):
        """help"""
        cmd.Cmd.do_help(self, args)

    def do_create(self, args):
        """Usage: create <class> <key 1>=<value> ...
        create a new cls instance with given keys/values and print its id"""
        c_list = args.split()
        if not c_list:
            print('** class name missing **')
        elif c_list[0] not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
        else:
            my_object = eval(c_list[0] + '()')

            for i in range(1, len(c_list)):
                result = c_list[i].split('=')
                result[1] = result[1].replace('_', ' ')
                setattr(my_object, result[0], result[1])

            my_object.save()
            print(my_object.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        s_list = args.split()
        if not s_list:
            print('** class name missing**')
        elif s_list[0] not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
        elif len(s_list) == 1:
            print('** instance id missing **')
        else:
            objects = models.storage.all()
            instance = s_list[0] + '.' + s_list[1]
            if instance in objects.keys():
                print(objects[instance])
            else:
                print('** no instance found **')

    def do_destory(self, args):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        d_list = args.split()
        if not d_list:
            print('** class name missing**')
        elif d_list[0] not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
        elif len(d_list) == 1:
            print('** instance id missing **')
        else:
            objects = models.storage.all()
            instance = d_list[0] + '.' + d_list[1]
            if instance in objects.keys():
                del (objects[instance])
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        """Prints all string representation of all instances based
        or not on the class name"""
        a_list = args.split()
        if not args or a_list[0] in HBNBCommand.__classes:
            str_list = []
            objects = models.storage.all()
            for instance in objects.values():
                str_list.append(instance.__str__())
                print(str_list)
        else:
            print('** class doesn\'t exist **')

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save to JSON file)"""
        u_list = args.split()
        if not u_list:
            print('** class name missing**')
        elif u_list[0] not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
        elif len(u_list) == 1:
            print('** instance id missing **')
        elif len(u_list) == 2:
            print('** attribute name missing **')
        elif len(u_list) == 3:
            print('** value missing **')
        else:
            objects = models.storage.all()
            instance = "{}.{}".format(u_list[0], u_list[1])
            if instance in objects.keys():
                for value in objects.values():
                    try:
                        old_attr_type = type(getattr(value, u_list[2]))
                        u_list[3] = old_attr_type(u_list[3])
                    except AttributeError:
                        pass
                setattr(value, u_list[2], u_list[3])
                models.storage.save()
            else:
                print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
