"""
	Defines class Employee and tests it
    One object of this class represents one employee's first and last name, SSN, and salary
"""
class Employee:
    """ 
        Initializes one employee's first and last name, SSN (as string, to account for xxx-xx-xxxx or xxxxxxxxx), and salary (as float)
        No writing to shell
        No reading to shell
    """
    def __init__(self, firstName, lastName, SSN, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = firstName + " " + lastName
        self.SSN = str(SSN)
        self.salary = float(salary)

    """
        Returns a sentence that tells the employee's first and last name, SSN, and salary
        No writing to shell
        No reading to shell
    """
    def __str__(self):
        return f"First Name: {self.firstName} Last Name: {self.lastName} SSN: {self.SSN} Salary: {self.salary}"

    """
        Returns True if self's first and last name (case insensitive) == other's first and last name (case insensitive), False otherwise
    """
    def __eq__(self, other):
        return self.firstName.lower()==other.firstName.lower() and self.lastName.lower()==other.lastName.lower()

    """
        Returns True when the name in self is alphabetically less than the name in other, and returns False otherwise. If the last names are equal, then checks the first names to determine which object is less than the other. This is by dictionary ordering, aka "case insensitive", which does not depend on the capitalization of the names. 
    """
    def __lt__(self, other):
        
        if self.lastName.lower() < other.lastName.lower():
            return True
        elif self.lastName.lower() > other.lastName.lower():
            return False
        else:  # last names are equal
            return self.firstName.lower() < other.firstName.lower()
    
    """
        Adds "percentRaise" percent of the current salary to the salary instance variable of this object.
        No return
        No writing to shell
        No reading to shell
    """
    def giveRaise(self, percentRaise):
        self.salary += self.salary * percentRaise
    
