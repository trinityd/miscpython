"""
	Defines class Rectangle and tests it by creating two Rectangle objects
"""
class Rectangle:
    """ 
        One object of this class stores one rectangle's length and width
    """
    def __init__(self):
        """
            Sets both height and width to 0
        """
        self.height = 0
        self.width = 0

    def setData(self, height, width):
        """
            Sets the object's dimensions to height by width
        """
        if (type(height) != int and type(height) != float) or (type(width) != int and type(width) != float):
            raise TypeError()
        elif height < 0 or width < 0:
            raise ValueError()
        self.height = height
        self.width = width

    def __str__(self):
        """
            returns a sentence that tells the height and width of the object
        """
        return f"height = {self.height}, and width = {self.width}"

    def area(self):
        """
            returns a float that tells the area of the object
        """
        return self.height * self.width
        
"""
     Creates two Rectangle objects and calls methods on them for testing purposes
"""
if __name__ == "__main__":

    # Good Rectangle
    r1 = Rectangle()
    print (r1)   # automatcially calls __str__(self) method and prints the returned value
    r1.setData(3,4)
    print (r1)
    print (f"Area: {r1.area()}")

    # Bad Rectangle
    try:
        r2 = Rectangle()
        r2.setData(18, "error")
        print (r2)
        print (f"Area: {r2.area()}")
    except TypeError:
        print ("Can't set the Rectangle to a non-integer value")
    except ValueError:
       print ("Can't set the Rectangle to a negative number")

    # Good Rectangle
    r3 = Rectangle()
    r3.setData(5,6.5)
    print (r3)
    print (f"Area: {r3.area()}")

    # Bad Rectangle
    try:
        r4 = Rectangle()
        r4.setData(-2.7, 3)
        print (r4)
        print (f"Area: {r4.area()}")
    except TypeError:
        print ("Can't set the Rectangle to a non-integer value")
    except ValueError:
       print ("Can't set the Rectangle to a negative number")


""" A RECORDING OF THE RUN
height = 0, and width = 0
height = 3, and width = 4
Area: 12
Can't set the Rectangle to a non-integer value
height = 5, and width = 6.5
Area: 32.5
Can't set the Rectangle to a negative number
"""