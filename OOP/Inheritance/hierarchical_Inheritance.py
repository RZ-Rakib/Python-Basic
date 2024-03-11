# Super class
class Animal:
    def __init__(self, name) -> None:
        self.name = name

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
dog_instance = Dog("Jack")
cat_instance = Cat("Musta")

# calliong the speak methods
print(dog_instance.speak())
print(cat_instance.speak())
