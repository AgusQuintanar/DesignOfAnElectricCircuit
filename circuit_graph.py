import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Circuit_Graph(ttk.Frame):
    def __init__(self, container, circuit, show_main_panel):
        super().__init__(container)

        self.circuit = circuit

        self.height = self.circuit.height
        self.width = self.circuit.width

        self["height"] = self.height
        self["width"] = self.width
        self["style"] = "BackgroundORANGE.TFrame"

        # background_label = tk.Label(self, image=self.circuit.BACKGROUND_IMAGE)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # background_label.image = self.circuit.BACKGROUND_IMAGE

        self.grid_propagate(0) #disables grid shrinking

        # I_ICON_PATH = "Assets/i_icon.png"
        # i_icon_image = ImageTk.PhotoImage(Image.open(I_ICON_PATH).resize((int(.07*self.width), int(.125*self.height)), Image.ANTIALIAS))
        info_button = tk.Button(
            self, 
            # image=i_icon_image, 
            text = "Show Drawing",
            borderwidth=0, 
            highlightthickness=0, 
            padx=0,
            pady=0,
            cursor="hand2",
            command=show_main_panel
        )
        info_button.grid(row=3, column=4, pady=(7, 0), padx=(19,0))
        # info_button.image = i_icon_image
