from tkinter import *

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 250

class Gui(Tk):

    # initialise window
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="#989898", height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
        
        self.add_heading_label()
        self.add_sub_heading_label()
        self.add_email_label()
        self.add_email_enrty()
        self.add_sub_button()


    def add_frame(self):
        self.frame= Frame()
        self.frame.place(x=10,y=10)
        self.frame.configure(bg="#c2c2c2",height=230,width=480)
        self.frame.pack()

    def add_heading_frame(self):
        self.heading_frame.Frame(bg="#c2c2c2")
        self.heading_frame.pack()

    def add_heading_label(self):
        # create   
        self.heading_label = Label()
        self.heading_label.pack(side = TOP)
        # style
        self.heading_label.configure(bg="#c2c2c2",font="Arial 24", text="  RECEIVE OUR NEWLETTER  ")


    def add_sub_heading_label(self):
        # create   
        self.sub_heading_label = Label()
        self.sub_heading_label.pack(side = TOP)
        # style
        self.sub_heading_label.configure(bg="#c2c2c2",font="Arial 14", text="Please enter your email below to receive our newsletter.")

    def add_email_label(self):
        # create   
        self.email_label = Label()
        self.email_label.pack(side = LEFT)
        # style
        self.email_label.configure(bg="#c2c2c2",font="Arial 14", text="Email:")

    def add_email_enrty(self):
        # create   
        self.email_entry = Entry()
        self.email_entry.pack(side = LEFT)
        # style
        self.email_entry.configure(bg="#fff",font="Arial 14", width = 30)


    def add_sub_button(self):
        # create   
        self.sub_button = Button()
        self.sub_button.pack(side = TOP)
        # style
        self.sub_button.configure(bg="#c2c2c2",font="Arial 14", text="Subscribe", width = 30)    