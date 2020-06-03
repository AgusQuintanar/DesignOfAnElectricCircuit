import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import graph

class Circuit_Graph(ttk.Frame):
    def __init__(self, container, circuit, show_main_panel):
        super().__init__(container)

        self.circuit = circuit

        self.height = self.circuit.height
        self.width = self.circuit.width

        self["height"] = self.height
        self["width"] = self.width
        self["style"] = "BackgroundGraph.TFrame"

        self.grid_propagate(0) #disables grid shrinking

        #graph.plot(self.circuit.dashboard.func, self.circuit.dashboard.start, self.circuit.dashboard.end)

    
        info_button = ttk.Button(
            self, 
            # image=i_icon_image, 
            text = "Show Drawing",
            cursor="hand2",
            command=show_main_panel,
            style="Button.TButton"
        )
        info_button.grid(row=3, column=4, pady=(7, 0), padx=(19,0))
        # info_button.image = i_icon_image
