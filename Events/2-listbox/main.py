from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Song Maker")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_lyric_entry()
        self.__add_lyric_button()
        self.__add_instruction_label_2()
        self.__add_lyric_listbox()
        self.lyrics_index = 1
        
    def __add_heading_label(self):
        # create
        self.add_heading_label = Label()
        self.add_heading_label.grid(sticky="e",row=0, column=0)
        # style
        self.add_heading_label.configure(font = "Arial 30",text="Song Maker")
        
    def __add_instruction_label(self):
        # create
        self.add_instruction_label = Label()
        self.add_instruction_label.grid(sticky="W",row=1, column=0) 
        # style
        self.add_instruction_label.configure(font = "Arial 18",text="Lyrics to add:")   

    def __add_lyric_entry(self):
        # create
        self.add_lyric_entry = Entry()
        self.add_lyric_entry.grid(row=2, column=0)
        # style
        self.add_lyric_entry.configure(bd=4,width = 20,font = "Arial 18")

    def __add_lyric_button(self):
        # create
        self.add_lyric_button = Button()
        self.add_lyric_button.grid(row=2, column=1)

        # style
        self.add_lyric_button.configure(bd=4,text="Add",width = 10)

        #events
        self.add_lyric_button.bind("<ButtonRelease-1>", self.__add_lyric_clicked)

    def __add_instruction_label_2(self):
        # create
        self.add_instruction_label_2 = Label()
        self.add_instruction_label_2.grid(sticky="W",row=3, column=0) 
        # style
        self.add_instruction_label_2.configure(font = "Arial 18",text="Lyrics:")

    def __add_lyric_listbox(self):
        # create
        self.add_lyric_Listbox = Listbox()
        
        self.add_lyric_Listbox.grid(row=4, column=0, columnspan = 2)
        # style
        self.add_lyric_Listbox.configure(selectmode = "multiple",bd=4,width = 60)
        
 
    def __add_lyric_clicked(self, event):
        self.add_lyric_Listbox.insert(self.lyrics_index, self.add_lyric_entry.get())
        self.lyrics_index +=1

gui = Gui()
gui.mainloop() 