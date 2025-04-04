"""6.	Define a class Mobile to store the details of a Mobile (company, model,price) with
the following methods.
a) set_details()- to set the values to the data attributes
b)display_details()-to display the data attribute values
Create an object of the class and invoke methods.
"""


class Mobile:
    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Company: {self.company}, Model: {self.model}, Price: {self.price}")

m = Mobile()
m.set_details("Samsung", "Galaxy S25", 180000)
m.display_details()