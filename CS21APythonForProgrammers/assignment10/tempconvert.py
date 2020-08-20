class TempConvert:
    """
    class TempConvert is the Model for a program that exemplifies the
    Model/View/Controller architecture. It contains the methods for converting between Fahrenheit and Celsius.
    Note that the Model (tempconvert.py) never contains a reference to the View (gui.py).
    """

    @staticmethod
    def farToCel(far):
        """ Given a temp in Fahrenheit, returns that temp in Celsius. """
        return (5/9) * (far-32)

    @staticmethod
    def celToFar(cel):
        """ Given a temp in Celsius, returns that temp in Fahrenheit. """
        return (9/5 * cel) + 32