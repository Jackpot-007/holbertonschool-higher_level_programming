#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract Base Class for animals.
    Defines an abstract method 'sound' that must be implemented by subclasses.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses,
        returning the sound the animal makes.
        """
        pass

class Dog(Animal):
    """
    Concrete subclass of Animal representing a Dog.
    Implements the 'sound' method to return "Bark".
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Concrete subclass of Animal representing a Cat.
    Implements the 'sound' method to return "Meow".
    """
    def sound(self):
        return "Meow"

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    print(f"Dog says: {dog.sound()}")
    print(f"Cat says: {cat.sound()}")

    try:
        abstract_animal = Animal()
    except TypeError as e:
        print(f"Error trying to instantiate Animal: {e}")
