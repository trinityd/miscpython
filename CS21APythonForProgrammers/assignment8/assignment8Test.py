""" Tests the Employee and Manager classes """

""" Imports Employee and Manager """
from employee import Employee
from manager import Manager


if __name__ == "__main__":
    """ Defines Employees and Managers """
    e1 = Employee("Jim", "Wellington III", "123-45-6789", 10000)
    e2 = Employee("Bob", "Connogherty", "132-42-5343", 25000)
    e3 = Employee("William", "Williamson", "098-76-5432", 40000)
    e4 = Employee("Aardvark", "Aaronson", "000-11-2222", 40000)
    e5 = Employee("Timothy", "Dangerous", "777-22-8888", 40000)

    m1 = Manager("Dirk", "Dangerous", "675-01-1234", 140000000, "Executive Assistant to the CEO", 500000)
    m2 = Manager("John", "McCEO", "896-45-8293", 15000000000, "CEO", 8000000)
    m3 = Manager("Dirk", "Dangerous", "333-44-5555", 666, "Dirk 1's Evil Twin", 666)

    company = [e1, e2, e3, e4, e5, m1, m2, m3]

    print(""" * Sorting""")

    print("Company pre-sorting:")
    for person in company:
        print(f"\t{person.fullName} ({person.SSN})")

    company.sort()

    print("\n")
    print("Company post-sorting:")
    for person in company:
        print(f"\t{person.fullName} ({person.SSN})")

    print("\n")
    print(""" * Checking equality/comparison """)
    for person in company:
        print(f"{person.fullName} ({person.SSN}) == {m1.fullName} ({m1.SSN})? {'Yes' if (person == m1) else 'No'}")
        print(f"{person.fullName} ({person.SSN}) < {m1.fullName} ({m1.SSN})? {'Yes' if (person < m1) else 'No'}\n")
 
"""
Test Run:

 * Sorting
Company pre-sorting:
        Jim Wellington III (123-45-6789)
        Bob Connogherty (132-42-5343)
        William Williamson (098-76-5432)
        Aardvark Aaronson (000-11-2222)
        Timothy Dangerous (777-22-8888)
        Dirk Dangerous (675-01-1234)
        John McCEO (896-45-8293)
        Dirk Dangerous (333-44-5555)


Company post-sorting:
        Aardvark Aaronson (000-11-2222)
        Bob Connogherty (132-42-5343)
        Dirk Dangerous (675-01-1234)
        Dirk Dangerous (333-44-5555)
        Timothy Dangerous (777-22-8888)
        John McCEO (896-45-8293)
        Jim Wellington III (123-45-6789)
        William Williamson (098-76-5432)


 * Checking equality/comparison
Aardvark Aaronson (000-11-2222) == Dirk Dangerous (675-01-1234)? No
Aardvark Aaronson (000-11-2222) < Dirk Dangerous (675-01-1234)? Yes

Bob Connogherty (132-42-5343) == Dirk Dangerous (675-01-1234)? No
Bob Connogherty (132-42-5343) < Dirk Dangerous (675-01-1234)? Yes

Dirk Dangerous (675-01-1234) == Dirk Dangerous (675-01-1234)? Yes
Dirk Dangerous (675-01-1234) < Dirk Dangerous (675-01-1234)? No

Dirk Dangerous (333-44-5555) == Dirk Dangerous (675-01-1234)? Yes
Dirk Dangerous (333-44-5555) < Dirk Dangerous (675-01-1234)? No

Timothy Dangerous (777-22-8888) == Dirk Dangerous (675-01-1234)? No
Timothy Dangerous (777-22-8888) < Dirk Dangerous (675-01-1234)? No

John McCEO (896-45-8293) == Dirk Dangerous (675-01-1234)? No
John McCEO (896-45-8293) < Dirk Dangerous (675-01-1234)? No

Jim Wellington III (123-45-6789) == Dirk Dangerous (675-01-1234)? No
Jim Wellington III (123-45-6789) < Dirk Dangerous (675-01-1234)? No

William Williamson (098-76-5432) == Dirk Dangerous (675-01-1234)? No
William Williamson (098-76-5432) < Dirk Dangerous (675-01-1234)? No

"""