import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def setLength(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width

    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)


def main():
    shape1 = Circle(7)
    print("Shape1 Radius: ", Circle.area(shape1))
    shape2 = Rectangle(5, 10)
    print("Shape2 Area: ", Rectangle.area(shape2))


main()
