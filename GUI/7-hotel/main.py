from tkinter import *
import time

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.green_tick = PhotoImage(file="green_tick.gif")
        self.red_cross = PhotoImage(file="red_cross.gif")

        # main attributes
        self.control_value = 0


        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_main_frame()
        self.add_heading_label()
        self.add_content_frame()
        self.add_checkin_button()

        self.add_name_label()
        self.add_name_box()
        self.check_name_box()

        self.add_passport_label()
        self.add_passport_box()
        self.check_passport_box()

        self.add_nights_label()
        self.add_nights_box()
        self.check_nights_box()        

# Main Frame ----------------------
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

    def add_checkin_button(self):
        self.checkin_button = Button(self.main_frame)
        self.checkin_button.grid(row=2,column=0)
        self.checkin_button.configure(bg="white", text="Check In", font="Arial 16")
        #Event
        self.checkin_button.bind("<Button-1>", self.checkin_button_handler)

    def checkin_button_handler(self, event):
        name = self.name_box.get()
        passport = self.passport_box.get()
        nights = self.nights_box.get()
        if self.control_value == 111:
            print(name, passport, nights)
        elif self.control_value == 101 or self.control_value == 1:
            if self.control_value == 101:
                print("Passport value is missing or incorrect")
            elif self.control_value == 1:
                print("Passport and No. of nights value is missing or incorrect")

        pass

# Content frame --------------------------
    def add_content_frame(self):
        #create
        self.content_frame = Frame(self.main_frame)
        self.content_frame.grid(row = 1, column = 0)
        #style
        self.content_frame.configure(bg = "white", bd = 4)

    #Name entery and check ------------------------
    def add_name_label(self):
        self.name_label = Label(self.content_frame)
        self.name_label.grid(row=0,column=0)
        self.name_label.configure(bg="white", text="Name:", font = "Arial 16")

    def add_name_box(self):
        self.name_box = Entry(self.content_frame)
        self.name_box.grid(row=0,column=1)
        self.name_box.configure(bg="white", font = "Arial 16")
        # events
        self.name_box.bind("<Key>", self.check_name_box_handler)

    def check_name_box(self):
        self.check_name = Label(self.content_frame)
        self.check_name.grid(row=0, column=2)
        self.check_name.configure(image=self.red_cross,height=60,width=53)

    def check_name_box_handler(self, event):
        if len(self.name_box.get()) > 3:
            self.check_name.configure(image=self.green_tick,height=60,width=53)
        else:
            self.check_name.configure(image=self.red_cross,height=60,width=53)

    #Passport number entery and check -----------------------
    def add_passport_label(self):
        self.passport_label = Label(self.content_frame)
        self.passport_label.grid(row=1,column=0)
        self.passport_label.configure(bg="white", text="Passport Number:", font = "Arial 16")

    def add_passport_box(self):
        self.passport_box = Entry(self.content_frame)
        self.passport_box.grid(row=1,column=1)
        self.passport_box.configure(bg="white", font = "Arial 16")
        # events
        self.passport_box.bind("<Key>", self.check_passport_box_handler)

    def check_passport_box(self):
        self.check_passport = Label(self.content_frame)
        self.check_passport.grid(row=1, column=2)
        self.check_passport.configure(image=self.red_cross,height=60,width=53)

    def check_passport_box_handler(self, event):
        if len(self.passport_box.get()) > 3:
            self.check_passport.configure(image=self.green_tick,height=60,width=53)
        else:
            self.check_passport.configure(image=self.red_cross,height=60,width=53)

    #Number of Nights entery and check -----------------------
    def add_nights_label(self):
        self.nights_label = Label(self.content_frame)
        self.nights_label.grid(row=2,column=0)
        self.nights_label.configure(bg="white", text="No. of nights:", font = "Arial 16")

    def add_nights_box(self):
        self.nights_box = Entry(self.content_frame)
        self.nights_box.grid(row=2,column=1)
        self.nights_box.configure(bg="white", font = "Arial 16")
        # events
        self.nights_box.bind("<Key>", self.check_nights_box_handler)

    def check_nights_box(self):
        self.check_nights = Label(self.content_frame)
        self.check_nights.grid(row=2, column=2)
        self.check_nights.configure(image=self.red_cross,height=60,width=53)

    def check_nights_box_handler(self, event):
            nights = self.nights_box.get()
            try:
                int(nights)
                self.nights_box.configure(bg="white", font = "Arial 16")
                if int(nights) >= 1 and int(nights) <= 365:
                    self.check_nights.configure(image=self.green_tick,height=60,width=53)
                else:
                    self.check_nights.configure(image=self.red_cross,height=60,width=53)
            except ValueError:
                print(nights)
                self.check_nights.configure(image=self.red_cross,height=60,width=53)
                #self.nights_box.configure(bg="red", font = "Arial 16") 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
