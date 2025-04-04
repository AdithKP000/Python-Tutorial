"""8.	Define a class in Python to store the details of book( title,author,cost) with the
following methods
get_details()- to assign values to class attributes
print_details()- to display the attribute values
Create an object of this class and invoke the methods
"""


class Book:
    def get_details(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def print_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Cost: {self.cost}")

b = Book()
b.get_details("Wings of Fire", "APJ Abdul Kalam", 350)
b.print_details()