from tkinter import *
from tkinter import messagebox
import time

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # Configuration --------------------
        Title = "Newsletter"
        Heading = "RECEIVE OUR NEWSLETTER"
        Heading_size = "Arial 14"
        Instruction = "Please enter your email below to receive our newsletter."
        Instruction_size = "Arial 10"

        Label_one = "Email:"
        Button_one_on = "yes"
        Button_one = "Subscribe"
        Label_type = "Type:"
        Button_type = "Weekly"
        Button_animation_on = "yes"
        Button_animation = "Start Animation"
        

        # main attributes
        self.heading = Heading
        self.heading_size = Heading_size
        self.instruction = Instruction
        self.instruction_size = Instruction_size
        self.label_one = Label_one
        self.button_one = Button_one
        self.is_email_correct = 0
        self.label_type = Label_type
        self.type_button_text = Button_type
        self.button_animation = Button_animation

        # load resources
        self.green_tick = PhotoImage(file="green_tick.gif")
        self.red_cross = PhotoImage(file="red_cross.gif")
        self.default_image = PhotoImage(file="default.gif")
        self.weekly_image = PhotoImage(file="weekly.gif")
        self.monthly_image = PhotoImage(file="monthly.gif")
        self.yearly_image = PhotoImage(file="yearly.gif")

        # set animation attributes
        self.animation_window_width = 348
        self.animation_window_height = 200
        self.image_x_pos = 139
        self.image_y_pos = 0
        self.image_x_change = 1
        self.image_y_change = 1

        # set window attributes
        self.title(Title)
        
        # add components
        self.add_frame()
        self.add_main_frame()
        self.add_heading_label()
        self.add_instruction_label()
        if Button_one_on == "yes":
            self.add_example_button()
        if Button_animation_on == "yes":
            self.add_animation_button()
                   
        self.add_content_frame()
        self.add_example_label()
        self.add_example_entry()
        self.add_image_default()   
        self.add_type_label()  
        self.add_type_button()


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
        self.heading_label.configure(bg = "#eee", bd = 2, text = self.heading, font = self.heading_size, pady = 10)

    def add_instruction_label(self):
        self.instruction_label = Label(self.main_frame)
        self.instruction_label.grid(row=1, column=0)
        self.instruction_label.configure(bg = "#eee", text = self.instruction, font = self.instruction_size, pady= 10, padx = 10)

    def add_example_button(self):
        self.example_button = Button(self.main_frame)
        self.example_button.grid(row=3, column=0)
        self.example_button.configure(bg = "#fee", width = 40, text = self.button_one, font = "Arial 10", pady = 1, padx= 10)
        #event
        self.example_button.bind("<ButtonRelease-1>", self.subscribed_button)
        
    def add_animation_button(self):
        self.animation_variable = 0
        self.animation_button = Button(self.main_frame)
        self.animation_button.grid(row=4, column=0)
        self.animation_button.configure(bg = "#fee", width = 40, text = self.button_animation, font = "Arial 10", pady = 1, padx = 10)
        #event
        self.animation_button.bind("<ButtonRelease-1>", self.animation_button_clicked) 

# Content frame --------------------------
    def add_content_frame(self):
        #create
        self.content_frame = Frame(self.main_frame)
        self.content_frame.grid(row = 2, column = 0)
        #style
        self.content_frame.configure(bg = "#eee", bd = 10)

# Content ---------------------------

    def add_example_label(self):
        self.example_label = Label(self.content_frame)
        self.example_label.grid(row=0, column=0)
        self.example_label.configure(bg = "#eee", text = self.label_one, font = "Arial 10")

    def add_example_entry(self):
        self.example_textbox = Entry(self.content_frame)
        self.example_textbox.grid(row=0, column=1)
        self.example_textbox.configure(bg = "white", fg = "#f00",  width = 30, font = "Arial 10")
        # events
        self.example_textbox.bind("<Key>", self.check_example_entry_handler)

    def add_image_default(self):
        self.image_default = Label(self.content_frame)
        self.image_default.grid(row=0, column=2)
        self.image_default.configure(image = self.default_image)

    def check_example_entry_handler(self, event):
        if len(self.example_textbox.get()) > 1 and "@" in self.example_textbox.get() and ".co.uk" in self.example_textbox.get() or ".com" in self.example_textbox.get():
            self.image_default.configure(image = self.green_tick)
            self.is_email_correct = 1
        else:
            self.image_default.configure(image = self.red_cross)
            self.is_email_correct = 0

    def subscribed_button(self, event):
        if self.is_email_correct == 1 and self.type_button_variable >= 1:
                self.info_message = "Email: " + str(self.example_textbox.get()) + " has Subscribed to the " + str(self.type_button_text) + " Newsletter!"
                messagebox.showinfo("Newsletter!", self.info_message)
        pass

    def add_type_label(self):
        self.type_label = Label(self.content_frame)
        self.type_label.grid(row=1, column=0)
        self.type_label.configure(bg = "#eee", text = self.label_type, font = "Arial 10")

    def add_type_button(self):
        self.type_button_variable = 1
        self.type_button = Button(self.content_frame)
        self.type_button.grid(row=1, column=1, columnspan = 2)
        self.type_button.configure(bg = "#eee", text = "Weekly", font = "Arial 10", width = 30)
        #event
        self.type_button.bind("<ButtonRelease-1>", self.type_button_clicked)

    def type_button_clicked(self, event):
        if self.type_button_variable == 1:
                self.type_button_variable += 1
        elif self.type_button_variable == 2:
                self.type_button_variable += 1
        elif self.type_button_variable == 3:
                self.type_button_variable = self.type_button_variable - 2
        else:
            self.type_button_variable = 1

        if self.type_button_variable == 1:
            self.type_button_text = "Weekly"
            self.type_button.configure(bg = "#eee", text = self.type_button_text, font = "Arial 10", width = 30)
        elif self.type_button_variable == 2:
            self.type_button_text = "Monthly"
            self.type_button.configure(bg = "#eee", text = "Monthly", font = "Arial 10", width = 30)        
        elif self.type_button_variable == 3:
            self.type_button_text = "Yearly"
            self.type_button.configure(bg = "#eee", text = "Yearly", font = "Arial 10", width = 30)

    def animation_button_clicked(self, event):
        self.animation = Frame(self.frame)
        self.animation.grid(row=1, column=0)
        self.animation.configure(bg = "light green", bd = 4, height = self.animation_window_height, width = self.animation_window_width)        
        self.image_label = Label(self.animation)
        self.image_label.place(x=self.image_x_pos, y=self.image_y_pos)
        self.image_label.configure(image=self.weekly_image , bd = 0)

        if self.type_button_variable == 1:
            self.image_label.configure(image=self.weekly_image)
        elif self.type_button_variable == 2:
            self.image_label.configure(image=self.monthly_image)
        elif self.type_button_variable == 3:
            self.image_label.configure(image=self.yearly_image)

        if self.animation_variable <= 1:
            self.animation_variable += 1
        elif self.animation_variable == 2:
            self.animation_variable -= 1

        if self.animation_variable == 1:
            self.button_animation = "Stop Animation"
            self.animation_button.configure(bg = "#fee", width = 40, text = self.button_animation, font = "Arial 10", pady = 1, padx = 10)
            self.run_animation()
        elif self.animation_variable == 2:
            self.button_animation = "Start Animation"
            self.animation_button.configure(bg = "#fee", width = 40, text = self.button_animation, font = "Arial 10", pady = 1, padx = 10)
            self.animation.configure(bg = "#eee", bd = 4, height = self.animation_window_height, width = self.animation_window_width) 

    def run_animation(self):
        posx = self.image_x_pos
        posy = self.image_y_pos
        changex = self.image_x_change
        changey = self.image_y_change
        if posx >= 0 and posx <= 141 and posy >= 0 and posy <= 79:
            self.image_x_pos = self.image_x_pos - changex
            self.image_y_pos = self.image_y_pos + changey
            self.image_label.place(x=self.image_x_pos, y=self.image_y_pos)
        
        elif posx >= 0 and posx <= 138 and posy >= 80 and posy <= 159:
            self.image_x_pos = self.image_x_pos + changex
            self.image_y_pos = self.image_y_pos + changey
            self.image_label.place(x=self.image_x_pos, y=self.image_y_pos)
        
        elif posx >= 139 and posx <= 268 and posy >= 80 and posy <= 161:
            self.image_x_pos = self.image_x_pos + changex
            self.image_y_pos = self.image_y_pos - changey
            self.image_label.place(x=self.image_x_pos, y=self.image_y_pos)
        
        else:
            self.image_x_pos = self.image_x_pos - changex
            self.image_y_pos = self.image_y_pos - changey
            self.image_label.place(x=self.image_x_pos, y=self.image_y_pos)
        
        # ticker
        self.after(10, self.run_animation)
        print(self.image_x_pos, self.image_y_pos)
                
# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
