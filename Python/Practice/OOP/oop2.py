# General class
class Employee:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def get_name(self):
        return "Anonymous"
    
# Child class 
class Manager(Employee): 
    def get_name(self): 
        return self.name
    
# Child class 
class Worker(Employee):
    def get_name(self):
        return self.name
    
# Child class
class Freelancer(Employee):
    pass

manager = Manager("Anakin", 19)
worker = Worker("Obi Wan", 35)
freelancer = Freelancer("Luke Skywalker", 21)

print(f"Worker Name: {worker.get_name()}")
print(f"Manager Name: {manager.get_name()}")
print(f"Freelancer Name: {freelancer.get_name()}")
