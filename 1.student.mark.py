students = []
courses = []
marks = {}

#Take information of students
def student_info(n):
    for student in range(n):
        students.append({"ID of student:":input("ID student: "),"Name of student:":input("Name student: "),"Birthday:":input("Birthday: ")})

#Take information of courses
def courses_info(c):
    for course in range(c):
        courses.append({int(input("ID of course: ")):input("Name of course: ")})

#Take marks follow course and student
def marks_info():
    for course in courses:
        for i in course:
            print(i,"-",course[i])
            marks[course[i]]={}
            for student in students:
                print(student["ID of student:"])
                marks[course[i]][student["Name of student:"]] = float(input("Mark: "))

#Print list students, courses or marks of a course
def print_info():
    print("1. List students information: \n2. List courses: \n3. List marks of course:")
    choice = int(input("Choose number from 1 to 3: "))
    if (choice == 1):
        print("\nInformation of student:")
        for student in students:
            print("\n")
            for i in student:
                print(i+student[i])
        print("------------")
        print_info()
    elif (choice == 2):
        print("Information of course:")
        for course in courses:
            for i in course:
                print("\n","ID:",i,"\n","Name course:",course[i])
        print("------------")
        print_info()
    elif (choice == 3):
        x = input("Enter course you want to know mark: ")
        for nameC, mark in marks.items():
            if (nameC == x):
                print(nameC)
                for key in mark:
                    print("   -" + key + ":",mark[key])
                break
            else:
                print("Don't have this course.")
                break
        print("------------")
        print_info()
    else:
        print("Wrong input, choose number from 1 to 3.")
        print_info()
    
#Main code
n = int(input("Number of students in class: "))
student_info(n)
print("------------\n")

c = int(input("The number of courses: "))
courses_info(c)
print("------------\n")

marks_info()
print("------------\n")

print_info()
