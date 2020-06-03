import tkinter as tk
from tkinter import ttk
from circuit import Circuit
from control_panel import Control_Panel
from PIL import Image, ImageTk
from circuit_drawing import Circuit_Drawing
import function
import bisection

class Dashboard(ttk.Frame):
    def __init__(self, parent, controller, show_settings, height, width):
        super().__init__(parent)

        self["style"] = "Background.TFrame"
        self["height"] = height
        self["width"] = width

        self.parent = parent

        self.func = None 
        self.start, self.end = 0, 0

        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
 
        self.circuit = Circuit(self, height=height, width=.8*width)
        self.circuit.grid(row=0, column=0, sticky="NSEW")

        self.control_panel = Control_Panel(self, height=height, width=.2*width)
        self.control_panel.grid(row=0, column=1, sticky="NSEW")

        self.handle_entries_change()

        


    def calculate_resistance(self):
        self.circuit.frames[Circuit_Drawing].show_button["state"] = "normal"
        self.func = function.get_func(self.control_panel.time.get(), self.circuit.inductance.get(), self.circuit.capacitance.get(), self.control_panel.disipation_ratio.get())
        self.start, selfend = function.get_range(self.circuit.inductance.get(), self.circuit.capacitance.get())
        resistance = bisection.solve(func, self.start, self.end, 1000, .001)
        self.circuit.resistance.set(f'{resistance:.2f}')



    def handle_entries_change(self, *args):
        self.circuit.frames[Circuit_Drawing].show_button["state"] = "disabled"
    

      


  


      


    
   