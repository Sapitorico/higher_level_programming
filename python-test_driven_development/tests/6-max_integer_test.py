#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ unittest for the function def max_integer(list=[]):. """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([6, 2, 3, 4, 5, 1]), 6)
        self.assertEqual(max_integer([1, 2, 3, 6, 5, 4]), 6)

    def test_max_integer_empty(self):
        """ check a list si not empty """
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([None]), None)

    def test_max_float(self):
        """ test max float """
        self.assertEqual(max_integer([1.3, 4.5, 2.0, 5.6]), 5.6)