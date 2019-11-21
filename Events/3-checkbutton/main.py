from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Passport Checker")
        # add variables
        self.check_var_1 = IntVar()
        self.check_var_2 = IntVar()
        self.check_var_3 = IntVar()

        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label_1()
        self.__add_yes_checkbox_1()
        self.__add_no_checkbox_1()
        self.__add_instruction_label_2()
        self.__add_yes_checkbox_2()
        self.__add_no_checkbox_2()
        self.__add_instruction_label_3()
        self.__add_yes_checkbox_3()
        self.__add_no_checkbox_3()
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
        self.add_instruction_label_1.grid(columnspan=2,sticky ="w",row=1, column=0)
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

    def __add_instruction_label_2(self):
        # create
        self.add_instruction_label_2 = Label()
        self.add_instruction_label_2.grid(columnspan=2,sticky ="w",row=3, column=0)
        # style
        self.add_instruction_label_2.configure(font = "Arial 14",text="2. Passport has at least 6 months validity?")

    def __add_yes_checkbox_2(self):
        #create
        self.add_yes_checkbox_2 = Checkbutton()
        self.add_yes_checkbox_2.grid(row = 4, column = 0)
        #style
        self.add_yes_checkbox_2.configure(text = "Yes", variable = self.check_var_2,onvalue = 1, offvalue = 0, height=2, width = 2)

    def __add_no_checkbox_2(self):
        #create
        self.add_no_checkbox_2 = Checkbutton()
        self.add_no_checkbox_2.grid(row = 4, column = 1)
        #style
        self.add_no_checkbox_2.configure(text = "No", variable = self.check_var_2,onvalue = 0, offvalue = 1, height=2, width = 2)

    def __add_instruction_label_3(self):
        # create
        self.add_instruction_label_3 = Label()
        self.add_instruction_label_3.grid(columnspan=2,sticky ="w",row=5, column=0)
        # style
        self.add_instruction_label_3.configure(font = "Arial 14",text="3. Visa, if required, is valid?")

    def __add_yes_checkbox_3(self):
        #create
        self.add_yes_checkbox_3 = Checkbutton()
        self.add_yes_checkbox_3.grid(row = 6, column = 0)
        #style
        self.add_yes_checkbox_3.configure(text = "Yes", variable = self.check_var_3,onvalue = 1, offvalue = 0, height=2, width = 2)

    def __add_no_checkbox_3(self):
        #create
        self.add_no_checkbox_3 = Checkbutton()
        self.add_no_checkbox_3.grid(row = 6, column = 1)
        #style
        self.add_no_checkbox_3.configure(text = "No", variable = self.check_var_3,onvalue = 0, offvalue = 1, height=2, width = 2)   
        
    def __add_check_button(self):
        # create
        self.check_button = Button()
        self.check_button.grid(columnspan=2,row=8, column=0)
        # style
        self.check_button.configure(bd=4,text="Check",width = 10)
        # events
        self.check_button.bind("<ButtonRelease-1>", self.__check_button_clicked)

    
        
    def __check_button_clicked(self, event):
        #verification statment
        if self.check_var_1.get() == 1 and self.check_var_2.get() == 1 and self.check_var_3.get() == 1:
            #if all the check buttons are 'Yes'
            info_message = "Passport is Valid."
            messagebox.showinfo("Passport Result", info_message)
        else:
            info_message = "Passport is Not Valid."
            messagebox.showinfo("Passport Result", info_message)


gui = Gui()
gui.mainloop()  
