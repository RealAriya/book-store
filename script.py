"""
A Program that stores book's information.

Front-End:
    Text (Entry Widgets) Fields: Title, Author, Year, ISBN
    User can view all records, search entry, update entry, delete entry, exit (program).

Back-End:
    Entry Widget
    Scroll Bar
    Command Buttons
"""

from tkinter import *

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Arya's book store")
        self.minsize(720,450)
        self.configure(background="#233D4D")

        # Labels
        l1 = Label(self, text="Title")
        l1.grid(column=0, row=0)


        l2 = Label(self, text="Author")
        l2.grid(column=2, row=0)


        l3 = Label(self, text="Year")
        l3.grid(column=0, row=1)


        l4 = Label(self, text="ISBN")
        l4.grid(column=2, row=1)


        # Entries
        self.title_text=StringVar()
        self.e1 = Entry(self, textvariable=self.title_text)
        self.e1.grid(column=1 , row=0)


        self.author_text=StringVar()
        self.e2 = Entry(self, textvariable=self.author_text)
        self.e2.grid(column=3 , row=0)


        self.year_text=StringVar()
        self.e3 = Entry(self, textvariable=self.year_text)
        self.e3.grid(column=1 , row=1)

        self.isbn_text=StringVar()
        self.e4 = Entry(self, textvariable=self.isbn_text)
        self.e4.grid(column=3 , row=1)


        # Listbox
        self.list1= Listbox(self, height=6, width=35)
        self.list1.grid(column=0, row=2, rowspan=6, columnspan=2 )


        # Scrollbar
        self.sb1 = Scrollbar(self)
        self.sb1.grid(column=2, row=2, rowspan=6)

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)


        # Buttons
        b1=Button(self, text="View All", width=12, command=self.view_command)
        b1.grid(column=3, row=2)


        b2=Button(self, text="Search", width=12, command=self.search_command)
        b2.grid(column=3, row=3)


        b3=Button(self, text="Add", width=12, command=self.add_command)
        b3.grid(column=3, row=4)


        b4=Button(self, text="Update", width=12, command=self.update_command)
        b4.grid(column=3, row=5)

        # bind method for the delete_command
        self.list1.bind("<<ListboxSelect>>", self.get_selected_row)

        b5=Button(self, text="Delete", width=12, command=self.delete_command)
        b5.grid(column=3, row=6)


        b6=Button(self, text="Close", width=12, command=self.destroy)
        b6.grid(column=3, row=7)


        # Define functions

    def get_selected_row(self,event):
        
        try:
            #global selected_tuple
            # identifies the index of the user selected item in the list1. 
            index=self.list1.curselection()[0]
            self.selected_tuple=self.list1.get(index)

            # Shows in the entry fields the user selected row item.
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1]) 
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2]) 
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3]) 
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            print("An error has occured") 


    def view_command(self):
        # ensures that everything is deleted from 0 to the end.
        self.list1.delete(0,END)
        for row in database.view():
            # Add new rows at the end.
            self.list1.insert(END, row)
            



window = Root()                                 
window.mainloop()