# super class 1
class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def Speak(self):
        pass

# super class 2
class CanFly:
    def fly(self):
        return f"{self.name} can fly"

# super class 3
class CanSwim:
    def swim(self):
        return f"{self.name} can swim"

# derived class 1 inheritaring from multiple base classes
class Bird(Animal, CanFly):
    def Speak(self):
        return f"{self.name} can do chirps"
    
# derived class 2 inheritaring from multiple base classes
class Duck(Animal, CanFly, CanSwim):
    def Speak(self):
        return f"{self.name} can do quacks"

# creating instance of derived classes
bird_instance = Bird("Parrot")
duck_instance = Duck("Duffy")

# calling methods from multiple inherited classes by using object
print(bird_instance.Speak())
print(bird_instance.fly())

print(duck_instance.Speak())
print(duck_instance.fly())
print(duck_instance.swim())