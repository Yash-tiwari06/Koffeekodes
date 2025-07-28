class Bookstore:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self. quantity = quantity

    def total_value(self):
        return self.price * self.quantity

book1 = Bookstore("The MSD", "Vishnu Sharma", 250000, 2)
book2 = Bookstore("THE landlord", "Arpit Pandey", 15000, 1000)
print(title ,book1.total_value())