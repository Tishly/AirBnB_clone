#!/usr/bin/python3
"""
Contains test cases for the Amenity class
"""

import unittest
from models import amenity
from datetime import datetime
import inspect
from models.base_model import BaseModel
Amenity = amenity.Amenity()


class TestAmenityDocs(unittest.TestCase):
    """Tests to check the docstring of the Amenity class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.amenity_f = inspect.getmembers(Amenity, inspsect.isfunction)

    def test_pep8_conformity_amenity(self):
        """Test that models/amenity.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformity_test_amenity(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8"""
        pep8s = pep8.styleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """Test for amenity.py module docstring"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """Test for amenity.py class docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_func_docstring(self):
        """Test for the docstring in Amenity methods"""
        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAmenity(unittest.TestCase):
    """Test for the Amenity class"""
    def test_is_subclass(self):
        """Test that Amenity is subclass of BaseModel"""
        amn = Amenity()
        self.assertIsInstance(amn, BaseModel)
        self.assertTrue(hasattr(amn, "id"))
        self.assertTrue(hasattr(amn, "created_at"))
        self.assertTrue(hasattr(amn, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has attribute name and is an empty string"""
        amn = Amenity()
        self.assertEqual(amn.name, "")
        self.assertTrue(hasattr(amn, "name"))

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attributes"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"], str))
        self.assertEqual(type(new_d["updated_at"], str))
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
