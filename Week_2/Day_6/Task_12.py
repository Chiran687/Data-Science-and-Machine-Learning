from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def display_info(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def display_info(self):
        return print(f"radius is {self.radius}")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return (2 * (self.length + self.breadth))

    def display_info(self):
        return print(f"The rectangle of {self.length} & {self.breadth}")


class Triangle(Shape):

    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

    def display_info(self):
        return print(f"The triangle with {self.a}, {self.b}, {self.c}")


if __name__ == "__main__":
    circle = Circle(5)
    print(f"The area of  circle is {circle.area()}")
    print(f"The perimeter of circle is {circle.perimeter()}")
    print(circle.display_info())

    rectangle = Rectangle(10, 20)
    print(f"The area of  circle is {rectangle.area()}")
    print(f"The perimeter of rectangle is {rectangle.perimeter()}")
    print(rectangle.display_info())

    triangle = Triangle(2, 5, 6)
    print(f"The area of  circle is {triangle.area()}")
    print(f"The perimeter of triangle is {triangle.perimeter()}")
    print(triangle.display_info())
