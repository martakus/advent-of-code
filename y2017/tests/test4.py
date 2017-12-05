import unittest
from y2017.day4 import *


class TestDay4(unittest.TestCase):
    def test_part_A(self):
        self.assertEqual(check_passphrase('aa bb cc dd ee'), True)
        self.assertEqual(check_passphrase('aa bb cc dd aa'), False)
        self.assertEqual(check_passphrase('aa bb cc dd aaa'), True)

    def test_part_B(self):
        self.assertEqual(check_anagram_passphrase('abcde fghij'), True)
        self.assertEqual(check_anagram_passphrase('abcde xyz ecdab'), False)
        self.assertEqual(check_anagram_passphrase('a ab abc abd abf abj'), True)
        self.assertEqual(check_anagram_passphrase('iiii oiii ooii oooi oooo'), True)
        self.assertEqual(check_anagram_passphrase('oiii ioii iioi iiio'), False)
