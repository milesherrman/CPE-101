# Lab 8
# Name: Miles Herrman
# Instructor: S. Einakian 
# Section: 3

#Purpose: take a list of strings and print them out with corresponding line # and length
def output(list_name: list) -> None:
    line_num = 0
    for line in list_name:
        line_num += 1
        length = len(line) - 1
        print("Line " + str(line_num) + " (" + str(length) + " chars) : " + line)

#Purpose: Create a list of text from the file and pass it to output function
def main() -> None:
    fin = open("in.txt", "r")
    list_of_lines = []
    for line in fin:
        list_of_lines.append(line)
    fin.close()
    output(list_of_lines)

if __name__ == '__main__':
   main()