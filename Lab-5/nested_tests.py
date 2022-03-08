# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Miles Herrman   
# Section: 3

import unittest
from nested import *

class TestNested(unittest.TestCase):
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_product(self):	# Tests for product function
      self.assertListAlmostEqual(product([[1,2,3], [5,1,9], [2,2,2]]), [6, 45, 8])
      self.assertListAlmostEqual(product([[1,2,0], [5,2,10]]), [0, 100])
      self.assertListAlmostEqual(product([[2,3,4,1], [1,2], [1,1,19]]), [24, 2, 19])

if __name__ == '__main__':
   unittest.main()