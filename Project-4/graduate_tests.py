#Project 4 – Graduate Rate (2017-2018)
# Name: Miles Herrman
# Instructor: Dr. S. Einakian
# Section: 3

# unittest cases for graduate rate will include here
import unittest
from graduate_funcs import *
class TestCases(unittest.TestCase):

    #Test the division class init function
    def test_division_init(self):
        test1 = Division(3210, "Agriculture")
        test2 = Division(3690, "Education")
        self.assertEqual(test1.id, 3210)
        self.assertEqual(test2.id, 3690)
        self.assertEqual(test1.division_name, "Agriculture")
        self.assertEqual(test2.division_name, "Education")

    #Test the division class eq function
    def test_division_eq(self):
        test1 = Division(3210, "Agriculture")
        test2 = Division(3690, "Education")
        test3 = Division(3210, "Agriculture") 
        self.assertNotEqual(test1, test2)
        self.assertNotEqual(test2, test3)
        self.assertEqual(test1, test3)

    #Test the division class repr function
    def test_division_repr(self):
        test1 = Division(3210, "Agriculture")
        test2 = Division(3690, "Education")
        test3 = Division(3490, "Computer") 
        self.assertEqual(test1.__repr__(), 'Division: Agriculture ID: 3210')
        self.assertEqual(test2.__repr__(), 'Division: Education ID: 3690')
        self.assertEqual(test3.__repr__(), 'Division: Computer ID: 3490')

    #Test the graduate class init function
    def test_graduate_init(self):
        test1 = Graduate(3210, "Ag Bus", (1,1), (2,2), (3,3))
        self.assertEqual(test1.id, 3210)
        self.assertEqual(test1.major, "Ag Bus")
        self.assertEqual(test1.bachelor, (1,1))
        self.assertEqual(test1.master, (2,2))
        self.assertEqual(test1.doctor, (3,3))
    
    #Test the graduate class eq function
    def test_graduate_eq(self):
        test1 = Graduate(3210, "Ag Bus", (10,11), (28,43), (39,17))
        test2 = Graduate(3611, "Teacher", (10,11), (24,11), (39,17))
        test3 = Graduate(3812, "Mechanic", (10,11), (28,43), (39,17))
        self.assertNotEqual(test1, test2)
        self.assertNotEqual(test2, test3)
        self.assertEqual(test1, test3)

    #Test the graduate class repr function
    def test_graduate_repr(self):
        test1 = Graduate(3, "Ag", (1,1), (2,2), (3,3))
        test2 = Graduate(3, "Ed", (1,2), (2,2), (3,3))
        test3 = Graduate(3, "Cs", (1,3), (2,2), (3,3))
        self.assertEqual(test1.__repr__(), 'Graduate: 3 Ag (1, 1) (2, 2) (3, 3)')
        self.assertEqual(test2.__repr__(), 'Graduate: 3 Ed (1, 2) (2, 2) (3, 3)')
        self.assertEqual(test3.__repr__(), 'Graduate: 3 Cs (1, 3) (2, 2) (3, 3)')

    #Test the read file function
    def test_read_file(self):
        self.assertEqual(read_file("test1.csv"), ["This is the header", "13, data, data, 12, 12", "72, data, data, 12, 14"])
        self.assertEqual(read_file("test2.csv"), ["This is the header", "This is a second header", "13, data, data, 12, 12", "72, data, data, 12, 14"])
        self.assertEqual(read_file("test3.csv"), [])

    #Test the create division function
    def test_create_division(self):
        self.assertEqual(create_division(read_file("test3.csv")), [])
        self.assertEqual(create_division(read_file("test4.csv")), [Division(3200,"Agriculture operations and related sciences")])
        self.assertEqual(create_division(read_file("test5.csv")), [Division(3400,"Education n stuff")])
       
    #Test the create graduate function
    def test_create_graduate(self):
        self.assertEqual(create_graduate(read_file("test3.csv")), [])
        self.assertEqual(create_graduate(read_file("test4.csv")), [Graduate(3201, "Agriculture general ", (1098, 1096), (181, 120), (3, 11)), Graduate(3202, "Agricultural business and management general", (379,745), (26,40), (1,0)), Graduate(3414, "Computer science     ", (4816, 21497), (3598, 8885), (168, 835))])
        self.assertEqual(create_graduate(read_file("test5.csv")), [Graduate(3202, "Agriculture general ", (1, 1), (0, 0), (0, 0)), Graduate(3602, "Agricultural business and management general", (0,0), (0,0), (0,0)), Graduate(3802, "Computer science     ", (4, 21), (3, 8), (0, 0))])
        
    #Test the find total avg function
    def test_find_total_avg(self):
        self.assertEqual(find_total_avg(create_division(read_file("test3.csv")),create_graduate(read_file("test3.csv"))), [])
        self.assertEqual(find_total_avg(create_division(read_file("test4.csv")),create_graduate(read_file("test4.csv"))), [(3700,1850)])
        self.assertEqual(find_total_avg(create_division(read_file("test5.csv")),create_graduate(read_file("test5.csv"))), [(0,0)])
    
    #Test the find graduate rate function
    def test_find_graduate_rate(self):
        self.assertEqual(find_graduate_rate(Graduate(3603, "Multicultural education  ", (0,2) ,(21,79) ,(4,9))), (90,25))
        self.assertEqual(find_graduate_rate(Graduate(3803, "Computer Science", (1,1) ,(2,2) ,(3,4))), (7,6))
        self.assertEqual(find_graduate_rate(Graduate(3403, "Engineering", (0,0) ,(0,0) ,(0,0))), (0,0))

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
