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

        label_title = ttk.Label(
            self, 
            text='Design of an Electric Circuit',
            style="LightText8.TLabel"
        )
        label_title.grid(column=0, row=0, columnspan=3, sticky="EW", padx=(int(.075*self.width), int(.0*self.width)), pady=(int(.05*self.height),int(.05*self.height)))

        # label_voltage_tag = ttk.Label(
        #     self, 
        #     text=' Voltage (V)',
        #     style="LightText.TLabel"
        # )
        # label_voltage_tag.grid(column=0, row=1, sticky="EW", padx=(int(.125*self.width),int(.125*self.width)), pady=(int(.455*self.height),0))

        # entry_voltage = ttk.Entry(
        #     self, 
        #     style="LightTextEntry4.TLabel",
        #     textvariable=self.circuit.voltage,
        #     width = 10,
        #     font="Helvetica 20",
        #     justify='center'
        # )
        # entry_voltage.grid(column=0, row=2, sticky="EW", padx=(int(.125*self.width), int(.125*self.width)), pady=(15,0))

        label_capacitance_tag = ttk.Label(
            self, 
            text='Capacitance (F)',
            style="LightText.TLabel"
        )
        label_capacitance_tag.grid(column=1, row=1, sticky="EW", padx=(int(.22*self.width), int(.3*self.width)), pady=(int(.25*self.height),0))

        entry_capacitance = ttk.Entry(
            self, 
            style="LightTextEntry.TLabel",
            textvariable=self.circuit.capacitance,
            width = 10,
            font="Helvetica 20",
            justify='center'
        )
        entry_capacitance.grid(column=1, row=2, sticky="EW", padx=(int(.22*self.width),int(.3*self.width)), pady=(15,0))

        label_inductance_tag = ttk.Label(
            self, 
            text='Inductance (H)',
            style="LightText.TLabel",
            justify='center'
        )
        label_inductance_tag.grid(column=2, row=1, sticky="EW", padx=(0,130), pady=(int(.25*self.height),0))

        entry_inductance = ttk.Entry(
            self, 
            style="LightTextEntry2.TLabel",
            textvariable=self.circuit.inductance,
            width = 10,
            font="Helvetica 20",
            justify='center'
        )
        entry_inductance.grid(column=2, row=2, sticky="EW", padx=(0,130), pady=(15,0))

        label_resistance_tag = ttk.Label(
            self,
            text= 'Resistance (Ω)',
            style="LightText.TLabel"
        )
        label_resistance_tag.grid(column=1, row=3, sticky="EW", padx=(int(.34*self.width),int(.2*self.width)), pady=(int(.275*self.height),0))

        # entry_resistance = tk.Entry(
        #     self, 
        #     textvariable=self.circuit.resistance,
        #     width = 10,
        #     font="Helvetica 20",
        #     disabledforeground='#f0f5f3',
        #     justify='center',
        #     state='disabled',
        #     disabledbackground="#978fdb",
        # )

        entry_resistance = ttk.Label(
            self, 
            style="LightTextEntry3.TLabel",
            textvariable=self.circuit.resistance,
            width = .13*self.width,
            font="Helvetica 20",
            justify='center',
            anchor="center"
        )
        entry_resistance.grid(column=1, row=4, sticky="EW", padx=(int(.34*self.width),int(.2*self.width)), pady=(15,0))

       

        self.show_button = ttk.Button(
            self, 
            text = "Show Graph",
            cursor="hand2",
            command=show_info_panel,
            style="Button.TButton",
        )
        self.show_button.grid(row=4, column=0, pady=(10, 0), padx=(int(.05*self.width),0))
        # info_button.image = i_icon_image
