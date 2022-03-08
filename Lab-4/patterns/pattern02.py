# Lab 4
#
# Name: Miles Herrman
# Instructor: Sussan Einakian
# Section: 3

import driver

def letter(row, col):
    if row < 10:
        if row >= 5 and row <= 7:
            if col >=5 and col <= 10:
                return 'M'
        return 'N'
    else:
        if row >= 13 and row <= 15:
            if col >=5 and col <= 10:
                return 'M'
        return 'Z'
        
if __name__ == '__main__':
	driver.comparePatterns(letter)
