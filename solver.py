import tkinter as tk
from tkinter import ttk
from circuit import Circuit
from PIL import ImageTk,Image

class Solver(ttk.Frame):
    def __init__(self, parent, height, width):
        super().__init__(parent)

        self.height = int(height)
        self.width = int(width)

        self["height"] = self.height
        self["width"] = self.width

        self.parent = parent
    
        # BACKGROUND_PATH = "Assets/team1_background.jpg"
        # background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((self.width, self.height), Image.ANTIALIAS))
        # background_label = tk.Label(self, image=background_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # background_label.image = background_image

        self.circuit = Circuit(self, height=height, width=width)
        self.circuit.grid(row=0, column=0, sticky="NSEW")



    
    