# Defines and tests the methods and variables of an Order class

from sandwich import Sandwich

# One object of class Order represents a whole Order consisting of multiple Orders to be made at a deli
class Order:
    # Initializes an empty Order object. 
    def __init__(self):
        self.sandwiches = []

    # Adds newSandwich to the Order. The parameter newSandwich must already be a fully initialized Sandwich object.
    def addSandwich(self, newSandwich):
        self.sandwiches.append(newSandwich)

    # Returns the Order as a string
    def __str__(self):
        if len(self.sandwiches) == 0: return "No sandwiches in the order."
        r = ''
        for i in range(len(self.sandwiches)): 
            r += "Sandwich #" + str(i+1) + ": " + str(self.sandwiches[i]) + ("" if i == len(self.sandwiches)-1 else "\n")
        return r

    # Calculates and returns the Order's price as a float
    def price(self):
        price = 0
        for sandwich in self.sandwiches: price += sandwich.price()
        return price

