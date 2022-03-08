# Lab 4
#
# Name: Miles Herrman
# Instructor: Sussan Einakian
# Section: 3

import driver

def letter(row, col):
    if row == 10:
        return 'B'
    elif (row == 4 or row == 5) and (col >= 10 and col <= 12):
        return 'B'
    elif (row == 6) and (col >= 7 and col <= 12):
        return 'B' 
    elif (row == 2 or row == 3) and (col >= 4 and col <= 9):
        return 'Y' 
    elif (row == 4 or row == 5) and (col >= 4 and col <= 6):
        return 'Y' 
    elif (row == 4 or row == 5) and (col >= 7 and col <= 9):
        return 'X'
    else:
        return 'K'
       
if __name__ == '__main__':
	driver.comparePatterns(letter)
