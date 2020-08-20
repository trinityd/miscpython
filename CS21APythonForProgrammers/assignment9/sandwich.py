# Defines and tests the methods and variables of a Sandwich class

# One object of this class represents a Sandwich with 6 variables, name, bread, cheese, meat, condiments, and toasted value
class Sandwich:
    # Initializes the Sandwich by defining its variables
    def __init__(self, name):
        self.name = name
        self.bread = None
        self.cheese = None
        self.meat = None
        self.condiments = None
        self.toasted = None

    # Setter for bread string variable
    def setBread(self, breadName):
        self.bread = breadName

    # Setter for cheese string variable
    def setCheese(self, cheeseName):
        self.cheese = cheeseName

    # Setter for meat string variable
    def setMeat(self, meatName):
        self.meat = meatName

    # Adder for condiment list variable
    def addCondiment(self, additionalCondiment):
        if self.condiments == None: self.condiments = []
        self.condiments.append(additionalCondiment)

    # Setter for toasted boolean variable
    def setToasted(self, isToasted):
        self.toasted = bool(isToasted)

    # Returns the Sandwich as a string
    def __str__(self):
        r = self.name + ": "
        if self.bread != None: r += self.bread + ", "
        if self.cheese != None: r += self.cheese + ", "
        if self.meat != None: r += self.meat + ", "
        if self.condiments != None: r += str(self.condiments) + ", "
        r += ("" if self.toasted == True else "not ") + "toasted"
        return r

    # Calculates and returns the Sandwich's price as a float
    def price(self):
        price = 4.5
        if self.meat != None: price += 1
        if self.condiments != None and len(self.condiments) > 1:
            price += (len(self.condiments) - 1) * .5
        return price
