#!/usr/bin/python3
""" write a test from class rectangle"""
import unittest
from models import Rectangle


class TestRectangle(unittest.TestCase):
    """ test from rectangle """
    def test_id(self):
        """ test id """
        r1 = Rectangle(10, 2, id=1)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10, id=2)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_width(self):
        """ test width """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        with self.assertRaises(TypeError):
            r3 = Rectangle("10", 2)
        with self.assertRaises(ValueError):
            r4 = Rectangle(-10, 2)

    def test_height(self):
        """ test height """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.height, 10)
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, -2)

    def test_x(self):
        """ test x """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)
        r2 = Rectangle(2, 10, 8)
        self.assertEqual(r2.x, 8)
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 2, "8")
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 2, -8)

    def test_y(self):
        """ test y """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 10, 0, 8)
        self.assertEqual(r2.y, 8)
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 2, 0, "8")
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 2, 0, -8)

    """ Test of Rectangle(0, 2) exists """
    def test_rectangle_0_2(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(2, 0)


if __name__ == '__main__':
    unittest.main()
