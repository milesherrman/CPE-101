# This is a header block example for lab 03.

# You will need to supply the following information.

# Name: Miles Herrman
# Section: 3

import unittest
from conditional import *

#You can delete pass after wrinting your code
class TestCases(unittest.TestCase):

   # 3 test cases for the min_of_2 function
   def test_min_of_2(self):
      self.assertEqual(min_of_2(1,2), 1)
      self.assertEqual(min_of_2(10,3), 3)
      self.assertEqual(min_of_2(22,23), 22)

   # 3 test cases for the min_of_3 function
   def test_min_of_3(self):
      self.assertEqual(min_of_3(1,2,3), 1)
      self.assertEqual(min_of_3(15,10,5), 5)
      self.assertEqual(min_of_3(9,3,7), 3)

   # 3 test cases for the rental_late_fee function
   def test_rental_late_fee(self):
      self.assertEqual(rental_late_fee(1), 0)
      self.assertEqual(rental_late_fee(10), 15)
      self.assertEqual(rental_late_fee(30), 100)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

