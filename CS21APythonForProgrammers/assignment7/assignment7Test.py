""" Tests the Employee and Manager classes """

""" Imports Employee and Manager """
from employee import Employee
from manager import Manager


if __name__ == "__main__":
    """ Defines Employees and Managers """
    e1 = Employee("Jim", "Wellington III", "123-45-6789", 10000)
    e2 = Employee("Bob", "Connogherty", "132-42-5343", 25000)
    e3 = Employee("William", "Williamson", "098-76-5432", 40000)

    m1 = Manager("Dirk", "Dangerous", "675-01-1234", 140000000, "Executive Assistant to the CEO", 500000)
    m2 = Manager("John", "McCEO", "896-45-8293", 15000000000, "CEO", 8000000)

    company = [e1, e2, e3, m1, m2]

    """ Gives raises to Employees and Managers, checks if raise ratio remains the same for each after giving the raise """
    for person in company:
        raiseAmt = .25

        print("Pre-Raise  > " + str(person))
        preSal = person.salary
        person.giveRaise(raiseAmt)
        print("Post-Raise > " + str(person))
        postSal = person.salary

        print(f"             (Post-Raise Salary - Pre-Raise Salary) / Pre-Raise Salary == {(postSal - preSal)/preSal}")


"""
Test Run:

Pre-Raise  > First Name: Jim Last Name: Wellington III SSN: 123-45-6789 Salary: 10000.0
Post-Raise > First Name: Jim Last Name: Wellington III SSN: 123-45-6789 Salary: 12500.0
            (Post-Raise Salary - Pre-Raise Salary) / Pre-Raise Salary == 0.25
Pre-Raise  > First Name: Bob Last Name: Connogherty SSN: 132-42-5343 Salary: 25000.0
Post-Raise > First Name: Bob Last Name: Connogherty SSN: 132-42-5343 Salary: 31250.0
            (Post-Raise Salary - Pre-Raise Salary) / Pre-Raise Salary == 0.25
Pre-Raise  > First Name: William Last Name: Williamson SSN: 098-76-5432 Salary: 40000.0
Post-Raise > First Name: William Last Name: Williamson SSN: 098-76-5432 Salary: 50000.0
            (Post-Raise Salary - Pre-Raise Salary) / Pre-Raise Salary == 0.25
Pre-Raise  > First Name: Dirk Last Name: Dangerous SSN: 675-01-1234 Salary: 140000000.0 Title: 675-01-1234 Annual Bonus: 140000000.0
Post-Raise > First Name: Dirk Last Name: Dangerous SSN: 675-01-1234 Salary: 175000000.0 Title: 675-01-1234 Annual Bonus: 175000000.0
            (Post-Raise Salary - Pre-Raise Salary) / Pre-Raise Salary == 0.25
Pre-Raise  > First Name: John Last Name: McCEO SSN: 896-45-8293 Salary: 15000000000.0 Title: 896-45-8293 Annual Bonus: 15000000000.0
Post-Raise > First Name: John Last Name: McCEO SSN: 896-45-8293 Salary: 18750000000.0 Title: 896-45-8293 Annual Bonus: 18750000000.0
            (Post-Raise Salary - Pre-Raise Salary) / Pre-Raise Salary == 0.25

"""