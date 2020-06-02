import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Control_Panel(ttk.Frame):
    def __init__(self, parent, height, width):
        super().__init__(parent)

        self.height = int(height)
        self.width = int(width)

        self.parent = parent

        print(self.parent.controller)


        self["height"] = self.height
        self["width"] =  self.width
        self["style"] = "BackgroundBLACK.TFrame"

        self.grid_propagate(0) #disables grid shrinking

        # BACKGROUND_PATH = "Assets/panel_background.jpg"
        # background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((int(self.width), int(self.height)), Image.ANTIALIAS))
        # background_label = tk.Label(self, image=background_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # background_label.image = background_image

    
        # IMAGE_SETTINGS_BUTTON_PATH = "Assets/settings_icon.png" 
        # settings_button_image = ImageTk.PhotoImage(Image.open(IMAGE_SETTINGS_BUTTON_PATH).resize((int(.056*self.width), int(.48*self.height)), Image.ANTIALIAS))

        settings_button = tk.Button(
                    self, 
                    # image=settings_button_image, 
                    borderwidth=0, 
                    highlightthickness=0, 
                    padx=0,
                    pady=0,
                    cursor="hand2",
                    #command=
                    )
        settings_button.grid(row=0, column=4, pady=(10, 10), padx=(int(.3*self.width),20))
        # settings_button.image = settings_button_image



        

        