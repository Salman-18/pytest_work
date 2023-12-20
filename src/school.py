class TooManyStudents(Exception):
    pass
class ClassRoom():
    def __init__(self, teachers, students, course_title):
        self.teachers = teachers
        self.students = students
        self.course_title = course_title
    

    def add_students(self, student):
        if len(self.students) <= 10:
            self.students.append(student)
        else:
            raise TooManyStudents 
 
                
    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                break

    def change_teachers(self, new_teacher):
        self.teacher = new_teacher


class Person:
    def __init__(self, name):
        self.name = name
        


class Teacher(Person):
    pass

class Student(Person):
    pass

 