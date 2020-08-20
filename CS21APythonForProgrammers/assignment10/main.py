import tkinter
import gui    # the VIEW
import tempconvert    # the MODEL

class Controller:
    """
    The CONTROLLER for an app that follows the Model/View/Controller architecture. When the user presses a Button on the View, this Controller calls the appropriate methods in the Model. The Controller handles all communication between the Model and the View.
    """
    def __init__(self):
        """  
        This starts the Tk framework up, instantiates the Model (a Counter object), instantiates the View (a MyFrame object), and starts the event loop that waits for the user to press a Button on the View.
        """
        root = tkinter.Tk()
        self.model = tempconvert.TempConvert
        self.view = gui.GUI(self)
        self.view.mainloop()
        
        root.destroy()

    def buttonPressed(self, cmd):
        """
        Python calls this method when the user presses the incrementButton in the View.
        """
        if cmd == self.view.convertButtonFC["text"]:
            fahrenheitVal = float(self.view.fahrenheitEntry.get())
            self.view.celsiusEntry.delete(0, 'end')
            self.view.celsiusEntry.insert(0, str(self.model.farToCel(fahrenheitVal)))
        elif cmd == self.view.convertButtonCF["text"]:
            celsiusVal = float(self.view.celsiusEntry.get())
            self.view.fahrenheitEntry.delete(0, 'end')
            self.view.fahrenheitEntry.insert(0, str(self.model.celToFar(celsiusVal)))   

if __name__ == "__main__":
    c = Controller()