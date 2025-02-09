"""
A Program that stores book's information.

Front-End:
    Text (Entry Widgets) Fields: Title, Author, Year, ISBN
    User can view all records, search entry, update entry, delete entry, exit (program).

Back-End:
    Entry Widget
    Scroll Bar
    Command Buttons
    Tkinter -> Grid Method
"""

from tkinter import *

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Arya's book store")
        self.minsize(720,450)
        self.configure(background="#233D4D")


        l1 = Label(self, text="Title")
        l1.grid(column=0, row=0)


        l2 = Label(self, text="Author")
        l2.grid(column=2, row=0)


        l3 = Label(self, text="Year")
        l3.grid(column=0, row=1)


        l4 = Label(self, text="ISBN")
        l4.grid(column=2, row=1)


window = Root()                                 
window.mainloop()