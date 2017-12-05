import unittest
from y2017.day3 import *


class TestDay3(unittest.TestCase):
    def test_part_A(self):
        self.assertEqual(spiral_steps(1), 0)
        self.assertEqual(spiral_steps(12), 3)
        self.assertEqual(spiral_steps(23), 2)
        self.assertEqual(spiral_steps(1024), 31)

    def test_part_B(self):
        sequence = [147, 142, 133, 122,  59, 304, 5, 4, 2, 57, 330, 10, 54, 351, 11, 23, 25, 26, 362, 747, 806]
        for s in sequence:
            self.assertEqual(spiral_sum(s - 1), s)
