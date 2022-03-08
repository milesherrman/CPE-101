# Lab 4
#
# Name: Miles Herrman
# Instructor: Sussan Einakian
# Section: 3

import driver

def letter(row, col):
    if row < 9:
        if col >= row:
            return 'U'
        return 'B'
    elif row < 12:
        if col < 11:
            return 'B'
        return 'U'
    else:
        if col >= row:
            return 'U'
        return 'B'
        
if __name__ == '__main__':
	driver.comparePatterns(letter)
