# Lab 4
#
# Name: Miles Herrman
# Instructor: Sussan Einakian
# Section: 3

import driver

def letter(row, col):
    if col <= 9:
        return 'D'
    return 'P'
        
if __name__ == '__main__':
	driver.comparePatterns(letter)
