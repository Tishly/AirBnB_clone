#!/usr/bin/python3
"""
Contains test cases for Review class
"""

import unittest
from models import review
from datetime import datetime
import inspect
from models.base_model import BaseModel
Review = review.Review()


class TestReviewDocs(unittest.TestCase):
    """Tests to check the docstring of the Review class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.review_f = inspect.getmembers(Review, inspsect.isfunction)

    def test_pep8_conformity_review(self):
        """Test that models/review.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformity_test_review(self):
        """Test that tests/test_models/test_review.py conforms to PEP8"""
        pep8s = pep8.styleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_module_docstring(self):
        """Test for review.py module docstring"""
        self.assertIsNot(review.__doc__, None,
                         "review.py needs a docstring")
        self.assertTrue(len(review.__doc__) >= 1,
                        "review.py needs a docstring")

    def test_review_class_docstring(self):
        """Test for review.py class docstring"""
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(Review__doc__) >= 1,
                        "Review class needs a docstring")

    def test_Review_func_docstring(self):
        """Test for the docstring in Review methods"""
        for func in self.review_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """Test for the Review class"""
    def test_is_subclass(self):
        """Test that Review is subclass of BaseModel"""
        r = Review()
        self.assertIsInstance(r, BaseModel)
        self.assertTrue(hasattr(r, "id"))
        self.assertTrue(hasattr(r, "created_at"))
        self.assertTrue(hasattr(r, "updated_at"))

    def test_place_id_attr(self):
        """Test that Review has attr place_id and it is an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_user_id_attr(self):
        """Test that Review has attr user_id and it is an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")

    def test_text_attr(self):
        """Test that Review has attr text and it is an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attributes"""
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in r.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(type(new_d["created_at"], str))
        self.assertEqual(type(new_d["updated_at"], str))
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        r = Review()
        string = "[Review] ({}) {}".format(r.id, r.__dict__)
        self.assertEqual(string, str(r))
