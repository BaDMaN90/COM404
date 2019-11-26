from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        #self.not_ready_image = PhotoImage(file="U:\Documents\Problem Solving\COM404\GUI\\7-hotel\\notreadys.gif")
        #self.ready_image = PhotoImage(file="U:\Documents\Problem Solving\COM404\GUI\\7-hotel\ready.gif")


        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_main_frame()
        self.add_heading_label()


    def add_main_frame(self):
        #create
        self.main_frame = Frame()
        self.main_frame.grid(row = 0, column = 0)
        #style
        self.main_frame.configure(bg = "white", bd = 4)
        
    def add_heading_label(self):
        self.heading_label = Label(self.main_frame)
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(bg = "white", text = "Hotel Check In", font = "Arial 16")


# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()