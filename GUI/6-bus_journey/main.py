from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.directions_image = PhotoImage(file="U:\Documents\Problem Solving\COM404\GUI\\6-bus_journey\directions.gif")
        self.bus_image = PhotoImage(file="U:\Documents\Problem Solving\COM404\GUI\\6-bus_journey\\bus.gif")

        self.bus_x_pos = 11
        self.bus_y_pos = 11

        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_main_frame()
        self.add_heading_label()
        self.add_secondary_frame()
        self.add_dirctions_image()
        self.add_bus_image()

    def add_main_frame(self):
        self.main_frame = Frame()
        self.main_frame.grid(row = 0, column = 0)
        self.main_frame.configure(bg = "light grey", bd = 4)
        
    def add_heading_label(self):
        self.heading_label = Label(self.main_frame)
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(bg = "light grey", text = "Bus Journey", font = "Arial 16")

    def add_secondary_frame(self):
        self.secondary_frame = Frame()
        self.secondary_frame.grid(row = 1, column = 0)
        self.secondary_frame.configure(bg = "light grey", bd = 4,width = 616, height = 396)

    def add_dirctions_image(self):
        self.direction_image = Label(self.secondary_frame)
        self.direction_image.place(x=1,y=1)
        self.direction_image.configure(image=self.directions_image, height=380, width=600)
        #Event
        self.direction_image.bind("<B1-Motion>", self.callback)

    def add_bus_image(self):
        self.buss_image = Label(self.secondary_frame)
        self.buss_image.place(x=self.bus_x_pos,y=self.bus_y_pos)
        self.buss_image.configure(image=self.bus_image, height = 30, width = 60)

    def callback(self, event):
        self.bus_x_pos = event.x
        self.bus_y_pos = event.y 
        print(self.bus_x_pos, self.bus_y_pos)
        self.buss_image.place(x=self.bus_x_pos,y=self.bus_y_pos)
        self.buss_image.configure(image=self.bus_image, height = 30, width = 60)

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()