# 1. Create a Student Management System using Class and Object in Python.
# What to Do
# 1. Create a class named Student.
# 2. Create a constructor __init__() to initialize:
# o Student name
# o Roll number
# o Age
# o Marks of 3 subjects
# 3. Create a display_details() method to display all student information.
# 4. Create a calculate_total() method to calculate the total marks.
# 5. Create a calculate_percentage() method to calculate the percentage.
# 6. Create a check_result() method:
# o Student passes if marks in every subject are 35 or above.
# o Otherwise, display FAIL.
# 7. Create an update_marks() method to update the marks of a selected subject. 
class Student:
    def __init__(self, name, roll_number, age, marks_math, marks_science, marks_english):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.marks_math = marks_math
        self.marks_science = marks_science
        self.marks_english = marks_english
        self.total_marks = 0
        self.percentage = 0
        self.result = " "
        
    def display_details(self):
        print("Student Name : ", self.name)
        print("Roll Number : ", self.roll_number)
        print("Age : ", self.age)
        print("Marks in Math : ", self.marks_math)
        print("Marks in Science : ", self.marks_science)
        print("Marks in English : ", self.marks_english)
        print("Total Marks : ", self.total_marks)
        print("Percentage : ", self.percentage)
        print("Result : ", self.result)
        
    def student_total(self):
        self.total_marks = (self.marks_math + self.marks_science + self.marks_english) 
        
    def student_percentage(self):
        self.percentage = (self.total_marks/300)*100
        
    def student_result(self):
        if(self.marks_math>=35 and 
           self.marks_science>=35 and
           self.marks_english>=35):
            self.result = "PASS"
        else:
            self.result = "FAIL"
            
    def update_marks(self):
        print("Select the Subject : ")
        print("1. Math")
        print("2. Science")
        print("3. English")
        
        choice = int(input("Enter your choice : "))
        
        match choice:
            case 1:
                new_marks = int(input("Enter new math marks : "))
                self.marks_math = new_marks
                print("Marks updated successfully")
            
            case 2:
                new_marks = int(input("Enter new science marks : "))
                self.marks_science = new_marks
                print("Marks updated successfully")
                
            case 3:
                new_marks = int(input("Enter new english marks : "))
                self.marks_english = new_marks
                print("Marks updated successfully")
                
            case _:
                print("Invalid Choice")
               
    
students = {}
    
def add_students():
    name = input("Enter the student name : ")
    roll_no = int(input("Enter the Roll no : "))
        
    if roll_no in students:
        print("Student with these roll no already exists.")
        return
        
    age = int(input("Enter the age of the Student"))
    math = int(input("Enter Math Marks: "))
    science = int(input("Enter Science Marks: "))
    english = int(input("Enter English Marks: "))
    
    student = Student(
        name, roll_no, age,math,science, english
    )
    
    students[roll_no]=student
    
    print("Student added successfully")
    
def display_student():
    roll_number = int(input("Enter the Roll no : "))
    
    if roll_number in students:
        student = students[roll_number]
        
        student.student_total()
        student.student_percentage()
        student.student_result()
        student.display_details()
    else:
        print("Student not found.")
        
def update_student_marks():
    roll_number = int(input("Enter the Roll no : "))
    
    if roll_number in students:
        student = students[roll_number]
        
        student.update_marks()
        student.student_total()
        student.student_percentage()
        student.student_result()
    else:
        print("Student not found.")
        
        
while True:
    print("1. Add Student")
    print("2. Display Student")
    print("3. Update Marks")
    print("4. Exit")
    
    choice = int(input("Enter your choice : "))
    
    match choice:
        case 1:
            add_students()
        
        case 2:
            display_student()
            
        case 3:
            update_student_marks()
            
        case 4:
            print("Thank You")
            break
        
    