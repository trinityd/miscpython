"""
	Defines class Manager, which inherits from Employee and tests it
    One object of this class represents one manager's first and last name, SSN, salary, title, and annual bonus.
"""

""" Imports Employee """
from employee import Employee

class Manager(Employee):
    """ 
        One object of this class stores one manager's first and last name, SSN (as string, to account for xxx-xx-xxxx or xxxxxxxxx), and salary (as float), title, and annual bonus (as float)
        No writing to shell
        No reading to shell
    """
    def __init__(self, firstName, lastName, SSN, salary, title, annualBonus):
        Employee.__init__(self, firstName, lastName, SSN, salary) # calls the Employee constructor to initialize that part of the object
        self.title = title
        self.annualBonus = float(annualBonus)

    """
        Returns a sentence that tells the managers's first and last name, SSN, salary, title, and annual bonus.
        No writing to shell
        No reading to shell
    """
    def __str__(self):
        return Employee.__str__(self) + f" Title: {self.SSN} Annual Bonus: {self.salary}"

