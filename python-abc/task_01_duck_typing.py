#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")

if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=6)

    print("--- Circle Info ---")
    shape_info(circle)
    print("\n--- Rectangle Info ---")
    shape_info(rectangle)
