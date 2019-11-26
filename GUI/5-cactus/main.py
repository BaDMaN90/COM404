from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.cacti_image = PhotoImage(file="U:\Documents\Problem Solving\COM404\GUI\\5-cactus\cactus1.gif")
        self.cacti_image_with_name = PhotoImage(file="U:\Documents\Problem Solving\COM404\GUI\\5-cactus\cactus2.gif")

        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_heading_label()
        self.add_cactus_picture()
        self.add_button_flip()

        
    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(text = "Cactus Leaves", font = "Arial 16")

    def add_cactus_picture(self):
        self.cactus_picture = Label()
        self.cactus_picture.grid(row=1, column=0)
        self.cactus_picture.configure(image=self.cacti_image, height=200, width=350)

    def add_button_flip(self):
        # create
        self.button_flip = Button()
        self.button_flip.grid(row=2, column = 0)
        # style
        self.button_flip.configure(text = "Flip", font = "Arial 16")
        # events
        self.button_flip.bind("<ButtonRelease-1>", self.button_flip_left_click)
        self.button_flip.bind("<ButtonRelease-3>", self.button_flip_right_click)
  
    def button_flip_left_click(self, event):
        self.cactus_picture.configure(image=self.cacti_image, height=200, width=350)


    def button_flip_right_click(self, event):
        self.cactus_picture.configure(image = self.cacti_image_with_name, height=200, width=350)


# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()