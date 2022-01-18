'''
 Test cases example for lab 01.

 Name: Miles Herrman
 Section: 3
'''

import unittest

class TestsLab1(unittest.TestCase):
   def test_expressions(self):
      self.assertEqual(2 + 3, 5)
      self.assertEqual(2 * 3, 6)
      self.assertEqual(2 ** 3, 8)
      self.assertEqual(49 // 3, 16)
      self.assertAlmostEqual(49 / 3, 16.33333333332)
      self.assertAlmostEqual(49 / 3.0, 16.3333333332)
      self.assertEqual(49 % 3, 1)
      self.assertEqual(7 * 2 + 29 // 3 - 2, 21)
      self.assertEqual(7 * (2 + 29) // 3 - 2, 70)

if __name__ == '__main__':
   unittest.main()
