import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Circuit_Drawing(ttk.Frame):
    def __init__(self, container, circuit, show_info_panel):
        super().__init__(container)

        self.circuit = circuit

        self.height = self.circuit.height
        self.width = self.circuit.width

        self["height"] = self.height
        self["width"] = self.width
        
        self["style"] = "BackgroundRED.TFrame"

        PAD_Y = int(self.height/5)

        background_label = tk.Label(self, image=self.circuit.BACKGROUND_IMAGE)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = self.circuit.BACKGROUND_IMAGE

        self.grid_propagate(0) #disables grid shrinking


        label_capacitance_tag = ttk.Label(
            self, 
            text='Capacitance',
            style="LightText.TLabel"
        )
        label_capacitance_tag.grid(column=1, row=1, sticky="EW", padx=(int(.415*self.width),10), pady=(int(.455*self.height),0))

        entry_capacitance = ttk.Entry(
            self, 
            style="LightTextEntry.TLabel",
            textvariable=self.circuit.capacitance,
            width = 10,
            font="Helvetica 20"
        )
        entry_capacitance.grid(column=1, row=2, sticky="EW", padx=(int(.415*self.width),10), pady=(15,0))

        label_inductance_tag = ttk.Label(
            self, 
            text='Inductance',
            style="LightText.TLabel"
        )
        label_inductance_tag.grid(column=2, row=1, sticky="EW", padx=(int(.325*self.width),130), pady=(int(.455*self.height),0))

        entry_inductance = ttk.Entry(
            self, 
            style="LightTextEntry.TLabel",
            textvariable=self.circuit.inductance,
            width = 10,
            font="Helvetica 20"
        )
        entry_inductance.grid(column=2, row=2, sticky="EW", padx=(int(.325*self.width),130), pady=(15,0))

        label_resistance_tag = ttk.Label(
            self,
            text= 'Resistance',
            style="LightText.TLabel"
        )
        label_resistance_tag.grid(column=2, row=3, sticky="EW", padx=(0,int(.45*self.width)), pady=(int(.275*self.height),0))

        entry_resistance = ttk.Entry(
            self, 
            style="LightTextEntry.TLabel",
            textvariable=self.circuit.resistance,
            width = 10,
            font="Helvetica 20"
        )
        entry_resistance.grid(column=2, row=4, sticky="EW", padx=(0,int(.45*self.width)), pady=(15,0))

       

        info_button = tk.Button(
            self, 
            # image=i_icon_image, 
            text = "Show Graph",
            borderwidth=0, 
            highlightthickness=0, 
            padx=0,
            pady=0,
            cursor="hand2",
            command=show_info_panel
        )
        info_button.grid(row=4, column=1, pady=(10, 0), padx=(0,0))
        # info_button.image = i_icon_image
