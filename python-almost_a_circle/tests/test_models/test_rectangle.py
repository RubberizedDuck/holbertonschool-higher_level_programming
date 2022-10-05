#!/usr/bin/python3
""" Contains tests for the Rectangle class """


import unittest
import pycodestyle
import inspect
from io import StringIO
import os
from contextlib import redirect_stdout

from models.rectangle import Rectangle
from models.base import Base


class TestRectangleDocs(unittest.TestCase):
    """ Testing class Rectangle for documentation """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_base_docs(self):
        """ checking for docs """
        module_docs = "models.rectangle".__doc__
        self.assertTrue(len(module_docs) > 1)

        class_docs = Rectangle.__doc__
        self.assertTrue(len(class_docs) > 1)

    def test_pycode_class(self):
        """ Checks pycodestyle for base """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """ Checks pycodestyle for test_base """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.rect_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestRectangle(unittest.TestCase):
    """ Testing class Rectangle """

    @classmethod
    def setUpClass(cls):
        """ setup the attributes for testing """
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(1, 2)
        cls.r2 = Rectangle(3, 6)
        cls.r3 = Rectangle(1, 3, 2, 2, 47)
        cls.r4 = Rectangle(2, 2)

    def test_id(self):
        """ Testing function id """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)

    def test_assign_id(self):
        """ Testing setting function id """

    def test_width(self):
        """ Testing function width """
        self.assertEqual(self.r3.width, 1)
        self.assertEqual(self.r4.width, 2)

    def test_height(self):
        """ Testing function height """
        self.assertEqual(self.r3.height, 3)
        self.assertEqual(self.r4.height, 2)

    def test_x(self):
        """ Testing function x """
        self.assertEqual(self.r3.x, 2)
        self.r3.x = 5
        self.assertEqual(self.r3.x, 5)

    def test_x(self):
        """ Testing function y """
        self.assertEqual(self.r3.y, 2)
        self.r3.y = 7
        self.assertEqual(self.r3.y, 7)

    def test_mandatory_width(self):
        """ Tests that width is a mandatory argument """
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_mandatory_height(self):
        """ Tests that height is a mandatory argument """
        with self.assertRaises(TypeError):
            r = Rectangle(4)

    def test_width_TypeError(self):
        """ Tests non-int types for width """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("1", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(None, 3)

    def test_height_TypeError(self):
        """ Tests non-int types for height """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "1")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(3, None)

    def test_x_TypeError(self):
        """ Tests non-int types for x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "4")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(3, 3, None)

    def test_y_TypeError(self):
        """ Tests non-int types for y """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 3, "7")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(4, 3, 5, None)

    def test_width_ValueError(self):
        """ Test int is > 0 for width """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-2, 4)

    def test_height_ValueError(self):
        """ Test int is > 0 for height """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(4, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(3, -4)

    def test_x_ValueError(self):
        """ Test int is >= 0 for x """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(3, 3, -1)

    def test_y_ValueError(self):
        """ Test int is >= 0 for y """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(3, 3, 2, -2)

    def test_area(self):
        """ Test area method """
        self.assertEqual(self.r1.area(), 2)
        self.assertEqual(self.r2.area(), 18)

    def test_area_args(self):
        """ Testing for too many arguments """
        r1 = Rectangle(3, 4)
        with self.assertRaises(TypeError):
            r = r1.area(1)

    def test_no_args(self):
        """ Tests entering no args to instantiate object """
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_update_method_with_args(self):
        """ Tests the update method with args """
        self.r1.update(55, 8, 9, 10, 11)
        self.assertEqual(self.r1.id, 55)
        self.assertEqual(self.r1.width, 8)
        self.assertEqual(self.r1.height, 9)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 11)

    def test_update_method_kwargs(self):
        """ Tests the udpate method with kwargs """
        self.r1.update(x=10, height=10, id=88, width=5, y=5)
        self.assertEqual(self.r1.id, 88)
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 5)

    def test_str(self):
        """ tests the __str__ method """
        self.r1.x = 5
        self.r1.y = 7
        self.assertEqual(str(self.r1), "[Rectangle] (1) 5/7 - 1/2")
        self.assertEqual(str(self.r3), "[Rectangle] (47) 2/2 - 1/3")

    def test_dictionary(self):
        """ Test to see if to_dictionary works """
        d1 = self.r1.to_dictionary()
        self.assertEqual(
            {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}, d1)
        self.assertTrue(type(d1) is dict)
        self.r1.x = 2
        self.r1.y = 3
        d1 = self.r1.to_dictionary()
        self.assertEqual(
            {"id": 1, "width": 1, "height": 2, "x": 2, "y": 3}, d1)
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

    def test_display_too_many_args(self):
        """Test display with too many args"""
        with self.assertRaises(TypeError):
            self.r1.display(1)

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
