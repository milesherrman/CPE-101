# CPE 101-01
# LAB 6: Str Function
# Name: Miles Herrman   
# Section: 3

import unittest
from str_funcs import *

class TestStrings(unittest.TestCase):   
    def test_vowel_extractor(self):
       self.assertEqual(vowel_extractor("My name is Miles"), "aeiie")
       self.assertEqual(vowel_extractor("Please help, this is not a drill"), "eaeeiioai")
       self.assertEqual(vowel_extractor("Vowels Are underrAted"), "oeAeueAe")

    def test_str_capitalize(self):
       self.assertEqual(str_capitalize("my name is miles"), "My Name Is Miles")
       self.assertEqual(str_capitalize("  i hope my function works properly"), "  I Hope My Function Works Properly")
       self.assertEqual(str_capitalize("vowels are underrated "), "Vowels Are Underrated ")

    def test_str_rotate(self):
       self.assertEqual(str_rotate("does this thing work"), "qbrf guvf guvat jbex")
       self.assertEqual(str_rotate("test number two"), "grfg ahzore gjb")
       self.assertEqual(str_rotate("pLeaSe giVe me A HuNdReD"), "cYrnFr tvIr zr N UhAqErQ")
       self.assertEqual(str_rotate("aBcDeFgHiJkLmNoPqRsTuVwXyZ"), "nOpQrStUvWxYzAbCdEfGhIjKlM")

    def test_make_substring(self):
       self.assertEqual(make_substring("My name is Miles", 0,7,1), "My name")
       self.assertEqual(make_substring("My name is Miles", 0,15,2), "M aei ie")
       self.assertEqual(make_substring("Does This Function Work?", 5,20,3), "Tsutn")
       
    def test_is_palindrome(self):
       self.assertTrue(is_palindrome("racecar"))
       self.assertFalse(is_palindrome("Miles"))
       self.assertTrue(is_palindrome("anna"))

    def test_count_characters(self):
       self.assertEqual(count_characters("count characters", "c"), 3)
       self.assertEqual(count_characters("count characters", "w"), -1)
       self.assertEqual(count_characters("my name is miles", "i"), 2)
       self.assertEqual(count_characters("my name is miles", " "), 3)
       
       
if __name__ == '__main__':
    unittest.main()