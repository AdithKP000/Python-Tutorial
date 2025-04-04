""""2.	Create a class Rectangle .A constructor is used to initialize the object values.
 Member function area() to compute the area of the rectangle """

class r:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def a(self):
        return self.length * self.breadth

rect = r(5, 3)
print("Area of Rectangle:", rect.a())