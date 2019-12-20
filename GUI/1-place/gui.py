from tkinter import *

FONT_24_SIZE = 14
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 250

class Gui(Tk):

    # initialise window
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="#989898", height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
        
        self.add_mixed_bg()               
        self.add_heading_label()
        self.add_heading_label_2()
        self.add_text_label_email()
        self.add_entry_email()
        self.add_button_sub()

    def add_mixed_bg(self):
        self.mixed_bg = Label()
        self.mixed_bg.place(x=20,y=20)
        self.mixed_bg.configure(bg="#c2c2c2",height=13,width=65)


    def add_heading_label(self):
        #label text
        header = "RECEIVE OUR NEWLETTER"
        # create   
        self.heading_label = Label()
        self.heading_label.place(x=34, y=20)

        # style
        self.heading_label.configure(bg="#c2c2c2",font = "Arial 24", text = header)


    def add_heading_label_2(self):
        #label text
        header_2 = "Please enter your email below to receive our newsletter."
        # create   
        self.heading_label = Label()
        self.heading_label.place(x=40, y=75)
        # style
        self.heading_label.configure(bg="#c2c2c2",font = "Arial 13", text = header_2)


    def add_text_label_email(self):
        #label text
        text_1 = "Email:"
        # create   
        self.heading_label = Label()
        self.heading_label.place(x=40, y=120)
        # style
        self.heading_label.configure(bg="#c2c2c2",font = "Arial 13", text = text_1)

    def add_entry_email(self):
        #create
        self.entry_1 = Entry()
        self.entry_1.place(x=90, y=120)
        #style
        self.entry_1.configure(bg="#fff",font = "Arial 13", width = "33")

    def add_button_sub(self):
        #create
        self.entry_1 = Button()
        self.entry_1.place(x=20, y=190)
        #style
        self.entry_1.configure(bg="#ede",font = "Arial 13", width = "50", height = "1", text = "Subscribe")
