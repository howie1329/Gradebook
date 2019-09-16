import sql_student
from Student import Students

def menu():
    print('Welcome to Gradebook')
    print('By:Howard Thomas')
    print('Menu')
    print('1.) Add Student')
    print('2.) Edit Student')
    print('3.) Find Student')
    print('4.) Add Assignments')
    print('5.) Edit Assignments')
    print('6.) Find Assignments')
    print('7.) Exit')
    choice = int(input('What would you like to do? '))
    user_choice_menu(choice)

def user_choice_menu(choice):
    if choice == 1:
        add_student()
        menu()
    elif choice == 2:
        edit_student()
        menu()
    elif choice == 3:
        find_student_menu()
        menu()
    elif choice == 4:
        make_assignment()
        menu()
    elif choice == 5:
        edit_assignment()
        menu()
    elif choice == 6:
        find_assignment()
        menu()
    elif choice == 7:
        print('Exiting Program')
    else:
        print('Wrong input please try again')
        menu()

def find_student_menu():
    print('1.) Find Student by ID Number')
    print('2.) Find Studnet by Class Number')
    choice = input('What would you like to do')
    if choice == '1':
        find_student_id()
    elif choice == '2':
        find_student_class_id()

def add_student():
    id_number = input('What is the students id? ')
    first_name = input('What is the students first name? ')
    last_name = input('What is the students last name? ')
    grade_level = input('What is the students grade level? ')
    class_id = input('What is the class id number? ')
    student = Students(id_number, first_name, last_name, grade_level, class_id)
    sql_student.new_students(student)

def find_student_id():
    id_number = input('What is the studnets id number?')
    result = sql_student.find_students_id(id_number)
    formatted_heading = '{:<2} {:<5} {:<5} {:<2} {:<2}'
    print(formatted_heading.format('ID', 'FirstName', 'LastName', 'GradeLevel', 'Class ID'))
    for row in result:
        print(formatted_heading.format(*row))

def find_student_class_id():
    class_id = input('What is the class id number? ')
    result = sql_student.find_students_class_id(class_id)
    formatted_heading = '{:<2} {:<5} {:<5} {:<2} {:<2}'
    print(formatted_heading.format('ID', 'FirstName', 'LastName', 'GradeLevel', 'Class ID'))
    for row in result:
        print(formatted_heading.format(*row))


def edit_student():   
    pass

def make_assignment():
    pass

def edit_assignment():
    pass

def find_assignment():
    pass

def create_report():
    pass

menu()