import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from circuit import Circuit
from control_panel import Control_Panel
from PIL import Image, ImageTk
from circuit_drawing import Circuit_Drawing
import function
import bisection
import graph

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
        if (self._validate_entries()): #Only calculates resistance when all validations are met
            self.circuit.frames[Circuit_Drawing].show_button["state"] = "normal"
            self.func = function.get_func(
                float(self.control_panel.time.get()), 
                float(self.circuit.inductance.get()), 
                float(self.circuit.capacitance.get()), 
                float(self.control_panel.disipation_ratio.get())
            )
            self.start, self.end = function.get_range(
                float(self.circuit.inductance.get()), 
                float(self.circuit.capacitance.get())
            )
            resistance = bisection.solve(self.func, self.start, self.end, 1000, .001)
            self.circuit.resistance.set(f'{resistance:.2f}')

    def handle_entries_change(self, *args):
        self.circuit.frames[Circuit_Drawing].show_button["state"] = "disabled"
    
    def show_graph(self):
        if self.func is not None:
            graph.plot(self.func, self.start, self.end)  
        print(self.end)  

    def _is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def _validate_entry(self, entry_name, entry_value, errors, passed_validations):
        if self._is_float(entry_value):
            if float(entry_value) <= 0:
                errors += f"{entry_name} must be grater than 0.\n" 
                passed_validations = False
        else:
            errors += f"{entry_name} must be a valid a number.\n" 
            passed_validations = False
        return (errors, passed_validations)

    def _validate_entries(self):
        errors = ""
        passed_validations = True

        errors, passed_validations = self._validate_entry("Inductance (H)",  self.circuit.inductance.get(), errors, passed_validations)
        errors, passed_validations = self._validate_entry("Capacitance (F)", self.circuit.capacitance.get(), errors, passed_validations)
        errors, passed_validations = self._validate_entry("Disipation Ratio", self.control_panel.disipation_ratio.get(), errors, passed_validations)
        errors, passed_validations = self._validate_entry("Interval of Time (s)", self.control_panel.time.get(), errors, passed_validations)

        if not passed_validations:
            messagebox.showerror("Invalid Entries", errors)
            print(errors)

        return passed_validations


      

  


      


    
   