""" Unit Testing for Day 1
    Markus Foote
    2017

    Call me like this (runs all tests):
        $ python -m unittest discover tests
    from the /2017 directory
    or (only this file's tests):
        $ python -m unittest test1
    from the /tests directory with appropriate PYTHONPATH for the day1 file
"""
import unittest
from y2017.day1 import *


class TestDay1(unittest.TestCase):
    def test_part_A(self):
        self.assertEqual(inverse_captcha('1122'), 3)
        self.assertEqual(inverse_captcha('1111'), 4)
        self.assertEqual(inverse_captcha('1234'), 0)
        self.assertEqual(inverse_captcha('91212129'), 9)

    def test_part_B(self):
        self.assertEqual(inverse_captcha_half('1212'), 6)
        self.assertEqual(inverse_captcha_half('1221'), 0)
        self.assertEqual(inverse_captcha_half('123425'), 4)
        self.assertEqual(inverse_captcha_half('123123'), 12)
        self.assertEqual(inverse_captcha_half('12131415'), 4)
