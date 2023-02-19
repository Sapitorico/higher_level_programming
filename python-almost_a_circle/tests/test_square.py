#!/usr/bin/python3
""" write a test from class square"""
import unittest
import io
import sys
import os
from models import Square


class TestSquare(unittest.TestCase):
    """ test """
    def test_id(self):
        """ test id """
        s1 = Square(10, id=1)
        self.assertEqual(s1.id, 1)
        s2 = Square(2, id=2)
        self.assertEqual(s2.id, 2)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.id, 12)
        s4 = Square(10, id=0)
        self.assertEqual(s4.id, 0)
        s5 = Square(10, id=-1)
        self.assertEqual(s5.id, -1)
        s6 = Square(10, id=1.5)
        self.assertEqual(s6.id, 1.5)
        s7 = Square(10, id="1")
        self.assertEqual(s7.id, "1")
        s8 = Square(10, id=[1, 2, 3])
        self.assertEqual(s8.id, [1, 2, 3])
        s9 = Square(10, id=(1, 2, 3))
        self.assertEqual(s9.id, (1, 2, 3))
        s10 = Square(10, id={1, 2, 3})
        self.assertEqual(s10.id, {1, 2, 3})
        s11 = Square(10, id={"a": 1, "b": 2})
        self.assertEqual(s11.id, {"a": 1, "b": 2})
        s12 = Square(10, id=True)
        self.assertEqual(s12.id, True)

    def test_square(self):
        """ test square """
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        s2 = Square(2, 2)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)
        """Test of Square(0) exists """
        with self.assertRaises(ValueError):
            s4 = Square(0)
        """Test of Square(-1) exists """
        with self.assertRaises(ValueError):
            s5 = Square(-1)
        """Test of Square(1, -1, 0, 0) exists """
        with self.assertRaises(ValueError):
            s7 = Square(1, -1, 0, 0)
        """Test of Square(1, 0, -1, 0) exists """
        with self.assertRaises(ValueError):
            s8 = Square(1, 0, -1, 0)

    def test_square_size(self):
        """ test square size """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s2 = Square(2, 2)
        self.assertEqual(s2.size, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.size, 3)
        with self.assertRaises(TypeError):
            s4 = Square("5")
        with self.assertRaises(ValueError):
            s5 = Square(-5)

    def test_square_x(self):
        """ test square x """
        s1 = Square(5)
        self.assertEqual(s1.x, 0)
        s2 = Square(2, 2)
        self.assertEqual(s2.x, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.x, 1)
        with self.assertRaises(TypeError):
            s4 = Square(5, "2")
        with self.assertRaises(ValueError):
            s5 = Square(5, -2)

    def test_str(self):
        """ test str """
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")

    """ Test of to_dictionary() in Square exists """
    def test_to_dictionary(self):
        """ test to dictionary """
        s1 = Square(10, 2, 1, 9)
        self.assertEqual
        (s1.to_dictionary(), {'x': 2, 'y': 1, 'id': 9, 'size': 10})

    """ Test of update() in Square exists """
    def test_update(self):
        """ test update """
        s1 = Square(10, 10, 10, 10)
        s1.update(89)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 10")
        s1.update(89, 2)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 2")
        s1.update(89, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/10 - 2")
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/4 - 2")
        s1.update(x=1, size=2, y=3, id=89)
        self.assertEqual(s1.__str__(), "[Square] (89) 1/3 - 2")
        s1.update(size=1, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 1/1 - 1")
        s1 = Square(10, 10, 10, 10)
        s1.update(size=1)
        self.assertEqual(s1.__str__(), "[Square] (10) 10/10 - 1")
        s1.update(size=1, x=2)
        self.assertEqual(s1.__str__(), "[Square] (10) 2/10 - 1")
        s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/1 - 2")
        s1.update(x=1, size=2, y=3, id=89)
        self.assertEqual(s1.__str__(), "[Square] (89) 1/3 - 2")


if __name__ == '__main__':
    unittest.main()
