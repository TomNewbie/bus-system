'''
    DEBUGGER GUI for run_model
'''
import tkinter as tk
from enum import Enum
from time import strftime, localtime
from tkintermapview import TkinterMapView
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data import data_in
from run_model import run_model


model_options = [
    "lstm",
    "lstm2",
    "random_forest"
]

class CongestionLevel(Enum):
    FREE = "gray"
    BASICALLY_FREE = "green"
    MILD_CONGESTED = "yellow"
    MODERATE_CONGESTED = "red"
    HEAVILY_CONGESTED = "brown"


class App(tk.Tk):
    APP_NAME = "Simple Map"
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(App.APP_NAME)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []
        self.marker_path = None

        # Create a frame for input fields
        input_frame = tk.Frame(self)
        input_frame.pack(padx=10, pady=10)
        
        # Input fields and labels
        tk.Label(input_frame).grid(row=0, column=0, sticky="w")
        self.model_field_value = tk.StringVar(input_frame)
        self.model_field_value.set("Select ML Model")
        self.model_field_entry = tk.OptionMenu(input_frame, self.model_field_value, *model_options)
        self.model_field_entry.grid(row=0, column=1)

        # Run Model button
        run_button = tk.Button(input_frame, text="Run Model", command=self.run_model_from_gui)
        run_button.grid(row=3, columnspan=2)

        # Map widget
        self.map_widget = TkinterMapView(self, width=1000, height=1000, corner_radius=0)
        self.map_widget.pack(fill="both")
        self.map_widget.set_address("Cologne")

    def run_model_from_gui(self):

        self.map_widget.delete_all_marker()
        self.map_widget.delete_all_path()
        
        model_option = self.model_field_value.get()
        
        df = run_model(data=data_in, type=model_option)
        location_list = list(zip(df['stop_lat'], df['stop_lon'], df['congestion_level']))
        self.marker_list = location_list

        # Add markers for each coordinate in self.marker_list
        for marker in self.marker_list:
            lat, lon, _ = marker
            self.map_widget.set_marker(lat, lon)

        # Create paths with different colors
        for i in range(len(location_list) - 1):
            start = location_list[i]
            end = location_list[i + 1]
            _, _, color = start  # Extract the congestion level as the color

            if color == 0:
                level = CongestionLevel.FREE
            elif color == 1:
                level = CongestionLevel.BASICALLY_FREE
            elif color == 2:
                level = CongestionLevel.MILD_CONGESTED
            elif color == 3:
                level = CongestionLevel.MODERATE_CONGESTED
            else:
                level = CongestionLevel.HEAVILY_CONGESTED

            self.map_widget.set_path([start[:2], end[:2]], color=level.value)

        first_marker = location_list[0]
        self.map_widget.set_position(first_marker[0], first_marker[1])

    def on_closing(self):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.mainloop()
