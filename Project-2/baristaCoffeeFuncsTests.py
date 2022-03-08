# Function Tests Program
# Project 2: Barista Coffee Assistant
#
# Name: Miles Herrman
# Section: 3
# Date: 1/25/2022
#
from baristaCoffeeFuncs import *
import unittest
class MyTestCase(unittest.TestCase):

    #Function does not take any parameters
    def test_type_prompt(self):
        pass
        
    #Function does not take any parameters
    def test_milk_prompt(self):
        pass

    #Function does not take any parameters
    def test_size_prompt(self):
        pass

    #Function does not take any parameters
    def test_takeout_prompt(self):
        pass

    #Function does not take any parameters
    def test_print_order(self):
        pass

    #Testing the total due function with every possible price outcome
    def test_total_due(self):
        self.assertEqual(total_due("FLAT WHITE", "N", "SMALL"), 2.95)
        self.assertEqual(total_due("FLAT WHITE", "N", "MEDIUM"), 3.00)
        self.assertEqual(total_due("FLAT WHITE", "N", "LARGE"), 3.75)
        self.assertEqual(total_due("LATTE", "N", "SMALL"), 2.85)
        self.assertEqual(total_due("LATTE", "N", "MEDIUM"), 3.75)
        self.assertEqual(total_due("LATTE", "N", "LARGE"), 4.15)
        self.assertEqual(total_due("AMERICANO", "N", "SMALL"), 2.75)
        self.assertEqual(total_due("AMERICANO", "N", "MEDIUM"), 2.95)
        self.assertEqual(total_due("AMERICANO", "N", "LARGE"), 3.25)
        self.assertEqual(total_due("AMERICANO", "Milk on the side", "SMALL"), 3.00)
        self.assertEqual(total_due("AMERICANO", "Milk on the side", "MEDIUM"), 3.20)
        self.assertEqual(total_due("AMERICANO", "Milk on the side", "LARGE"), 3.50)
        self.assertEqual(total_due("ESPRESSO", "", "SMALL"), 2.75)
        self.assertEqual(total_due("ESPRESSO", "", "MEDIUM"), 2.95)
        self.assertEqual(total_due("ESPRESSO", "", "LARGE"), 3.25)
        self.assertEqual(total_due("ESPRESSO", "Milk on the side", "SMALL"), 3.00)
        self.assertEqual(total_due("ESPRESSO", "Milk on the side", "MEDIUM"), 3.20)
        self.assertEqual(total_due("ESPRESSO", "Milk on the side", "LARGE"), 3.50)
  
if __name__ == '__main__':
    unittest.main()