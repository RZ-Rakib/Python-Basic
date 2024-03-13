# basic example
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Function to demonstrate polymorphism
def make_sound(animal):
    return animal.speak()

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call make_sound function with different instances
print(make_sound(dog))  # Output: Dog barks
print(make_sound(cat))  # Output: Cat meows




# professional example
class Shape:
    def area(self):
        pass  # Abstract method to be overridden

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Function to calculate area of any shape
def calculate_area(shape):
    return shape.area()

# Create instances of Rectangle and Circle
rectangle = Rectangle(5, 4)
circle = Circle(3)

# Call calculate_area function with different instances
print(calculate_area(rectangle))  # Output: 20
print(calculate_area(circle))     # Output: 28.26
