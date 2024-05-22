from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("Car is accelerating!")

    def stop(self):
        print("Car is stopping!")

class Motorcycle(Vehicle):

    def go(self):
        print("Motorcycle is accelerating!")

    def stop(self):
        print("Motorcycle is stopping!")


car1 = Car()
motorcycle1 = Motorcycle()

car1.go()
motorcycle1.go()
car1.stop()
motorcycle1.stop()