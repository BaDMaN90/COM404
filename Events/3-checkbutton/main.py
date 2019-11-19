from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Passport Checker")
        # add variables
        self.check_var_1 = IntVar()

        # add components
        self.__add_heading_label()
        self.__add_instruction_label_1()
        self.__add_yes_checkbox_1()
        self.__add_no_checkbox_1()
        self.__add_check_button()

        
        
    def __add_heading_label(self):
        # create
        self.add_heading_label = Label()
        self.add_heading_label.grid(columnspan=2,row=0, column=0)
        # style
        self.add_heading_label.configure(font = "Arial 30",text="Passport Checker")
        
    def __add_instruction_label_1(self):
        # create
        self.add_instruction_label_1 = Label()
        self.add_instruction_label_1.grid(sticky ="w",row=1, column=0)
        # style
        self.add_instruction_label_1.configure(font = "Arial 14",text="1. Photo matches face?")

    def __add_yes_checkbox_1(self):
        #create
        self.add_yes_checkbox_1 = Checkbutton()
        self.add_yes_checkbox_1.grid(row = 2, column = 0)
        #style
        self.add_yes_checkbox_1.configure(text = "Yes", variable = self.check_var_1,onvalue = 1, offvalue = 0, height=2, width = 2)

    def __add_no_checkbox_1(self):
        #create
        self.add_no_checkbox_1 = Checkbutton()
        self.add_no_checkbox_1.grid(row = 2, column = 1)
        #style
        self.add_no_checkbox_1.configure(text = "No", variable = self.check_var_1,onvalue = 0, offvalue = 1, height=2, width = 2)
    def __add_check_button(self):
        # create
        self.check_button = Button()
        self.check_button.grid(columnspan=2,row=3, column=0)
        # style
        self.check_button.configure(bd=4,text="Check",width = 10)
        # events
        self.check_button.bind("<ButtonRelease-1>", self.__check_button_clicked)
        
    def __check_button_clicked(self, event):
        pass

gui = Gui()
gui.mainloop()  