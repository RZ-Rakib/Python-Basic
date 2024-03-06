class Triangle:
    base = ""
    height = ""

    def __init__(self, nBase, nHeight):
        self.base = nBase
        self.height = nHeight

    def area(self):
        area = 0.5 * self.base * self.height
        print(f"Area of triangle is {area}")

t1 = Triangle(10, 20)
t1.area()

t2 = Triangle(20, 30)
t2.area()