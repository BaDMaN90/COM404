from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # Configuration --------------------
        Title = "GUI"
        Heading = "Heading Label"
        Instruction = "Instruction Label"

        Button_one_on = "yes"
        Button_one = "Button 1"
        
        # load resources
        #self.image = PhotoImage(file="green_tick.gif")

        # main attributes
        self.heading = Heading
        self.instruction = Instruction
        self.button_one = Button_one

        # set window attributes
        self.title(Title)
        
        # add components
        self.add_frame()
        self.add_main_frame()
        self.add_heading_label()
        self.add_instruction_label()
        if Button_one_on == "yes":
            self.add_example_button()
                   
        self.add_content_frame()
        self.add_example_label()
        self.add_example_entry()        


# Dark bordered frame 10 px --------------
    def add_frame(self):     
        #create
        self.frame = Frame()
        self.frame.grid(row = 0, column = 0)
        #style
        self.frame.configure(bg = "grey", bd = 10)

# Main Frame ----------------------
    def add_main_frame(self):
        #create
        self.main_frame = Frame(self.frame)
        self.main_frame.grid(row = 0, column = 0)
        #style
        self.main_frame.configure(bg = "light grey", bd = 10)

    def add_heading_label(self):
        self.heading_label = Label(self.main_frame)
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(bg = "light grey", bd = 10, text = self.heading, font = "Arial 16")

    def add_instruction_label(self):
        self.instruction_label = Label(self.main_frame)
        self.instruction_label.grid(row=1, column=0)
        self.instruction_label.configure(bg = "light grey", text = self.instruction, font = "Arial 12")

    def add_example_button(self):
        self.example_button = Button(self.main_frame)
        self.example_button.grid(row=3, column=0)
        self.example_button.configure(bg = "grey", text = self.button_one, font = "Arial 12")

        
# Content frame --------------------------
    def add_content_frame(self):
        #create
        self.content_frame = Frame(self.main_frame)
        self.content_frame.grid(row = 2, column = 0)
        #style
        self.content_frame.configure(bg = "light grey", bd = 10)

# Content ---------------------------

    def add_example_label(self):
        self.example_label = Label(self.content_frame)
        self.example_label.grid(row=0, column=0)
        self.example_label.configure(bg = "light grey", text = "Example Label", font = "Arial 12")

    def add_example_entry(self):
        self.example_textbox = Entry(self.content_frame)
        self.example_textbox.grid(row=0, column=1)
        self.example_textbox.configure(bg = "light grey", width = 30)



# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()