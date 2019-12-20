from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_image = PhotoImage(file="U:\Documents\Problem Solving\COM404\GUI\8-Animation\\ball.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.ball_x_pos = 200
        self.ball_y_pos = 0
        self.ball_x_change = 1
        self.ball_y_change = 1
        
        # add components
        self.add_ball_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        bxpos = self.ball_x_pos + 50
        bypos = self.ball_y_pos + 50
        bxcha = self.ball_x_change
        bycha = self.ball_y_change
        if bxpos >= 0 and bxpos <= 250 and bypos >= 0 and bypos <= 250:
            self.ball_x_pos = self.ball_x_pos + self.ball_x_change
            self.ball_y_pos = self.ball_y_pos - self.ball_y_change
            self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        
        elif bxpos >= 251 and bxpos <= 500 and bypos >= 0 and bypos <= 250:
            self.ball_x_pos = self.ball_x_pos + self.ball_x_change
            self.ball_y_pos = self.ball_y_pos + self.ball_y_change
            self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        
        elif bxpos >= 251 and bxpos <= 500 and bypos >= 251 and bypos <= 500:
            self.ball_x_pos = self.ball_x_pos - self.ball_x_change
            self.ball_y_pos = self.ball_y_pos + self.ball_y_change
            self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        
        else:
            self.ball_x_pos = self.ball_x_pos - self.ball_x_change
            self.ball_y_pos = self.ball_y_pos - self.ball_y_change
            self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        
        # ticker
        self.after(10, self.tick)

    # the ball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 