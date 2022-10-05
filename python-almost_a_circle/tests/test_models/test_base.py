#!/usr/bin/python3
""" Contains tests for the Base class """


import unittest
import pycodestyle
import json
from models.rectangle import Rectangle
from models.square import Square
from models import base
Base = base.Base



class TestBaseDocs(unittest.TestCase):
    """ Testing class Base for documentation """
    def test_base_docs(self):
        """ checking for docs """
        module_docs = "models.base".__doc__
        self.assertTrue(len(module_docs) > 1)

        class_docs = Base.__doc__
        self.assertTrue(len(class_docs) > 1)

    def test_pycode_class(self):
        """ Checks pycodestyle for base """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """ Checks pycodestyle for test_base """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")


class TestBase(unittest.TestCase):
    """ Testing for class Base """

    @classmethod
    def setUpClass(cls):
        """ setup attributes for testing """
        Base._base__nb_objects = 0
        cls.b1 = Square(8, 0, 0, 8)
        cls.b2 = Square(4)

    def test_empty_id(self):
        """ tests id as empty """
        Base._Base__nb_objects = 0
        b3 = Base()
        self.assertEqual(b3.id, 1)

    def test_assigned_id(self):
        """ test to change id """
        self.assertEqual(self.b1.id, 8)
        self.b1.id = 5
        self.assertEqual(self.b1.id, 5)

    def test_TypeError(self):
        """ calling class with more than 1 arg """
        with self.assertRaises(TypeError):
            base3 = Base(2, 5)

    def test_empty_to_json_sting(self):
        """ Test passing empty list/None """
        j_string = Base.to_json_string([])
        self.assertTrue(type(j_string) is str)
        self.assertEqual(j_string, "[]")

    def test_empty_from_json_sting(self):
        """ Test passing empty string """
        self.assertEqual([], Base.from_json_string(""))

    def test_None_to_json_sting(self):
        """ Test passing None to JSON """
        j_string = Base.to_json_string(None)
        self.assertTrue(type(j_string) is str)
        self.assertEqual(j_string, "[]")

    def test_None_from_json_sting(self):
        """ Test for passing None from JSON """
        self.assertEqual([], Base.from_json_string(None))
