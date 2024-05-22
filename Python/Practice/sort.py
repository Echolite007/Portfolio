students = [("John", 10),
            ("Mike", 7),
            ("David", 9),
            ]

grade = lambda grades: grades[1]
students.sort(key=grade, reverse=True)
# Show name in order of highest to lowest grade 
for student in students:
    print(student[0])