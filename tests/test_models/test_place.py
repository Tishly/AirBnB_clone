#!/usr/bin/python3
"""
Contains the test cases for Place class
"""

import unittest
from models import place
from datetime import datetime
import inspect
from models.base_model import BaseModel
Place = place.Place()


class TestPlaceDocs(unittest.TestCase):
    """Tests to check the docstring of the Place class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.place_f = inspect.getmembers(Place, inspsect.isfunction)

    def test_pep8_conformity_place(self):
        """Test that models/place.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformity_test_place(self):
        """Test that tests/test_models/test_place.py conforms to PEP8"""
        pep8s = pep8.styleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_place_module_docstring(self):
        """Test for place.py module docstring"""
        self.assertIsNot(place.__doc__, None,
                         "place.py needs a docstring")
        self.assertTrue(len(place.__doc__) >= 1,
                        "place.py needs a docstring")

    def test_place_class_docstring(self):
        """Test for place.py class docstring"""
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place__doc__) >= 1,
                        "Place class needs a docstring")

    def test_place_func_docstring(self):
        """Test for the docstring in Place methods"""
        for func in self.place_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """Test for the Place class"""
    def test_is_subclass(self):
        """Test that Place is subclass of BaseModel"""
        pl = Place()
        self.assertIsInstance(pl, BaseModel)
        self.assertTrue(hasattr(pl, "id"))
        self.assertTrue(hasattr(pl, "created_at"))
        self.assertTrue(hasattr(pl, "updated_at"))

    def test_city_id_attr(self):
        """Test that Place has attr city_id and it is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_user_id_attr(self):
        """Test that place has attr user_id and it is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_name_attr(self):
        """Test that Place has attr name and it is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_description_attr(self):
        """Test that Place has attr description and it is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_number_rooms_attr(self):
        """Test that Place has attr number_rooms and it is an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test that Place has attr number_bathrooms and it is an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Test that Place has attr max_guest and it is an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night_attr(self):
        """Test that Place has attr price_by_night and it is an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(place.price_by_night, 0)

    def test_latitude_attr(self):
        """Test that Place has attr latitude and it is a float == 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(place.latitude, 0.0)

    def test_longitude_attr(self):
        """Test that Place has attr longitude and it is a float == 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)

    def test_amennity_ids_attr(self):
        """Test that Place has attr amennity_ids and it is an empty list"""
        place = Place()
        self.assertTrue(hasattr(place, "amennity_ids"))
        self.assertEqual(type(place.amennity_ids), list)
        self.assertEqual(place.amennity_ids, 0)

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attributes"""
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in p.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"], str))
        self.assertEqual(type(new_d["updated_at"], str))
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        p = Place()
        string = "[Place] ({}) {}".format(p.id, p.__dict__)
        self.assertEqual(string, str(p))
