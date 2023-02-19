#!/usr/bin/python3
""" write a test from class Square"""
import unittest
from models import Square


class TestSquare(unittest.TestCase):
    """ tests class """
    def test_square_id(self):
        """ test square id """
        s1 = Square(5)
        self.assertEqual(s1.id, 10)
        s2 = Square(2, 2)
        self.assertEqual(s2.id, 11)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.id, 12)

    def test_square(self):
        """ test square """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
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

    def test_square_y(self):
        """ test square y """
        s1 = Square(5)
        self.assertEqual(s1.y, 0)
        s2 = Square(2, 2)
        self.assertEqual(s2.y, 0)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.y, 3)
        with self.assertRaises(TypeError):
            s4 = Square(5, 2, "3")
        with self.assertRaises(ValueError):
            s5 = Square(5, 2, -3)

    def test_square_area(self):
        """ test square area """
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

    def test_square_display(self):
        """ test square display """
        s1 = Square(4)
        s1.display()
        s2 = Square(2, 2)
        s2.display()
        s3 = Square(3, 1, 3)
        s3.display()

    def test_square_str(self):
        """ test square str """
        s1 = Square(4)
        self.assertEqual(s1.__str__(), "[Square] (18) 0/0 - 4")
        s2 = Square(2, 2)
        self.assertEqual(s2.__str__(), "[Square] (19) 2/0 - 2")
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.__str__(), "[Square] (20) 1/3 - 3")

    def test_square_update(self):
        """ test square update """
        s1 = Square(4)
        s1.update(89)
        self.assertEqual(s1.__str__(), "[Square] (89) 0/0 - 4")
        s1.update(89, 2)
        self.assertEqual(s1.__str__(), "[Square] (89) 0/0 - 2")
        s1.update(89, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/0 - 2")
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/4 - 2")
        s1.update(x=1, size=2, y=3, id=89)
        self.assertEqual(s1.__str__(), "[Square] (89) 1/3 - 2")
        s1.update(size=1, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 1/1 - 1")

    def test_square_to_dictionary(self):
        """ test square to dictionary """
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'x': 2, 'y': 1, 'id': 21, 'size': 10})
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s2.__str__(), "[Square] (21) 2/1 - 10")
        self.assertFalse(s1 is s2)


if __name__ == '__main__':
    unittest.main()
