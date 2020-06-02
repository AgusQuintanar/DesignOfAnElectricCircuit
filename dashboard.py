import tkinter as tk
from tkinter import ttk
from circuit import Circuit
from control_panel import Control_Panel
from PIL import Image, ImageTk


class Dashboard(ttk.Frame):
    def __init__(self, parent, controller, show_settings, height, width):
        super().__init__(parent)

        self["style"] = "Background.TFrame"
        self["height"] = height
        self["width"] = width

        self.parent = parent

        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

 
        self.circuit = Circuit(self, height=height, width=.75*width)
        self.circuit.grid(row=0, column=0, sticky="NSEW")

        self.control_panel = Control_Panel(self, height=height, width=.25*width)
        self.control_panel.grid(row=0, column=1, sticky="NSEW")

    

      


  


      


    
   