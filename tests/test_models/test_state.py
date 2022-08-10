#!/usr/bin/python3
"""
Contains test cases for the State class
"""

import unittest
from models import state
from datetime import datetime
import inspect
from models.base_model import BaseModel
State = state.State()


class TestStateDocs(unittest.TestCase):
    """Tests to check the docstring of the State class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.state_f = inspect.getmembers(State, inspsect.isfunction)

    def test_pep8_conformity_state(self):
        """Test that models/state.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformity_test_state(self):
        """Test that tests/test_models/test_state.py conforms to PEP8"""
        pep8s = pep8.styleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_state_module_docstring(self):
        """Test for state.py module docstring"""
        self.assertIsNot(state.__doc__, None,
                         "state.py needs a docstring")
        self.assertTrue(len(state.__doc__) >= 1,
                        "state.py needs a docstring")

    def test_amenity_class_docstring(self):
        """Test for state.py class docstring"""
        self.assertIsNot(State.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(State__doc__) >= 1,
                        "State class needs a docstring")

    def test_state_func_docstring(self):
        """Test for the docstring in State methods"""
        for func in self.state_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestState(unittest.TestCase):
    """Test for the State class"""
    def test_is_subclass(self):
        """Test that State is subclass of BaseModel"""
        st = State()
        self.assertIsInstance(st, BaseModel)
        self.assertTrue(hasattr(st, "id"))
        self.assertTrue(hasattr(st, "created_at"))
        self.assertTrue(hasattr(st, "updated_at"))

    def test_name_attr(self):
        """Test that State has attribute name and it is an empty string"""
        stt = State()
        self.assertEqual(stt.name, "")
        self.assertTrue(hasattr(stt, "name"))

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attributes"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = State()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "State")
        self.assertEqual(type(new_d["created_at"], str))
        self.assertEqual(type(new_d["updated_at"], str))
        self.assertEqual(new_d["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))
