from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # Configuration --------------------
        Title = "Letter to Santa"
        Heading = "Write to Santa!"
        
        name_label = "Your name:"
        post_button = "Post Letter"

        # load resources
        self.santa_image = PhotoImage(file="Assessment_2\santa.gif")
        self.unknown_image = PhotoImage(file="Assessment_2\pic.gif")
        self.elf_image = PhotoImage(file="Assessment_2\elf.gif")
        self.reindeer_image = PhotoImage(file="Assessment_2\\reindeer.gif")
        self.snowman_image = PhotoImage(file="Assessment_2\snowman.gif")

        # set animation attributes
        self.animation_window_width = 384
        self.animation_window_height = 200
        self.animation_button_text = "Start Animation"
        self.image_x_pos = 139
        self.image_y_pos = 10
        self.image_x_change = 1
        self.image_y_change = 1
        self.tick_time = 10

        # main attributes
        self.heading = Heading
        self.name_label_text = name_label
        self.post_button_text = post_button

        # set window attributes
        self.title(Title)
        
        # add components
        self.add_frame()
        self.add_global_frame()
        self.add_heading_label()
        self.add_post_button()
              
        self.add_content_frame()
        self.add_name_label()
        self.add_name_entry()        
        self.add_santa_gif()
        self.add_letter_text()

        self.add_picture_frame()
        self.add_name_picture()

        self.add_animation_button()
        self.add_reverse_button()

# Lighter bordered frame 15 px padding --------------
    def add_frame(self):     
        #create
        self.frame = Frame()
        self.frame.grid(row = 0, column = 0)
        #style
        self.frame.configure(bg = "#f66", padx = 15, pady = 15, width = 400)

# Global Frame ----------------------
    def add_global_frame(self):
        #create
        self.global_frame = Frame(self.frame)
        self.global_frame.grid(row = 0, column = 0)
        #style
        self.global_frame.configure(bg = "#f33", bd = 0, padx = 5, pady = 5)

    def add_heading_label(self):
        self.heading_label = Label(self.global_frame)
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(bg = "#f33", fg = "#fff", pady = 5, text = self.heading, font = "Arial 18")

    def add_post_button(self):
        self.post_button = Button(self.global_frame)
        self.post_button.grid(row=3, column=0)
        self.post_button.configure(bg = "#ff0", width = 52, text = self.post_button_text)
        #event
        self.post_button.bind("<ButtonRelease-1>", self.post_letter_handler)

    def post_letter_handler(self, event):
        self.letter_message = "Your letter has been sent!"
        self.entered_name = str(self.name_entry.get())
        self.is_name_entered = int(len(self.name_entry.get()))
        self.is_letter_entered = int(len(self.letter_text.get(1.0 , END)))-1
        print(self.is_letter_entered,self.is_name_entered )
        if self.is_name_entered >= 3 and self.is_letter_entered >= 3:      
            if self.entered_name == "Snowy":
                letter_message = self.letter_message + " Snowy is on its way!"
                messagebox.showinfo("Sent!", letter_message)
            elif self.entered_name == "Elfie":
                letter_message = self.letter_message + " The elf is on its way!"
                messagebox.showinfo("Sent!", letter_message)
            elif self.entered_name == "Rudolph":
                letter_message = self.letter_message + " The reindeer is shining its nose!"
                messagebox.showinfo("Sent!", letter_message)
            else:
                letter_message = self.letter_message
                messagebox.showinfo("Sent!", letter_message)
        elif self.is_name_entered < 3:
            messagebox.showinfo("Error!", "Please enter a name")

        elif self.is_letter_entered < 3:
            messagebox.showinfo("Error!", "Please enter a letter")

    def add_animation_button(self):
        #variable
        self.animation_variable = 0
        #create
        self.animation_button = Button(self.global_frame)
        self.animation_button.grid(row=4, column=0)
        self.animation_button.configure(bg = "#0ff", width = 52, text = self.animation_button_text)
        #event
        self.animation_button.bind("<ButtonRelease-1>", self.animation_button_clicked)

    def add_reverse_button(self):
        #variable
        self.reverse_var = 1
        #create
        self.reverse_button = Button(self.global_frame)
        self.reverse_button.grid(row=5, column=0)
        self.reverse_button.configure(bg = "#0ff", width = 52, text = "Reverse")
        #event
        self.reverse_button.bind("<ButtonRelease-1>", self.reverse_button_clicked)


# Content frame --------------------------
    def add_content_frame(self):
        #create
        self.content_frame = Frame(self.global_frame)
        self.content_frame.grid(row = 1, column = 0)
        #style
        self.content_frame.configure(bg = "#f33", bd = 5)

# Content ---------------------------

    def add_name_label(self):
        self.name_label = Label(self.content_frame)
        self.name_label.grid(row=0, column=0)
        self.name_label.configure(bg = "#f33", fg = "#fff", text = self.name_label_text, font = "Arial 12", pady = 5, padx=5)

    def add_name_entry(self):
        self.name_entry = Entry(self.content_frame)
        self.name_entry.grid(row=0, column=1)
        self.name_entry.configure(bg = "white", fg = "#f00",  width = 30, font = "Arial 12")
        #event
        self.name_entry.bind("<KeyRelease>", self.name_picture_change)

    def add_santa_gif(self):
        self.santa_gif = Label(self.content_frame)
        self.santa_gif.grid(row=1, column=0)
        self.santa_gif.configure(image = self.santa_image, bd = 0, padx =5, pady = 5)

    def add_letter_text(self):
        self.letter_text = Text(self.content_frame)
        self.letter_text.grid(row=1, column=1)
        self.letter_text.configure(bg = "white", fg = "#f00", height = 5, width = 30, font = "Arial 12", pady = 5)

# Picture frame --------------------------
    def add_picture_frame(self):
        #create
        self.picture_frame = Frame(self.global_frame)
        self.picture_frame.grid(row = 2, column = 0)
        #style
        self.picture_frame.configure(bg = "#f33", bd = 5)

    def add_name_picture(self):
        self.picture_variable = 1
        self.name_picture = Label(self.picture_frame)
        self.name_picture.grid(row = 0 , column = 0)
        self.name_picture.configure(image = self.unknown_image, bd = 2, pady = 10)
       
    def name_picture_change(self, event):
        self.entered_name = str(self.name_entry.get())
        if self.entered_name == "Snowy":
            self.picture_variable = 2
            self.name_picture.configure(image = self.snowman_image, bd = 2, pady = 10)
        elif self.entered_name == "Elfie":
            self.picture_variable = 3
            self.name_picture.configure(image = self.elf_image, bd = 2, pady = 10)
        elif self.entered_name == "Rudolph":
            self.picture_variable = 4
            self.name_picture.configure(image = self.reindeer_image, bd = 2, pady = 10)
        else:
            self.picture_variable = 1
            self.name_picture.configure(image = self.unknown_image, bd = 2, pady = 10)
        

    def animation_button_clicked(self, event):
        self.animation = Frame(self.frame)
        self.animation.grid(row=1, column=0)
        self.animation.configure(bg = "white", bd = 4, height = self.animation_window_height, width = self.animation_window_width)        
        self.animation_picture = Label(self.animation)
        self.animation_picture.place(x=self.image_x_pos, y=self.image_y_pos)
        self.animation_picture.configure(image=self.unknown_image , bd = 0)

        if self.picture_variable == 1:
            self.animation_picture.configure(image=self.unknown_image)
        elif self.picture_variable == 2:
            self.animation_picture.configure(image=self.snowman_image)
        elif self.picture_variable == 3:
            self.animation_picture.configure(image=self.elf_image)
        elif self.picture_variable == 4:
            self.animation_picture.configure(image=self.reindeer_image)

        if self.animation_variable <= 1:
            self.animation_variable += 1
        elif self.animation_variable == 2:
            self.animation_variable -= 1

        if self.animation_variable == 1:
            self.button_animation = "Stop Animation"
            self.animation_button.configure(bg = "#0ff", width = 52, text = self.button_animation)
            self.run_animation()    
        elif self.animation_variable == 2:
            self.button_animation = "Start Animation"
            self.animation_button.configure(bg = "#0ff", width = 52, text = self.button_animation)
            self.animation.configure(bg = "#eee", bd = 4, height = self.animation_window_height, width = self.animation_window_width) 
            self.tick_time += 4

    def run_animation(self):
        if self.picture_variable == 1:
            self.animation_picture.configure(image=self.unknown_image)
        elif self.picture_variable == 2:
            self.animation_picture.configure(image=self.snowman_image)
        elif self.picture_variable == 3:
            self.animation_picture.configure(image=self.elf_image)
        elif self.picture_variable == 4:
            self.animation_picture.configure(image=self.reindeer_image)

        posx = self.image_x_pos
        posy = self.image_y_pos
        changex = self.image_x_change * self.reverse_var
        changey = self.image_y_change * self.reverse_var

        if self.animation_variable == 1:
            if posx >= 11 and posx <= 322 and posy <= 10:
                self.image_x_pos = self.image_x_pos - changex
                self.animation_picture.place(x=self.image_x_pos, y=self.image_y_pos)
            
            elif posx == 10 and posy >= 10 and posy <= 130:
                self.image_y_pos = self.image_y_pos + changey
                self.animation_picture.place(x=self.image_x_pos, y=self.image_y_pos)
            
            elif posx >= 10 and posx <= 321 and posy == 131:
                self.image_x_pos = self.image_x_pos + changex
                self.animation_picture.place(x=self.image_x_pos, y=self.image_y_pos)
            
            elif posx == 323 and posy >= 10 and posy <= 132:
                self.image_y_pos = self.image_y_pos - changey
                self.animation_picture.place(x=self.image_x_pos, y=self.image_y_pos)
        
        # ticker
        self.after(self.tick_time, self.run_animation)
        print(self.image_x_pos, self.image_y_pos)

    def reverse_button_clicked(self, event):
        self.reverse_var = self.reverse_var * (-1)


# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()