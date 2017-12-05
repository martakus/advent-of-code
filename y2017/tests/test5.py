import unittest
from y2017.day5 import *


class TestDay1(unittest.TestCase):
    def test_part_A(self):
        self.assertEqual(jump_increment('0\n3\n0\n1\n-3\n'), 5)

    def test_part_B(self):
        self.assertEqual(jump_conditional_increment('0\n3\n0\n1\n-3\n'), 10)
