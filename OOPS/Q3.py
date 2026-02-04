# Create a class called Order which stores item & its price.
# Use Dunder functions __gt__() to convert that:
#  order1 > order2 if price of the order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self, other):
        return self.price > other.price

order1 = Order("Apple", 10)
order2 = Order("Orange", 20)
print(order1 > order2)