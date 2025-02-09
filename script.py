from tkinter import *

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Arya book store")
        self.minsize(720,450)
        self.configure(background="#233D4D")


window = Root()                                 
window.mainloop()