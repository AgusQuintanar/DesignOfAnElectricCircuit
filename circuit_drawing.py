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

        background_label = tk.Label(self, image=self.circuit.BACKGROUND_IMAGE)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = self.circuit.BACKGROUND_IMAGE

        self.grid_propagate(0) #disables grid shrinking



        label_x_tag = ttk.Label(
            self, 
            text='X:',
            style="LightText.TLabel"
        )
        label_x_tag.grid(column=1, row=0, sticky="EW", padx=(30,10), pady=(70,10))

        # label_x = ttk.Label( ###### Change to input box
        #     self, 
        #     textvariable=self.circuit.x,
        #     style="LightText.TLabel"
        # )
        # label_x.grid(column=2, row=0, sticky="EW", padx=(10,50), pady=(70,10))

        label_y_tag = ttk.Label(
            self, 
            text='Y:',
            style="LightText.TLabel"
        )
        label_y_tag.grid(column=3, row=0, sticky="EW", padx=(20,10), pady=(70,10))

        # label_y = ttk.Label(
        #     self, 
        #     textvariable=self.circuit.y,
        #     style="LightText.TLabel"
        # )
        # label_y.grid(column=4, row=0, sticky="EW", padx=(10,50), pady=(70,10))

        label_vision_angle_tag = ttk.Label(
            self,
            text= 'Vision Angle:',
            style="LightText.TLabel"
        )
        label_vision_angle_tag.grid(column=1, row=1, sticky="EW", padx=(30,0), pady=(10,10), columnspan=2)

        # label_vision_angle = ttk.Label(
        #     self,
        #     textvariable=self.circuit.vision_angle,
        #     style="LightText.TLabel"
        # )
        # label_vision_angle.grid(column=3, row=1, sticky="EW", padx=(30,0), pady=(10,10), columnspan=2)

        
        # I_ICON_PATH = "Assets/i_icon.png"
        # i_icon_image = ImageTk.PhotoImage(Image.open(I_ICON_PATH).resize((int(.07*self.width), int(.125*self.height)), Image.ANTIALIAS))

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
        info_button.grid(row=2, column=1, columnspan=5, pady=(10, 0), padx=(int(self.width*.62),0))
        # info_button.image = i_icon_image
