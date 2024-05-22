class Prey:
    def flee(self):
        print("Prey is fleeing!")
        return self

class Predator:
    def hunt(self):
        print("Predator is hunting!")
        return self

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator, Prey):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee().hunt()