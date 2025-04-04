"""10.	Write Python program to create a class called as Complex and implement __add__( )
 method to add two complex numbers. Display the result by overloading the + Operator."""


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(2, 3)
c2 = Complex(1, 4)
c3 = c1 + c2
print("Sum:", c3)