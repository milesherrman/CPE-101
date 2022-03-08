# Lab 8
# Name: Miles Herrman
# Instructor: S. Einakian 
# Section: 3

#for each string, find the GPA and add that to the sum of
# its respective major (EE or CPE)
def calculations(list_name: list, file_name: str) -> None:
    #open new file and crate variables
    std_avg = open(file_name, "w")
    ee_sum = ee_cnt = 0
    cpe_sum = cpe_cnt = 0
    total_sum = total_cnt = 0
    #loop through each string in the list and find GPA
    for line in list_name:
        std_avg.write(line)
        data = line.split()
        gpa = float(data[3])
        total_cnt += 1
        total_sum += gpa
        if "EE" in line:
            ee_cnt += 1
            ee_sum += gpa
        elif "CPE" in line:
            cpe_cnt += 1
            cpe_sum += gpa
    #pass values to calc_avg function to find averages for each 
    ee_avg, cpe_avg, total_avg = calc_avg(ee_cnt, ee_sum, cpe_cnt, cpe_sum, total_cnt, total_sum)
    #print averages in the new file
    std_avg.write("EE Average = %.2f \n" %ee_avg )
    std_avg.write("CPE Average = %.2f \n" %cpe_avg)
    std_avg.write("Total Average = %.2f" %total_avg)
    #close the new file
    std_avg.close()
    
#Purpose: Calculate averages
def calc_avg(ee_cnt: int, ee_sum: float, cpe_cnt: int, cpe_sum: float, total_cnt: int, total_sum: float) -> tuple[float, float, float]:
    ee_avg = ee_sum/ee_cnt
    cpe_avg = cpe_sum/cpe_cnt
    total_avg = total_sum/total_cnt
    return ee_avg, cpe_avg, total_avg

#PurposeL Create a list of text from file and pass it to calculations function
def main() -> None:
    std_info_list = []
    std_info = open("std_info.txt","r")
    for line in std_info:
        std_info_list.append(line)
    std_info.close()    
    calculations(std_info_list, "student_avg.txt")

if __name__ == '__main__':
   main()
