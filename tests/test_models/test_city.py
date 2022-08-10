#!/usr/bin/python3
"""
Contains test cases for the City class
"""

import unittest
from models import city
from datetime import datetime
import inspect
from models.base_model import BaseModel
City = city.City


class TestCityDocs(unittest.TestCase):
    """Tests to check the docstring of the City class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.city_f = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformity_city(self):
        """Test that models/city.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformity_test_city(self):
        """Test that tests/test_models/test_city.py conforms to PEP8"""
        pep8s = pep8.styleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """Test for city.py module docstring"""
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for city.py class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City__doc__) >= 1,
                        "City class needs a docstring")

    def test_city_func_docstring(self):
        """Test for the docstring in City methods"""
        for func in self.city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCity(unittest.TestCase):
    """Test for the City class"""
    def test_is_subclass(self):
        """Test that City is subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name_attr(self):
        """Test that City has attribute name and is an empty string"""
        cty = City()
        self.assertEqual(cty.name, "")
        self.assertTrue(hasattr(cty, "name"))

    def test_state_id_attr(self):
        """Test that City has attribute state_id and is an empty string"""
        cty = City()
        self.assertEqual(cty.state_id, "")
        self.assertTrue(hasattr(city, "state_id"))

    def test_to_dict_creats_dict(self):
        """Test to_dict method creates a dictionary with proper attributes"""
        c = City()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in c.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test to_dict for correct values"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"], str))
        self.assertEqual(type(new_d["updated_at"], str))
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
