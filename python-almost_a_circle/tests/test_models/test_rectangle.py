#!/usr/bin/python3
""" Contains tests for the Rectangle class """


import unittest
import pycodestyle
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleDocs(unittest.TestCase):
    """ Testing class Rectangle for documentation """
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


class TestRectangle(unittest.TestCase):
    """ Testing class Rectangle """

    def test_id(self):
        """ Testing function id """
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 6)
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.id, 7)

    def test_width(self):
        """ Testing function width """
        r3 = Rectangle(1, 2)
        self.assertEqual(r3.width, 1)
        r4 = Rectangle(3, 4)
        self.assertEqual(r4.width, 3)

    def test_height(self):
        """ Testing function height """
        r5 = Rectangle(1, 2)
        self.assertEqual(r5.height, 2)
        r6 = Rectangle(3, 4)
        self.assertEqual(r6.height, 4)

    def test_x(self):
        """ Testing function x """
        r7 = Rectangle(1, 2, 3)
        self.assertEqual(r7.x, 3)
        r8 = Rectangle(3, 4, 5, 6)
        self.assertEqual(r8.x, 5)

    def test_x(self):
        """ Testing function y """
        r9 = Rectangle(1, 2, 3)
        self.assertEqual(r9.y, 0)
        r10 = Rectangle(3, 4, 5, 6)
        self.assertEqual(r10.y, 6)

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
        r11 = Rectangle(5, 5)
        self.assertEqual(r11.area(), 25)
        r12 = Rectangle(3, 2)
        self.assertEqual(r12.area(), 6)

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
        r1 = Rectangle(5, 5, 5, 5, 88)
        r1.update(55, 8, 9, 10, 11)
        self.assertEqual(r1.id, 55)
        self.assertEqual(r1.width, 8)
        self.assertEqual(r1.height, 9)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 11)

    def test_update_method_kwargs(self):
        """ Tests the udpate method with kwargs """
        r1 = Rectangle(5, 5, 5, 5, 88)
        r1.update(x=10, height=10)
        self.assertEqual(r1.id, 88)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 5)
