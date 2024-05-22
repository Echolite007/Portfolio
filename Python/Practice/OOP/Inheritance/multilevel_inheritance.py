# Parent class
class Organism: 
    alive = True 

# Parent class which inherits from Organism
class Animal(Organism):
    
    def eating(self):
        print("This animal is eating")

# Child class class which inherits from Animal class which itself inherits from Organism class
class Dog(Animal):

    def bark(self):
        print("Woof!")

boya = Dog()

boya.eating()
boya.bark()