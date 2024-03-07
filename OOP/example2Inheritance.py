# super class
class Shape:
    def __init__(self, dimension1, dimension2) -> None:
        self.dim1 = dimension1
        self.dim2 = dimension2

    def area(self):
        print("This is a default message")

# Triangle_sub class
class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print(f"Area of triangle is{area}")

# rectangle_sub class
class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print(f"Area of rectangle is {area}")

# calling the sub classes
t = Triangle(10, 20) # call the triangle
t.area()

r = Rectangle(20, 30) # call the rectangle
r.area()