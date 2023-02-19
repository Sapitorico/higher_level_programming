#!/usr/bin/python3
""" write a test from class base"""
import unittest
from models import Base


class TestBase(unittest.TestCase):
    """ Test class """
    def test_id(self):
        """ test id """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """ test to json string """
        r1 = Base.to_json_string(None)
        self.assertEqual(r1, "[]")
        r2 = Base.to_json_string([])
        self.assertEqual(r2, "[]")
        r3 = Base.to_json_string([{'id': 89}])
        self.assertEqual(r3, '[{"id": 89}]')

    def test_from_json_string(self):
        """ test from json string """
        r1 = Base.from_json_string(None)
        self.assertEqual(r1, [])
        r2 = Base.from_json_string("[]")
        self.assertEqual(r2, [])
        r3 = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(r3, [{'id': 89}])


if __name__ == '__main__':
    unittest.main()
