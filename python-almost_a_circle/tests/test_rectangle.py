#!/usr/bin/python3
""" write a test from class rectangle"""
import unittest
import io, sys
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

    """ Test of Rectangle(0, 2) exists """
    def test_rectangle_0_2(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(2, 0)

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

    def test_area(self):
        """ test area """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_str(self):
        """ test str """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        """ test display """
        r1 = Rectangle(4, 6)
        output = io.StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "####\n####\n####\n####\n####\n####\n")

    """ Test of to_dictionary() in Rectangle exists """
    def test_to_dictionary(self):
        """Test to dictionary."""
        dic = {'y': 62, 'x': 24, 'id': 12, 'width': 2, 'height': 2}
        r1 = Rectangle(2, 2, 24, 62, 12)
        self.assertEqual(r1.to_dictionary(), dic)

    def test_update(self):
        """ test update """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        r1.update(width=1, x=2, y=3, height=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 2/3 - 1/4")


if __name__ == '__main__':
    unittest.main()
