from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
    def __add_heading_label(self):
        # create
        self.add_heading_label = Label()
        self.add_heading_label.grid(row=0, column=0)
        # style
        self.add_heading_label.configure(font = "Arial 30",text="Entrance Ticket")
        
    def __add_instruction_label(self):
        # create
        self.add_instruction_label = Label()
        self.add_instruction_label.grid(row=1, column=0)
        # style
        self.add_instruction_label.configure(font = "Arial 18",text="How many tickets are needed?")
        
    def __add_tickets_entry(self):
        # create
        self.add_tickets_entry = Entry()
        self.add_tickets_entry.grid(row=2, column=0)
        # style
        self.add_tickets_entry.configure(bd=4,width = 50)        
    def __add_buy_button(self):
        # create
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0)

        # style
        self.buy_button.configure(bd=4,text="Buy",width = 10)

        # events
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)
        
 
    def __buy_button_clicked(self, event):
        no_of_tickets = self.add_tickets_entry.get()
        try:
            int(no_of_tickets)
            if int(no_of_tickets) >= 2:
                info_message = "You have bought " + str(no_of_tickets) + " tickets!"
                messagebox.showinfo("Purchased!", info_message)
            elif int(no_of_tickets) == 1:
                info_message = "You have bought " + str(no_of_tickets) + " ticket!"
                messagebox.showinfo("Purchased!", info_message)
            else:
                info_message = "invalid input!"
                messagebox.showinfo("Try Again.", info_message)           
        except ValueError:
            info_message = "Please enter the number of tickets."
            messagebox.showinfo("Try Again.", info_message)

gui = Gui()
gui.mainloop()
