"""7.	Define a class in Python to store the details of students( rollno, mark1,mark2) with
the following methods
readData()- to assign values to class attributes
computeTotal()-to find the total marks
printDetails()- to print the attribute values and total marks.
Create an object of this class and invoke the methods
"""


class Student:
    def readData(self, rollno, mark1, mark2):
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2

    def computeTotal(self):
        self.total = self.mark1 + self.mark2

    def printDetails(self):
        print(f"Roll No: {self.rollno}, Mark1: {self.mark1}, Mark2: {self.mark2}, Total: {self.total}")

s = Student()
s.readData(14, 45, 31)
s.computeTotal()
s.printDetails()