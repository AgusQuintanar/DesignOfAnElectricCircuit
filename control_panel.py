import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Control_Panel(ttk.Frame):
    def __init__(self, parent, height, width):
        super().__init__(parent)

        self.height = int(height)
        self.width = int(width)

        self.dashboard = parent

        self["height"] = self.height
        self["width"] =  self.width
        self["style"] = "BackgroundControlPanel.TFrame"

        self.grid_propagate(0) #disables grid shrinking

        self.disipation_ratio = tk.DoubleVar()
        self.time = tk.DoubleVar()

        self.disipation_ratio.trace("w", self.dashboard.handle_entries_change)
        self.time.trace("w", self.dashboard.handle_entries_change)


        label_disipation_tag = ttk.Label(
            self,
            text= 'Disipation Ratio (0, 1]',
            style="LightText6.TLabel"
        )
        label_disipation_tag.grid(column=0, row=0, sticky="EW", padx=(int(.175*self.width),int(.05*self.width)), pady=(int(.05*self.height),0))


        disipation_ratio = tk.Scale (
            self,
            orient="vertical",
            from_=0.0001,
            to=1,
            variable=self.disipation_ratio,
            length=int(.3*self.height),
            tickinterval=.9999, 
            resolution=0.0001,
            font="Helvetica 16",
            foreground="#bfbfbf",
            background="#222a2e",
            troughcolor='#04a7e0',
            activebackground='#1065BF',
            sliderrelief='flat',
            highlightthickness=0
        )

        disipation_ratio.grid(column=0, row=1, sticky="NS", padx=int(.35*self.width), pady=(int(.05*self.height),int(.05*self.height)))


        label_time_tag = ttk.Label(
            self, 
            text='Interval of Time (s)',
            style="LightText6.TLabel"
        )
        label_time_tag.grid(column=0, row=2, sticky="EW", padx=(int(.25*self.width), int(.3*self.width)), pady=(int(.05*self.height),0))

        entry_time = ttk.Entry(
            self, 
            style="LightTextEntry7.TLabel",
            textvariable=self.time,
            width = 10,
            font="Helvetica 20",
            justify='center'
        )
        entry_time.grid(column=0, row=3, sticky="EW", padx=(int(.25*self.width),int(.3*self.width)), pady=(15,15))


        calculate_button = ttk.Button(
                    self, 
                    cursor="hand2",
                    style="Button.TButton",
                    text="Calculate Resistance",
                    command=self.dashboard.calculate_resistance,
                    )
        calculate_button.grid(row=5, column=0, padx=(int(.0*self.width),int(.05*self.width)), pady=(.1*self.height, 10))
        # settings_button.image = settings_button_image



        

        