# Project 3 - Tic-Tac-Toe Simulator
# Name: Miles Herrman
# Instructor: S. Einakian 
# Section: 3

import unittest
from tictactoeFuncs import *

class TestCases(unittest.TestCase):

#Test check_rows function
   def test_check_rows(self):
      self.assertTrue(check_rows(["X","X","X","","","","","",""]))
      self.assertTrue(check_rows(["","","","X","X","X","","",""]))
      self.assertTrue(check_rows(["","","","","","","X","X","X"]))
      self.assertFalse(check_rows(["","O","","X","O","","","O",""]))

#Test check_cols function
   def test_check_cols(self):
      self.assertTrue(check_cols(["X","","","X","","","X","",""]))
      self.assertTrue(check_cols(["","X","","","X","","","X",""]))
      self.assertTrue(check_cols(["","","X","","","X","","","X"]))
      self.assertFalse(check_cols(["","O","","X","","X","","O",""]))

#Test check_diags function
   def test_check_diags(self):
      self.assertTrue(check_diags(["X","","","","X","","","","X"]))
      self.assertTrue(check_diags(["","","O","","O","","O","",""]))
      self.assertFalse(check_diags(["","O","O","","O","","","X","X"]))

#Test board_full function
   def test_board_full(self):
      self.assertTrue(board_full(["X","O","X","X","O","X","O","X","O"]))
      self.assertTrue(board_full(["O","X","O","O","X","O","X","O","X"]))
      self.assertFalse(board_full(["","O","O","","O","","","X","X"]))

#Test check_win function (full board w/ no winners return true, but prints a tie)
   def test_check_win(self):
      self.assertTrue(check_win(["X","O","X","O","X","O","X","",""], "X"))
      self.assertTrue(check_win(["O","X","O","O","X","O","X","O","X"], "X"))
      self.assertFalse(check_win(["","O","O","","O","","","X","X"], "X"))

if __name__ == '__main__':
   unittest.main()