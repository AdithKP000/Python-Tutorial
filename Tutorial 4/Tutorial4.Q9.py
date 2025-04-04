
"""9.	How can a class be instantiated in Python? Write a Python program to express the
instances as return values to define a class RECTANGLE with parameters height, width, corner_x, and corner_y and member functions to find center, area, and
perimeter of an instance.
"""

class RECTANGLE:
    def __init__(self, height, width, corner_x, corner_y):
        self.height = height
        self.width = width
        self.corner_x = corner_x
        self.corner_y = corner_y

    def center(self):
        center_x = self.corner_x + self.width / 2
        center_y = self.corner_y + self.height / 2
        return (center_x, center_y)

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

r = RECTANGLE(10, 20, 0, 0)
print("Center:", r.center())
print("Area:", r.area())
print("Perimeter:", r.perimeter())