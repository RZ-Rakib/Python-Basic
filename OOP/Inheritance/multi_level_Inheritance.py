# Super class
class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def Speak(self):
        pass # Abstract method, to be overridden in derived classes

# derived sub-super_class
class Feature(Animal):
    def Give_birth(self):
        return f"{self.name} can give birth"
    
# derived class 2
class Dog(Feature): # inherited super class
    def Speak(self):
        return f"{self.name} says Woof!"
    def Guard(self):
        return f"{self.name} can use as a guard"
    
# Derived class 3
class Cat(Feature): # inherited super class
    def Speak(self):
        return f"{self.name} says Meaw!"
    def Sleep(self):
        return f"{self.name} can sleep all day"
    
# creating instance of derived class
dog_instance = Dog("Jack")
cat_instance = Cat("Musta")

# calliong the speak methods
print(dog_instance.Speak())
print(dog_instance.Give_birth())
print(dog_instance.Guard())

print(cat_instance.Speak())
print(cat_instance.Give_birth())
print(cat_instance.Sleep())
