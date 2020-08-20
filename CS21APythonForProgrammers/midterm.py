# income = input("What income would you like to know the tax rate for? ")
# income = int(income)
# incomeTaxRate = 0
# if income > 20000 and income <= 30000:
#     incomeTaxRate = .15
# elif income > 30001 and income <= 45000: 
#     incomeTaxRate = .20
# elif income > 45001 and income <= 75000: 
#     incomeTaxRate = .30 
# elif income >= 75001:
#     incomeTaxRate = .4
# print(incomeTaxRate)

# def digits(n):
#     return len(str(n))
# print(digits(11121))

# from random import randrange

# class Die:
#     """
#     One object of this class represnts one die with    6 sides. You can roll the die
#     to come up with a pseudo random value between 1    and 6.
#     """
#     def __init__(self):
#        """
#        Initializes the die to 1.
#        """
#        self.value = 1

#     def __str__(self):
#        """
#        Returns a string representation of the die.
#        """
#        return "This die has value : " + str(self.value)

#     def roll(self):
#        """
#        Rolls the die to come up with a pseudorandom       value between 1 and 6.
#        """
#        self.value = randrange(1,7)

# d1 = Die()
# d2 = Die()
# for i in range(10):
#     d1.roll()
#     d2.roll()
#     print(f"D1: {d1}\nD2: {d2}")

userInput = input ("Please type a real number: ")

try:
    userInput = float(userInput)
except:
    print("You typed a char that isn't appropriate in a real number.")
else:
    print("Thank you for following instructions.")
finally:
    print("I hope you play again.")