""" Unit Testing for Day 2
    Markus Foote, 2017
"""
import unittest
from y2017.day2 import *


class TestDay2(unittest.TestCase):
    def test_part_A(self):
        self.assertEqual(check_sum('5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8'), 18)

    def test_part_B(self):
        self.assertEqual(check_divide('5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5'), 9)
