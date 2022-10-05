#!/usr/bin/python3
""" Contains tests for the Square class """


import unittest
import pycodestyle
import inspect
import io
from contextlib import redirect_stdout

from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquareDocs(unittest.TestCase):
    """ Testing class Square for documentation """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.square_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_base_docs(self):
        """ checking for docs """
        module_docs = "models.square".__doc__
        self.assertTrue(len(module_docs) >= 1)

        class_docs = Square.__doc__
        self.assertTrue(len(class_docs) >= 1)

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

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.square_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestSquare(unittest.TestCase):
    """ Testing class Rectangle """

    @classmethod
    def setUpClass(cls):
        """ setup the attributes for testing """
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(6)
        cls.s3 = Square(1, 3, 2, 47)
        cls.s4 = Square(2)

    def test_id(self):
        """ Testing method id """
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)

    def test_width(self):
        """ Testing method width """
        self.assertEqual(self.s3.width, 1)
        self.assertEqual(self.s4.width, 2)

    def test_height(self):
        """ Testing method height """
        self.assertEqual(self.s3.height, 1)
        self.assertEqual(self.s4.height, 2)

    def test_size(self):
        """ Testing size method """
        self.assertEqual(self.s3.size, 1)
        self.assertEqual(self.s4.size, 2)

    def test_x(self):
        """ Testing function x """
        self.assertEqual(self.s3.x, 3)
        self.s3.x = 5
        self.assertEqual(self.s3.x, 5)

    def test_x(self):
        """ Testing function y """
        self.assertEqual(self.s3.y, 2)
        self.s3.y = 7
        self.assertEqual(self.s3.y, 7)

    def test_mandatory_size(self):
        """ Tests that height is a mandatory argument """
        with self.assertRaises(TypeError):
            s = Square()

    def test_size_TypeError(self):
        """ Tests non-int types for size """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("1")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(None)

    def test_x_TypeError(self):
        """ Tests non-int types for x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "4")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(3, None)

    def test_y_TypeError(self):
        """ Tests non-int types for y """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 3, "7")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(4, 3, None)

    def test_size_ValueError(self):
        """ Test int is > 0 for size """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-2)

    def test_x_ValueError(self):
        """ Test int is >= 0 for x """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(3, -1)

    def test_y_ValueError(self):
        """ Test int is >= 0 for y """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(3, 2, -2)

    def test_area(self):
        """ Test area method """
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 36)

    def test_area_args(self):
        """ Testing for too many arguments """
        with self.assertRaises(TypeError):
            s = self.s1.area(1)

    def test_no_args(self):
        """ Tests entering no args to instantiate object """
        with self.assertRaises(TypeError):
            s = Square()

    def test_update_method_with_args(self):
        """ Tests the update method with args """
        self.s1.update(55, 8, 9, 10)
        self.assertEqual(self.s1.id, 55)
        self.assertEqual(self.s1.size, 8)
        self.assertEqual(self.s1.x, 9)
        self.assertEqual(self.s1.y, 10)

    def test_update_method_kwargs(self):
        """ Tests the udpate method with kwargs """
        self.s1.update(x=10, id=88, size=5, y=5)
        self.assertEqual(self.s1.id, 88)
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s1.x, 10)
        self.assertEqual(self.s1.y, 5)

    def test_str(self):
        """ tests the __str__ method """
        self.s1.x = 5
        self.s1.y = 7
        self.assertEqual(str(self.s1), "[Square] (1) 5/7 - 1")
        self.assertEqual(str(self.s3), "[Square] (47) 3/2 - 1")

    def test_dictionary(self):
        """ Test to see if to_dictionary works """
        d1 = self.s1.to_dictionary()
        self.assertEqual(
            {"id": 1, "size": 1, "x": 0, "y": 0}, d1)
        self.assertTrue(type(d1) is dict)
        self.s1.x = 2
        self.s1.y = 3
        d1 = self.s1.to_dictionary()
        self.assertEqual(
            {"id": 1, "size": 1, "x": 2, "y": 3}, d1)
        self.assertTrue(type(d1) is dict)

#    def test_display_without_xy(self):
#        """ Test to see if display method works without x & y """
#        with StringIO() as buf, redirect_stdout(buf):
#            self.r1.display()
#            output = buf.getvalue()
#            self.assertEqual(output, "#\n")
#        with StringIO() as buf, redirect_stdout(buf):
#            self.r2.display()
#            output = buf.getvalue()
#            self.assertEqual(output, ("#" * 4 + "\n") * 5)

#    def test_display_too_many_args(self):
#        """Test display with too many args"""
#        with self.assertRaises(TypeError):
#            self.r1.display(1)

#    def test_xy_display(self):
#        """Test display with x & y"""
#        self.r1.x = 2
#        self.r1.y = 2
#        self.r2.x = 8
#        self.r2.y = 4
#        with StringIO() as buf, redirect_stdout(buf):
#            self.r1.display()
#            output = buf.getvalue()
#            self.assertEqual(output, "\n" * 2 + (" " * 2 + "#\n"))
#        with StringIO() as buf, redirect_stdout(buf):
#            self.r2.display()
#            output = buf.getvalue()
#         self.assertEqual(output, "\n" * 4 + (" " * 8 + "#" * 4 + "\n") * 5)
