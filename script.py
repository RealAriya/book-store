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
from Query import Database 

database = Database("books.db")

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Arya's Bookstore")
        self.geometry("800x600")
        # self.configure(background="#233D4D")

        # Labels
        l1 = Label(self, text="Title", bg="#233D4D", fg="white")
        l1.grid(column=0, row=0, padx=10, pady=10)


        l2 = Label(self, text="Author", bg="#233D4D", fg="white")
        l2.grid(column=2, row=0, padx=10, pady=10)


        l3 = Label(self, text="Year", bg="#233D4D", fg="white")
        l3.grid(column=0, row=1, padx=10, pady=10)


        l4 = Label(self, text="ISBN", bg="#233D4D", fg="white")
        l4.grid(column=2, row=1, padx=10, pady=10)


        # Entries
        self.title_text=StringVar()
        self.e1 = Entry(self, textvariable=self.title_text)
        self.e1.grid(column=1, row=0, padx=10, pady=10)


        self.author_text=StringVar()
        self.e2 = Entry(self, textvariable=self.author_text)
        self.e2.grid(column=3, row=0, padx=10, pady=10)


        self.year_text=StringVar()
        self.e3 = Entry(self, textvariable=self.year_text)
        self.e3.grid(column=1, row=1, padx=10, pady=10)

        self.isbn_text=StringVar()
        self.e4 = Entry(self, textvariable=self.isbn_text)
        self.e4.grid(column=3, row=1, padx=10, pady=10)


        # Listbox
        self.list1= Listbox(self, height=15, width=50, bg="#F3F3F3")
        self.list1.grid(column=0, row=2, rowspan=6, columnspan=2, padx=10, pady=10 )


        # Scrollbar
        self.sb1 = Scrollbar(self)
        self.sb1.grid(column=2, row=2, rowspan=6, sticky='ns')

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)


        # Buttons
        b1=Button(self, text="View All", width=12, command=self.view_command, bg="#4CAF50", fg="white")
        b1.grid(column=3, row=2, padx=10, pady=10)


        b2=Button(self, text="Search", width=12, command=self.search_command, bg="#4CAF50", fg="white")
        b2.grid(column=3, row=3, padx=10, pady=10)


        b3=Button(self, text="Add", width=12, command=self.add_command, bg="#4CAF50", fg="white")
        b3.grid(column=3, row=4, padx=10, pady=10)


        b4=Button(self, text="Update", width=12, command=self.update_command, bg="#4CAF50", fg="white")
        b4.grid(column=3, row=5, padx=10, pady=10)

        # bind method for the delete_command
        self.list1.bind("<<ListboxSelect>>", self.get_selected_row)

        b5=Button(self, text="Delete", width=12, command=self.delete_command, bg="#4CAF50", fg="white")
        b5.grid(column=3, row=6, padx=10, pady=10)


        b6=Button(self, text="Close", width=12, command=self.destroy, bg="#4CAF50", fg="white")
        b6.grid(column=3, row=7, padx=10, pady=10)


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
            pass


    def view_command(self):
        # ensures that everything is deleted from 0 to the end.
        self.list1.delete(0,END)
        for row in database.view():
            # Add new rows at the end.
            self.list1.insert(END, " | ".join(map(str, row)))

    
    def search_command(self):
        self.list1.delete(0,END)
        # uses get for a search method
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, " | ".join(map(str, row)))


    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        # makes sure the list is empty
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))    
        # Clear the entry fields
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)


    def delete_command(self):
        database.delete(self.selected_tuple[0])

    
    def update_command(self):
        database.update(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        print(self.selected_tuple[0],self.selected_tuple[1],self.selected_tuple[2],self.selected_tuple[3],self.selected_tuple[4])


window = Root()                                 
window.mainloop()