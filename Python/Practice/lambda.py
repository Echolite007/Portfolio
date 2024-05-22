# Lambda functions are functions that are written on one line 
# Lambda functions are useful for functions that are intended to be used once

double = lambda x: x *2 
print(double(5))

multiply = lambda x, y: x * y
print(multiply(10, 2))

add = lambda x, y , z: x + y + z
print(add(1,2,3))

full_name = lambda first_name, last_name: f"{first_name} {last_name}"
print(full_name("Aryan", "Sewgobind"))

age_check = lambda age: True if age >= 18 else False
print(age_check(17))
