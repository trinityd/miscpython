import tkinter
# from tkinter import Tk, W, E
from tkinter.ttk import Label, Frame, Button, Entry, Style

class GUI(tkinter.Frame):
    """
    class GUI is the View for a simple program that exemplifies the Model/View/Controller
    architecture. This View class is a tkinter.Frame that contains two Labels, two Entrys, and three Buttons. Two Button
    notifies the Controller when they are pressed, and the other Button quits the app. The Labels display
    which temperature measure each Entry field corresponds to. Notice that the View never contains a reference to the Model,
    but it does contain a reference to the Controller.
    """
    def __init__(self, controller):
        Frame.__init__(self)
        self.master.title("Temp Convert")
        self.pack()
        self.controller = controller    # saves a reference to the controller so that we can call methods
                                        # on the controller object when the user generates events       

        Style().configure("TButton", padding=(0, 5, 0, 5),
            font='serif 10')

        # Adds padding to cols and rows
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)


        # Adds widgets
        self.labelFahrenheit = Label(self)
        self.labelFahrenheit["text"] = "Fahrenheit"
        self.labelFahrenheit.grid(row=0, column=0)

        self.labelCelsius = Label(self)
        self.labelCelsius["text"] = "Celsius"
        self.labelCelsius.grid(row=0, column=1)

        self.fahrenheitEntry = Entry(self)
        self.fahrenheitEntry.insert(0, "32")
        self.fahrenheitEntry.grid(row=1, column=0)

        self.celsiusEntry = Entry(self)
        self.celsiusEntry.insert(0, "0")
        self.celsiusEntry.grid(row=1, column=1)
        
        # Buttons with commands handled by controller
        self.convertButtonFC = Button(self)
        self.convertButtonFC["text"] = "Convert F->C"
        self.convertButtonFC["command"] = lambda: self.controller.buttonPressed(self.convertButtonFC["text"])
        self.convertButtonFC.grid(row=2, column=0)

        self.convertButtonCF = Button(self)
        self.convertButtonCF["text"] = "Convert F<-C"
        self.convertButtonCF["command"] = lambda: self.controller.buttonPressed(self.convertButtonCF["text"])
        self.convertButtonCF.grid(row=2, column=1)

        self.quitButton = Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] =  self.quit
        self.quitButton.grid(row=3, column=1)
