from tkinter import ttk
import tkinter as tk
from dashboard import Dashboard


COLOR_PRIMARY = "#fff8e7"
COLOR_SECONDARY = "#293846"
COLOR_LIGHT_BACKGROUND = "#fff8e7"
COLOR_LIGHT_TEXT = "#eee"
COLOR_DARK_TEXT = "#8095a8"


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Dashboard.TFrame", background=COLOR_LIGHT_BACKGROUND)

        style.configure("BackgroundRED.TFrame", background="red")
        style.configure("BackgroundBLUE.TFrame", background="blue")
        style.configure("BackgroundGREEN.TFrame", background="green")
        style.configure("BackgroundYELLOW.TFrame", background="yellow")
        style.configure("BackgroundPURPLE.TFrame", background="purple")
        style.configure("BackgroundWHITE.TFrame", background="white")
        style.configure("BackgroundORANGE.TFrame", background="orange")
        style.configure("BackgroundDM.TFrame", background="#1e262b")


        style.configure("Background.TFrame", background=COLOR_PRIMARY)
        style.configure(
            "Dashboard.TLabel",
            background=COLOR_LIGHT_BACKGROUND,
            foreground=COLOR_DARK_TEXT,
            font="Courier 46"
        )

        style.configure(
            "LightText.TLabel",
            background="blue",
            foreground="white",
            font=("TkDefaultFont", 22)
        )

        style.configure(
            "LightTextEntry.TLabel",
            background="black",
            foreground="white",
            font=("TkDefaultFont", 20)
        )

        style.configure(
            "Button.TButton",
            background=[COLOR_SECONDARY],
            foreground=COLOR_LIGHT_TEXT,
            font=("TkDefaultFont", 11)
        )

        style.configure(
            "info_button.TButton",
            background="black",
            foreground="white",
            font=("TkDefaultFont", 11)
        )

        style.map(
            "Button.TButton",
            background=[("active", COLOR_PRIMARY), ("disabled", COLOR_LIGHT_TEXT)]
        )

        SCREEN_WIDTH = self.winfo_screenwidth()
        SCREEN_HEIGHT = self.winfo_screenheight()

        self["background"] = COLOR_PRIMARY

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        container = ttk.Frame(self)
        container["height"] = SCREEN_HEIGHT
        container["width"] = SCREEN_WIDTH
        container.grid()
        container.columnconfigure(0, weight=1)

        self.frames = {}

        dashboard_frame = Dashboard(container, self, lambda: self.show_frame(Dashboard), height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
        dashboard_frame.grid(row=0, column=0, sticky="NESW")

        self.frames[Dashboard] = dashboard_frame
        
        self.show_frame(Dashboard)

        self.title('Design Of An Electric Circuit')
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.resizable(False, False)

        print(SCREEN_HEIGHT, SCREEN_WIDTH)

        self.update()
        
       
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

if __name__ == '__main__':        
    root = Main()
    root.mainloop()
   



