class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width
    
square1 = Square(10, 20)
cube1 = Cube(10, 15, 20)

print(f"Area: {square1.area()}")
print(f"Volume: {cube1.volume()}")

    