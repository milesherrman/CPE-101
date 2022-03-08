# Lab 4
#
# Name: Miles Herrman
# Instructor: Sussan Einakian
# Section: 3
import driver

def letter(row, col):
    if row % 2 == 0:
        if col < 3:
            return 'L'
        return 'G'
    else:
        if col > 16:
            return 'O'
        return 'G'
        
if __name__ == '__main__':
	driver.comparePatterns(letter)
