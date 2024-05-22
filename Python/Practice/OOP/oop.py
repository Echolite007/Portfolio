class Student: 
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade 
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, duration):
        self.name = name 
        self.duration = duration
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def get_name(self):
        return self.name    
    def get_duration(self):
        return self.duration
    def get_students(self):
        for student in self.students:
            print(f"Student name: {student.get_name()}")
    def get_average(self):
        value = 0 
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


student1 = Student("Anakin", 19, 100)
student2 = Student("Luke", 21, 85)
student3 = Student("Obi Wan", 35, 70)

print(f"Student Name: {student1.get_name()}")
print(f"Student Age: {student1.get_age()}")
print(f"Student Grade: {student1.get_grade()}")
physics_course = Course("Physics", "12 months")
print(f"Course Name: {physics_course.get_name()}")
print(f"Course Duration: {physics_course.get_duration()}")
physics_course.add_student(student1)
physics_course.add_student(student2)
physics_course.add_student(student3)
physics_course.get_students()
print(f"Average Score ({physics_course.get_name()}): {physics_course.get_average()}")