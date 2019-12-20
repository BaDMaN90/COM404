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
        letter_message = "Your letter has been posted!"
        messagebox.showinfo("Sent!", letter_message)

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
        self.example_textbox = Entry(self.content_frame)
        self.example_textbox.grid(row=0, column=1)
        self.example_textbox.configure(bg = "white", fg = "#f00",  width = 30, font = "Arial 12")

    def add_santa_gif(self):
        self.santa_gif = Label(self.content_frame)
        self.santa_gif.grid(row=1, column=0)
        self.santa_gif.configure(image = self.santa_image, bd = 0, padx =5, pady = 5)

    def add_letter_text(self):
        self.letter_entry = Text(self.content_frame)
        self.letter_entry.grid(row=1, column=1)
        self.letter_entry.configure(bg = "white", fg = "#f00", height = 5, width = 30, font = "Arial 12", pady = 5)


# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()