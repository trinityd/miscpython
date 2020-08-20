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
        if(isToasted == True): self.toasted = True
        else: self.toasted = False

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

print("Sandwich 1: ")
s = Sandwich("Bennie")
print (s)
print (s.price())
s.setBread("wheat")
print (s)
print (s.price())
s.setCheese("Cheddar")
print (s)
print (s.price())
s.setMeat("turkey")
print(s)
print (s.price())
s.addCondiment("mayo")
print (s)
print (s.price())
s.addCondiment("mustard")
print (s)
print (s.price())
s.addCondiment("lettuce")
print (s)
print (s.price())
s.setToasted(True)
print (s)
print (s.price())
print("\n")

print("Sandwich 2: ")
s = Sandwich("Jimbo")
print (s)
print (s.price())
s.setBread("sourdough")
print (s)
print (s.price())
s.setCheese("provolone")
print (s)
print (s.price())
s.setMeat("roast beef")
print(s)
print (s.price())
s.addCondiment("BBQ sauce")
print (s)
print (s.price())
s.addCondiment("spit")
print (s)
print (s.price())
s.addCondiment("sweat")
print (s)
print (s.price())
s.addCondiment("blood")
print (s)
print (s.price())
s.addCondiment("tears")
print (s)
print (s.price())
s.setToasted(False)
print (s)
print (s.price())
print("\n")

print("Sandwich 3: ")
s = Sandwich("Jess")
print (s)
print (s.price())
s.setBread("hotdog bun")
print (s)
print (s.price())
s.setMeat("turkey")
print(s)
print (s.price())
s.addCondiment("mayo")
print (s)
print (s.price())
s.addCondiment("mustard")
print (s)
print (s.price())
s.addCondiment("sauerkraut")
print (s)
print (s.price())
s.addCondiment("more sauerkraut")
print (s)
print (s.price())
s.addCondiment("yet more sauerkraut")
print (s)
print (s.price())
s.addCondiment("a squeeze of lemon")
print (s)
print (s.price())
s.setToasted(True)
print (s)
print (s.price())

""" A RECORDING OF THE RUN
Sandwich 1: 
Bennie: not toasted
4.5
Bennie: wheat, not toasted
4.5
Bennie: wheat, Cheddar, not toasted        
4.5
Bennie: wheat, Cheddar, turkey, not toasted
5.5
Bennie: wheat, Cheddar, turkey, ['mayo'], not toasted
5.5
Bennie: wheat, Cheddar, turkey, ['mayo', 'mustard'], not toasted
6.0
Bennie: wheat, Cheddar, turkey, ['mayo', 'mustard', 'lettuce'], not toasted      
6.5
Bennie: wheat, Cheddar, turkey, ['mayo', 'mustard', 'lettuce'], toasted
6.5


Sandwich 2:
Jimbo: not toasted
4.5
Jimbo: sourdough, not toasted
4.5
Jimbo: sourdough, provolone, not toasted
4.5
Jimbo: sourdough, provolone, roast beef, not toasted
5.5
Jimbo: sourdough, provolone, roast beef, ['BBQ sauce'], not toasted
5.5
Jimbo: sourdough, provolone, roast beef, ['BBQ sauce', 'spit'], not toasted      
6.0
Jimbo: sourdough, provolone, roast beef, ['BBQ sauce', 'spit', 'sweat'], not toasted
6.5
Jimbo: sourdough, provolone, roast beef, ['BBQ sauce', 'spit', 'sweat', 'blood'], not toasted
7.0
Jimbo: sourdough, provolone, roast beef, ['BBQ sauce', 'spit', 'sweat', 'blood', 
'tears'], not toasted
7.5
Jimbo: sourdough, provolone, roast beef, ['BBQ sauce', 'spit', 'sweat', 'blood', 
'tears'], not toasted
7.5


Sandwich 3:
Jess: not toasted
4.5
Jess: hotdog bun, not toasted
4.5
Jess: hotdog bun, turkey, not toasted
5.5
Jess: hotdog bun, turkey, ['mayo'], not toasted
5.5
Jess: hotdog bun, turkey, ['mayo', 'mustard'], not toasted
6.0
Jess: hotdog bun, turkey, ['mayo', 'mustard', 'sauerkraut'], not toasted
6.5
Jess: hotdog bun, turkey, ['mayo', 'mustard', 'sauerkraut', 'more sauerkraut'], not toasted
7.0
Jess: hotdog bun, turkey, ['mayo', 'mustard', 'sauerkraut', 'more sauerkraut', 'yet more sauerkraut'], not toasted
7.5
Jess: hotdog bun, turkey, ['mayo', 'mustard', 'sauerkraut', 'more sauerkraut', 'yet more sauerkraut', 'a squeeze of lemon'], not toasted
8.0
Jess: hotdog bun, turkey, ['mayo', 'mustard', 'sauerkraut', 'more sauerkraut', 'yet more sauerkraut', 'a squeeze of lemon'], toasted
8.0
"""