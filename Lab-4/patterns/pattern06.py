# Lab 4
#
# Name: Miles Herrman
# Instructor: Sussan Einakian
# Section: 3

import driver

def letter(row, col):
    if col == 0 or col == 8 or row == 0 or row == 8:
            return 'C'
    elif col == row or col == 8 - row:
        return 'E'
    return 'O'
    
       
if __name__ == '__main__':
	driver.comparePatterns(letter)
