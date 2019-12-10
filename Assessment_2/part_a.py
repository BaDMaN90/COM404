from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # Configuration --------------------
        Title = "GUI"
        Heading = "Heading Label"
        Instruction = "Instruction Label"
        
        Label_one = "Label 1:"
        Button_one = "Button 1"
        
        # load resources
        #self.image = PhotoImage(file="green_tick.gif")

        # main attributes
        self.heading = Heading
        self.instruction = Instruction
        self.label_one_text = Label_one
        self.button_one_text = Button_one

        # set window attributes
        self.title(Title)
        
        # add components
        self.add_frame()
        self.add_main_frame()
        self.add_heading_label()
        self.add_instruction_label()
        self.add_button_one()
                   
        self.add_content_frame()
        self.add_label_one()
        self.add_example_entry()        


# Dark bordered frame 10 px --------------
    def add_frame(self):     
        #create
        self.frame = Frame()
        self.frame.grid(row = 0, column = 0)
        #style
        self.frame.configure(bg = "light grey", bd = 10)

# Main Frame ----------------------
    def add_main_frame(self):
        #create
        self.main_frame = Frame(self.frame)
        self.main_frame.grid(row = 0, column = 0)
        #style
        self.main_frame.configure(bg = "#eee", bd = 0)

    def add_heading_label(self):
        self.heading_label = Label(self.main_frame)
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(bg = "#eee", bd = 10, text = self.heading, font = "Arial 16")

    def add_instruction_label(self):
        self.instruction_label = Label(self.main_frame)
        self.instruction_label.grid(row=1, column=0)
        self.instruction_label.configure(bg = "#eee", text = self.instruction, font = "Arial 12")

    def add_button_one(self):
        self.button_one = Button(self.main_frame)
        self.button_one.grid(row=3, column=0)
        self.button_one.configure(bg = "#fee", width = 40, text = self.button_one_text, font = "Arial 10")

        
# Content frame --------------------------
    def add_content_frame(self):
        #create
        self.content_frame = Frame(self.main_frame)
        self.content_frame.grid(row = 2, column = 0)
        #style
        self.content_frame.configure(bg = "#eee", bd = 10)

# Content ---------------------------

    def add_label_one(self):
        self.label_one = Label(self.content_frame)
        self.label_one.grid(row=0, column=0)
        self.label_one.configure(bg = "#eee", text = self.label_one_text, font = "Arial 10")

    def add_example_entry(self):
        self.example_textbox = Entry(self.content_frame)
        self.example_textbox.grid(row=0, column=1)
        self.example_textbox.configure(bg = "white", fg = "#f00",  width = 30, font = "Arial 10")



# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()