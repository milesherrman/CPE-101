# CPE 101 Lab 4
# Name: Miles Herrman
# Section: 3

def main():
   table_size = get_table_size()
   while table_size != 0:
      first = get_first()
      increment = get_increment()
      show_table(table_size, first, increment)
      table_size = get_table_size()

# Obtain a valid table size from the user
def get_table_size():
   size = int(input("Enter number of rows in table (0 to end): "))
   while (size) < 0:
      print ("Size must be non-negative.")
      size = int(input("Enter number of rows in table (0 to end): "))
   return size

# Obtain the first table entry from the user 
def get_first():
   first = int(input("Enter the value of the first number in the table: "))
   while first < 0:
      print("First number must be non-negative.")
      first = int(input("Enter the value of the first number in the table: "))
   return first

# Display the table of power5
def show_table(size, first, increment):
   count = 0
   sum = 0
   print ("Number  Power5")
   while count < size:
      power_5 = first ** 5
      print("{0:-3d}{1:}{2:7d}".format(first, "   ", power_5))
      first += increment
      count += 1
      sum += power_5
   print("")
   print("The sum of power5 is:", sum)
   print("")

def get_increment():
   increment = int(input("Enter the increment between rows: "))
   while (increment) < 0:
      print ("Increment must be non-negative.")
      increment = int(input("Enter the increment between rows: "))
   return increment

if __name__ == "__main__":
   main()

