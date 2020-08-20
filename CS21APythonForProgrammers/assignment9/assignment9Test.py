""" Tests the Sandwich and Order classes """

""" Imports Sandwich and Order """
from sandwich import Sandwich
from order import Order

""" Imports json library to make extra credit easier """
import json

def saveOrderAsTextFile(order, filename):
    txtfile = open(filename, "w")
    for sandwich in order.sandwiches:
        txtfile.write(str(sandwich.__dict__).replace("\'", "\"").replace(": None", ": null").replace(": True", ": 1").replace(": False", ": 0") + '\n')
    txtfile.close()

def loadOrderFromTextFile(filename):
    order = Order()
    txtfile = open(filename, 'r')
    sandwichstrings = txtfile.readlines()
    for sandwichstring in sandwichstrings:
        sandwichstring = sandwichstring[0:-1]
        print(sandwichstring)
        sandwichvars = json.loads(sandwichstring)
        sandwich = Sandwich(sandwichvars['name'])
        if(sandwichvars['bread'] != None): sandwich.setBread(sandwichvars['bread'])
        if(sandwichvars['cheese'] != None): sandwich.setCheese(sandwichvars['cheese'])
        if(sandwichvars['meat'] != None): sandwich.setMeat(sandwichvars['meat'])
        if(sandwichvars['condiments'] != None): 
            for condiment in sandwichvars['condiments']:
                sandwich.addCondiment(condiment)
        if(sandwichvars['toasted'] != None): sandwich.setToasted(sandwichvars['toasted'])
        order.addSandwich(sandwich)
    return order

if __name__ == "__main__":
    s1 = Sandwich("Joe")
    s1.setMeat("steak")
    s1.addCondiment("Lettuce")
    print (s1)

    s2 = Sandwich("Mary")
    s2.setCheese("cheddar")
    s2.addCondiment("Mayo")
    print (s2)

    print("Order 1:")
    order = Order()
    print(order)
    order.addSandwich(s1)
    print (order)
    print ("Total Price:"+ str(order.price()))
    order.addSandwich(s2)
    print (order)
    print ("Total Price:" + str(order.price()))

    s3 = Sandwich("Gary")
    s3.setBread("Sourdough")
    s3.addCondiment("Horseradish")
    s3.setToasted(True)
    print("Order 2:")
    order2 = Order()
    order2.addSandwich(s1)
    order2.addSandwich(s2)
    order2.addSandwich(s3)
    print(order2)
    print("Order 1:")
    print(order)
    

    print("\nExtra Credit Option 2 Save/Load From Text:")
    saveOrderAsTextFile(order2, "order.txt")
    order3 = loadOrderFromTextFile("order.txt")
    print(order3)
 
"""
Test Run:

Joe: steak, ['Lettuce'], not toasted
Mary: cheddar, ['Mayo'], not toasted
Order 1:
No sandwiches in the order.
Sandwich #1: Joe: steak, ['Lettuce'], not toasted
Total Price:5.5
Sandwich #1: Joe: steak, ['Lettuce'], not toasted
Sandwich #2: Mary: cheddar, ['Mayo'], not toasted
Total Price:10.0
Order 2:
Sandwich #1: Joe: steak, ['Lettuce'], not toasted
Sandwich #2: Mary: cheddar, ['Mayo'], not toasted
Sandwich #3: Gary: Sourdough, ['Horseradish'], toasted
Order 1:
Sandwich #1: Joe: steak, ['Lettuce'], not toasted
Sandwich #2: Mary: cheddar, ['Mayo'], not toasted

Extra Credit Option 2 Save/Load From Text:
{"name": "Joe", "bread": null, "cheese": null, "meat": "steak", "condiments": ["Lettuce"], "toasted": null}
{"name": "Mary", "bread": null, "cheese": "cheddar", "meat": null, "condiments": ["Mayo"], "toasted": null}
{"name": "Gary", "bread": "Sourdough", "cheese": null, "meat": null, "condiments": ["Horseradish"], "toasted": 1}
Sandwich #1: Joe: steak, ['Lettuce'], not toasted
Sandwich #2: Mary: cheddar, ['Mayo'], not toasted
Sandwich #3: Gary: Sourdough, ['Horseradish'], toasted

"""