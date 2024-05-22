students = [("John", 10),
            ("Mike", 4),
            ("David", 9),
            ]

grade = lambda data: data[1] > 5

graduates = list(filter(grade, students))

# Print name of graduates 
for graduate in graduates: 
    print(graduate[0])