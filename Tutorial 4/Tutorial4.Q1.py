""""1.	Create class Arith to do arithmetic operation. It contains a member function read()
 to read the two numbers and add() method to find the sum.
 You can add more methods to the class to incorporate more functionality."""

class Arith:
    def readline(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

name = Arith()
name.readline(10, 20)
print("Sum:", name.add())