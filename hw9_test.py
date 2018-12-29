"""

# Kareen Sade id: 30492432
# Curse: Python 

"""
from HW9 import *
import unittest


class test_hw9(unittest.TestCase):
    def test_countDigits(self):
        self.assertEqual(countDigits(32), 2)
        self.assertEqual(countDigits(332), 3)
        self.assertEqual(countDigits(10), 2)
        self.assertEqual(countDigits(100), 3)
        self.assertEqual(countDigits(9), 1)
        self.assertEqual(countDigits(0), 1)

    def test_compString(self):
        self.assertEqual(compString('help', 'Help'), True)
        self.assertEqual(compString('help1', 'Help'), False)
        self.assertEqual(compString('HoLA', 'hola'), True)

    def test_sameVowels(self):
        self.assertEqual(sameVowels('this is is', 'this is nt is'), True)
        self.assertEqual(sameVowels('this is is', 'this is not is'), False)
        self.assertEqual(sameVowels('this is is u t o', 'tuohis is nt is'), True)
if __name__ == '__main__':
    unittest.main()