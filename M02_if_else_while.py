"""
Name: Carlos Lizarazu Linares
File name: M02_if_else_while
This app will get information from the student such as name, last name, and GPA. 
Next, the program will select students that that qualife for the Dean's list or Honor Roll.
"""
lastname = input("Enter the student lastname, 'ZZZ' to quit: ")
#we are asking if the lastname is different than ZZZ to quit the redords or continue
while lastname != "ZZZ":
    fname = input("Enter the student name: ")
    gpa = float(input("Enter the student gpa: "))
    
    #we will evaluate if student made it into the dean's list or honor list
    if gpa >= 3.5:
        print("Student has made the Dean's List")
    elif gpa >= 3.25 and gpa < 3.5:
        print("The student has made the honor Roll")
    break
