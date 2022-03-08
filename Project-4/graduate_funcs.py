# Project 4 – Graduate Rate (2017-2018)
# Name: Miles Herrman
# Instructor: Dr. S. Einakian
# Section: 3

# classes and functionalities will be provided here

# class Division
from pydoc import doc

class Division:
    def __init__(self, id, division_name):
        self.id = id
        self.division_name = division_name
    def __eq__(self,other):
        return type(self) == type(other) == Division and \
            self.id == other.id and \
                self.division_name == other.division_name
    def __repr__(self) -> str:
        return "Division: " + str(self.division_name) + " ID: " + str(self.id)

# class Graduate:
class Graduate:
    def __init__(self, id, major, bachelor, master, doctor):
        self.id = id
        self.major = major
        self.bachelor = bachelor
        self.master = master
        self.doctor = doctor

    def __eq__(self, other) -> bool:
        return type(self) == type(other) == Graduate and \
            self.bachelor == other.bachelor and \
                self.master == other.master and \
                    self.doctor == other.doctor

    def __repr__(self) -> str:
        return "Graduate: " + str(self.id) + " " + str(self.major) + " " + str(self.bachelor) + " " +str(self.master) + " " + str(self.doctor) 

# read file and return list of strings
def read_file(csv_file: str) -> list:
    list_of_data = []
    header_and_data = open(csv_file, "r")
    for line in header_and_data:
        list_of_data.append(line.strip())
    header_and_data.close()
    return list_of_data

# create list of Division objects
def create_division(list_of_data: list) -> list:
    list_by_division = []
    data = list_of_data[3:]
    for line in data:
        current_major = line.split(",")
        id = int(current_major[0])
        if id % 100 == 0:
            division_name = current_major[1]
            list_by_division.append(Division(id, division_name))
    return list_by_division

# create list of Graduate objects
def create_graduate(list_of_data: list) -> list:
    list_by_graduate = []
    data = list_of_data[3:]
    for line in data:
        current_major = line.split(",")
        id = int(current_major[0])
        if id % 100 != 0:
            major = current_major[1]
            bachelor = (int(current_major[3]),int(current_major[2]))
            master = (int(current_major[5]),int(current_major[4]))
            doctor = (int(current_major[7]),int(current_major[6]))
            list_by_graduate.append(Graduate(id,major,bachelor,master,doctor))
    return list_by_graduate

# create files for each division
def create_files(list_by_graduate: list):
    list_of_divisions = [Division(3200, "agriculture"), Division(3400, "computer"), Division(3600, "education"),Division(3800, "engineering")]
    for div in list_of_divisions:
        csv = div.division_name + ".csv"
        current_file = open(csv, "w")
        current_file.write("This table shows Bachelor's, master's, and doctor's degrees conferred by postsecondary institutions, of student and discipline division: 2017-18 \n")
        current_file.write("ID, Major, Bachelor, Master, Doctor \n")
        for item in list_by_graduate:
            if item.id//100 == div.id/100:
                current_file.write(str(item.id) + " " + item.major + "," + str(sum(item.bachelor)) + "," + str(sum(item.master)) + "," + str(sum(item.doctor)) + '\n')
        current_file.close()

# find total and average graduate for every division
def find_total_avg(list_by_division: list, list_by_graduate: list) -> list:

    list_of_tot_and_avg = []

    for div in list_by_division:
        div_total = div_cnt = 0
        for grad in list_by_graduate:
            if grad.id//100 == div.id/100:
                div_cnt += 1
                div_total += (sum(grad.bachelor) + sum(grad.master) + sum(grad.doctor))
        if div_cnt != 0:
            list_of_tot_and_avg.append((div_total, round(div_total/div_cnt, 2)))
        else:
            list_of_tot_and_avg.append((div_total, 0))
        
    return list_of_tot_and_avg
                
# find (female, male) graduate rate for given major
def find_graduate_rate(Graduate):
    male_grad = Graduate.bachelor[0] + Graduate.master[0] + Graduate.doctor[0]
    female_grad = Graduate.bachelor[1] + Graduate.master[1] + Graduate.doctor[1]
    return female_grad, male_grad

#Print total grads for computer related majors
def total_comp_grad(list_by_graduate: list) -> int:
    total = 0
    for grad in list_by_graduate:
        if grad.id//100 == 34:
            total += (sum(grad.bachelor) + sum(grad.master) + sum(grad.doctor))
    print("Total of Processed Gradute in Computer and Information Sciences and Support: " + str(total))
    return total

#Print average grads by male/female for computer related majors
def avg_comp_grad(list_by_graduate: list):
    total_male = 0
    total_female = 0
    count = 0
    for grad in list_by_graduate:
        if grad.id//100 == 34:
            count += 1
            current = find_graduate_rate(grad)
            total_female += current[0]
            total_male += current[1]
    print("Average of Processed Male in Computer and Information Sciences and Support: %.2f" %(total_male/count))
    print("Average of Processed Female in Computer and Information Sciences and Support: %.2f" %(total_female/count))

#Print total graduates by gender across all majors
def total_grads(list_by_graduate: list) -> int:
    total_male = 0
    total_female = 0
    for grad in list_by_graduate:
        current = find_graduate_rate(grad)
        total_female += current[0]
        total_male += current[1]
    
    print("Total of all Males in all Majors: %.0f" %total_male)
    print("Total of all Females in all Majors: %.0f" %total_female)
    return total_male + total_female