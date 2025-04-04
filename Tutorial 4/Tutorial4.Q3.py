"""3.	Create a class car with attributes model, year and price and a method cost() for displaying the prize.
 Create two instance of the class and call the method for each instance"""

class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print(f"Model: {self.model}, Year: {self.year}, Price: {self.price}")

car1 = Car("Mahindra", 2019, 191209)
car2 = Car("tata", 2022, 7000)
car1.cost()
car2.cost()