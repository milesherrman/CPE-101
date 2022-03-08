# Lab 4
#
# Name: Miles Herrman
# Instructor: Sussan Einakian
# Section: 3

import driver

def letter(row, col):
    if row == 0 or row == 8:
        return 'W'
    elif row > 2 and row < 6 and col > 2 and col < 7:
        return 'W'
    else:
        return 'S'
    
        
if __name__ == '__main__':
	driver.comparePatterns(letter)
