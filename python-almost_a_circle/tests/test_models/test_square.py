#!/usr/bin/python3
""" Contains tests for the Square class """


import unittest
import pycodestyle
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquareDocs(unittest.TestCase):
    """ Testing class Square for documentation """
    def test_base_docs(self):
        """ checking for docs """
        module_docs = "models.square".__doc__
        self.assertTrue(len(module_docs) > 1)

        class_docs = Square.__doc__
        self.assertTrue(len(class_docs) > 1)

    def test_pycode_class(self):
        """ Checks pycodestyle for base """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """ Checks pycodestyle for test_base """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
