import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"{self.p1} <-> {self.p2}"

    def length(self):
        return math.sqrt(math.pow(self.p1.x - self.p2.x, 2) + math.pow(self.p1.y - self.p2.y, 2))

class Account:
    def __init__(self):
        """ creates a new Account object with a balance of 0 and "Mickey Mouse" as customer. """
        self.balance = 0
        self.customer = "Mickey Mouse"

    def deposit(self, amount):
        """ Adds "amount" to the balance"""

        self.balance = self.balance + amount

    def __str__(self):     

        """ Returns a string containing the data in the object."""
        return "%s has a balance of %d" % (self.customer, self.balance)

    def __int__(self):
        return self.balance

class SavingsAccount (Account):  
# syntax above shows that SavingsAccount is a subclass of the superclass Account

   def __init__(self):

        """ creates a new object with an interest rate of 0.05 """

        Account.__init__(self)  # calls the Account constructor to initialize that part of the object
        self.interestRate = 0.05

   def __str__(self):
        """ returns a string representation of the object"""

        return Account.__str__(self) + ", and the interest rate is " + str(self.interestRate)

if __name__ == "__main__":
    # p1 = Point()
    # p2 = Point(0, 1)
    # p3 = Point(0, 17)
    # p4 = Point(-1, -1)

    # l1 = Line(p1, p2)
    # l2 = Line(p1, p3)
    # l3 = Line(p1, p4)
    # print(l1)
    # print(l1.length())
    # print(l2)
    # print(l2.length())
    # print(l3)
    # print(l3.length())
    # print(l3.length() == math.sqrt(2)) # Sqrt(2)

    a = SavingsAccount()
    a.deposit(4500)
    print(int(a))