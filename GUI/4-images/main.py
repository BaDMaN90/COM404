from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="U:\Documents\Problem Solving\COM404\GUI\\4-images\\ambulance.gif")
        self.bike_image = PhotoImage(file="U:\Documents\Problem Solving\COM404\GUI\\4-images\\Bike.gif")  
        self.plane_image = PhotoImage(file="U:\Documents\Problem Solving\COM404\GUI\\4-images\\plane.gif")                  
        # set window attributes
        self.title("Gui")
        

        
        # add components
        self.add_main_frame()
        self.add_transport_label()
        self.add_ambulance_image_label()
        self.add_bike_image_label()
        self.add_plane_image_label()

    def add_main_frame(self):
        self.main_frame = Frame()
        self.main_frame.grid(row = 0, column = 0)
        self.main_frame.configure(bg = "black", bd = 4)


    def add_transport_label(self):
        self.transport_label = Label(self.main_frame)
        self.transport_label.grid(columnspan=3, row=0, column=0)
        self.transport_label.configure(width = 16, justify = CENTER, text = "TRANSPORT", font = "Arial 16")
        
    def add_ambulance_image_label(self):
        self.ambulance_image_label = Label(self.main_frame)
        self.ambulance_image_label.grid(row=1, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image, height=62, width=62)

    def add_bike_image_label(self):
        self.ambulance_image_label = Label(self.main_frame)
        self.ambulance_image_label.grid(row=1, column=1)
        self.ambulance_image_label.configure(image=self.bike_image, height=62, width=62)
 
    def add_plane_image_label(self):
        self.ambulance_image_label = Label(self.main_frame)
        self.ambulance_image_label.grid(row=1, column=2)
        self.ambulance_image_label.configure(image=self.plane_image, height=62, width=62)
 

# Create an object of the Gui class when this module is executed
#if (__name__ == "__main__"):
gui = Gui()
gui.mainloop()