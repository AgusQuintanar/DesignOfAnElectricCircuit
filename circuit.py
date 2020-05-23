import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from circuit_drawing import Circuit_Drawing
from circuit_graph import Circuit_Graph

class Circuit(ttk.Frame):
    def __init__(self, parent, height, width):
        super().__init__(parent)

        self.parent = parent

        self.height = height
        self.width = width

        self["height"] = self.height
        self["width"] = self.width
        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(0) #disables grid shrinking

        BACKGROUND_PATH = "Assets/circuit4.png"
        self.BACKGROUND_IMAGE = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((int(self.width), int(self.height)), Image.ANTIALIAS))
        
        self.frames = {}
        self.resistance = 0
        self.inductance = 0
        self.capacitance = 0

        container = ttk.Frame(self)
        container["height"] = self.height
        container["width"] = self.width
        container.grid()
        container.columnconfigure(0, weight=1)

        circuit_drawing  =  Circuit_Drawing (
                                container,
                                self, 
                                lambda: self.show_frame(Circuit_Graph), 
                            )

        circuit_graph =     Circuit_Graph (
                                container, 
                                self, 
                                lambda: self.show_frame(Circuit_Drawing), 
                            )

        circuit_drawing.grid(row=0, column=0, sticky="NESW")
        circuit_graph.grid(row=0, column=0, sticky="NESW")

        self.frames[Circuit_Drawing] = circuit_drawing
        self.frames[Circuit_Graph] = circuit_graph
        
        self.show_frame(Circuit_Drawing)
        
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

       



    


    


        


        
    
