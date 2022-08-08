#!/usr/bin/python3

"""
Contains the TestUserDocs classes
"""

from datetime import datetime
import inspect
from models import user
from models.base_model import BaseModel
import pep8
import unittest
User = user.User


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
    """Set up for the doc tests"""
    cls.user_f = inspect.getmembers(User, inspect.isfunction)
