class Person: 
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.number_of_people += 1
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people
    
person1 = Person("Aryan", 17)
person2 = Person("Anakin", 17)
person3 = Person("Luke", 17)
person4 = Person("Obi Wan", 17)
person5 = Person("Yoda", 17)

print(f"Number of people: {Person.get_number_of_people()}")