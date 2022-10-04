#!/usr/bin/python3
""" Contains tests for the Base class """


import unittest
import pycodestyle
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


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

    def test_empty_id(self):
        """ tests id as empty """
        Base._Base__nb_objects = 0
        base3 = Base()
        self.assertEqual(base3.id, 1)

    def test_change_id(self):
        """ test to change id """
        base1 = Base(2)
        self.assertEqual(base1.id, 2)
        base1.id = 5
        self.assertEqual(base1.id, 5)

    def test_TypeError(self):
        """ calling class with more than 1 arg """
        with self.assertRaises(TypeError):
            base3 = Base(2, 5)
