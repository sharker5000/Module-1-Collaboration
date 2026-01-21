#Robbie Robertson
#GPA Checker (Robbie Robertson)
#This program accepts student names and GPAs and outputs if they have any honors
student_lname = input("Input student's last name or type ZZZ to quit: ")
while student_lname != "ZZZ":
    student_fname = input("Input student's first name: ")
    gpa = float(input("Input student's gpa: "))
    if gpa >= 3.5:
        print(f"{student_fname} {student_lname} is on the Dean's List")
    elif gpa >= 3.25:
        print(f"{student_fname} {student_lname} is on the Honor Roll")
    else:
        print(f"{student_fname} {student_lname} does not qualify for any honors")
    student_lname = input("Input student's last name or type ZZZ to quit: ")
else:
    print("")