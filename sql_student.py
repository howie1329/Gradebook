import sqlite3

conn = sqlite3.connect('Student.db')

c = conn.cursor()

try:
    c.execute('CREATE TABLE student(id integer, first text, last text, gradelevel integer, class_id integer)')
except:
    pass

def new_students(student):
    with conn:
        c.execute(" INSERT INTO student VALUES (:id, :first, :last, :gradeLevel, :class_id)", {'id': student.id_number, 'first': student.first, 'last': student.last, 'gradeLevel': student.gradelevel, 'class_id': student.class_id})

def find_students_id(id_number):
    c.execute('SELECT * FROM student WHERE id = :id', {'id': id_number})
    return c.fetchall()

def find_students_class_id(class_id):
    c.execute('SELECT * FROM student WHERE class_id = :class_id', {'class_id': class_id})
    return c.fetchall()

def remove_students(id_number):
    with conn:
        c.execute('DELETE from student WHERE id =:id', {'id': id_number})

