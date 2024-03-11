#importing Abstract base class(ABC), must have to defined abastractmethods
from abc import ABC, abstractmethod

# Super class
class Animal(ABC): #after defined a class as abstract, it is not allow to create an object
    def __init__(self, name) -> None:
        self.name = name
    
    @abstractmethod # only derived classes can override it
    def speak(self):
        pass # Abstract method, to be overridden in derived classes

# derived class 1
class Dog(Animal): # inherited super class
    def speak(self):
        return f"{self.name} says Woof!"
    
# Derived class 2
class Cat(Animal): # inherited super class
    def speak(self):
        return f"{self.name} says Meaw!"
    
# creating instance of derived class
# Shape class is unable to create an instance due to defined as abstract
dog_instance = Dog("Jack")
cat_instance = Cat("Musta")

# calling the speak methods
print(dog_instance.speak())
print(cat_instance.speak())
