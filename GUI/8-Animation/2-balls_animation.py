from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.image_one = PhotoImage(file="U:\Documents\Problem Solving\COM404\GUI\8-Animation\\bike.gif")
        self.image_two = PhotoImage(file="U:\Documents\Problem Solving\COM404\GUI\8-Animation\\plane.gif")
  
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.image1_x_pos = 100
        self.image1_y_pos = 0
        self.image1_x_change = 1
        self.image1_y_change = 1

        self.image2_x_pos = 200
        self.image2_y_pos = 0
        self.image2_x_change = 1
        self.image2_y_change = 1
        
        # add components
        self.add_image1_label() 
        self.add_image2_label() 

        # start the timer
        self.image_one_tick()
        self.image_two_tick()

    # the timer tick function    
    def image_one_tick(self):
        posx = self.image1_x_pos
        posy = self.image1_y_pos
        changex = self.image1_x_change
        changey = self.image1_y_change
        if posx >= 100 and posx <= 499 and posy >= 0 and posy <= 399:
            self.image1_x_pos = self.image1_x_pos + changex
            self.image1_y_pos = self.image1_y_pos + changey
            self.image1_label.place(x=self.image1_x_pos, y=self.image1_y_pos)
        
        elif posx >= 401 and posx <= 500 and posy >= 400 and posy <= 498:
            self.image1_x_pos = self.image1_x_pos - changex
            self.image1_y_pos = self.image1_y_pos + changey
            self.image1_label.place(x=self.image1_x_pos, y=self.image1_y_pos)
        
        elif posx >= 0 and posx <= 401 and posy >= 100 and posy <= 500:
            self.image1_x_pos = self.image1_x_pos - changex
            self.image1_y_pos = self.image1_y_pos - changey
            self.image1_label.place(x=self.image1_x_pos, y=self.image1_y_pos)
        
        elif posx >= 0 and posx <= 99 and posy >= 0 and posy <= 99:
            self.image1_x_pos = self.image1_x_pos + changex
            self.image1_y_pos = self.image1_y_pos - changey
            self.image1_label.place(x=self.image1_x_pos, y=self.image1_y_pos)
        else:
            pass
        # ticker
        print(self.image1_x_pos, self.image1_y_pos)
        self.after(10, self.image_one_tick)

    def image_two_tick(self):
        posx = self.image2_x_pos + 50
        posy = self.image2_y_pos + 50
        changex = self.image2_x_change
        changey = self.image2_y_change
        if posx >= 0 and posx <= 250 and posy >= 0 and posy <= 250:
            self.image2_x_pos = self.image2_x_pos - changex
            self.image2_y_pos = self.image2_y_pos + changey
            self.image2_label.place(x=self.image2_x_pos, y=self.image2_y_pos)
        
        elif posx >= 0 and posx <= 250 and posy >= 251 and posy <= 500:
            self.image2_x_pos = self.image2_x_pos + changex
            self.image2_y_pos = self.image2_y_pos + changey
            self.image2_label.place(x=self.image2_x_pos, y=self.image2_y_pos)
        
        elif posx >= 251 and posx <= 500 and posy >= 251 and posy <= 500:
            self.image2_x_pos = self.image2_x_pos + changex
            self.image2_y_pos = self.image2_y_pos - changey
            self.image2_label.place(x=self.image2_x_pos, y=self.image2_y_pos)
        
        else:
            self.image2_x_pos = self.image2_x_pos - changex
            self.image2_y_pos = self.image2_y_pos - changey
            self.image2_label.place(x=self.image2_x_pos, y=self.image2_y_pos)
        
        # ticker
        self.after(10, self.image_two_tick)

    # the images
    def add_image1_label(self):
        self.image1_label = Label()
        self.image1_label.place(x=self.image1_x_pos, y=self.image1_y_pos)
        self.image1_label.configure(image=self.image_one)

    def add_image2_label(self):
        self.image2_label = Label()
        self.image2_label.place(x=self.image2_x_pos, y=self.image2_y_pos)
        self.image2_label.configure(image=self.image_two)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 