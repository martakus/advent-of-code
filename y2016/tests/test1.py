import unittest
from y2016.day1 import *


class TestDay1(unittest.TestCase):
    def test_part_A(self):
        self.assertEqual(day1('R2, L3')[0], 5)
        self.assertEqual(day1('R2, R2, R2')[0], 2)
        self.assertEqual(day1('R5, L5, R5, R3')[0], 12)

    def test_part_B(self):
        self.assertEqual(day1('R8, R4, R4, R8')[1], 4)