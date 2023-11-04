import tkinter as tk
from enum import Enum
from time import strftime, localtime
from tkintermapview import TkinterMapView
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import ../db.py
import run_model

route_id_option = ["100007"]
direction_id_option = ["0", "1"]
curr_time = strftime("%Y-%m-%d %H:%M:%S", localtime())


data_in = {
    "route_id": 100001,
    "direction_id": 0,
    "arrival_hour": 23,
    "arrival_minute": 7,
    "segments": [
        {
            "segment_id": "702 - 241",
            "start_stop_id": 655,
            "stop_lat": 50.962889,
            "stop_lon": 7.156225,
            "end_stop_id": 655,
            "next_lat": 50.962497,
            "next_lon": 7.149525,
            "runtime_sec": 60
        },
        {
            "segment_id": "241 - 261",
            "start_stop_id": 666,
            "stop_lat": 50.962497,
            "stop_lon": 7.149525,
            "end_stop_id": 666,
            "next_lat": 50.963338,
            "next_lon": 7.142599,
            "runtime_sec": 120,
        },
        {
            "segment_id": "261 - 830",
            "start_stop_id": 667,
            "stop_lat": 50.963338,
            "stop_lon": 7.142599,
            "end_stop_id": 667,
            "next_lat": 50.96085,
            "next_lon": 7.136873,
            "runtime_sec": 60
        },
        {
            "segment_id": "830 - 142",
            "start_stop_id": 671,
            "stop_lat": 50.96085,
            "stop_lon": 7.136873,
            "end_stop_id": 671,
            "next_lat": 50.956685,
            "next_lon": 7.129755,
            "runtime_sec": 120
        },
        {
            "segment_id": "142 - 200",
            "start_stop_id": 670,
            "stop_lat": 50.956685,
            "stop_lon": 7.129755,
            "end_stop_id": 670,
            "next_lat": 50.953963,
            "next_lon": 7.115585,
            "runtime_sec": 120
        },
        {
            "segment_id": "200 - 187",
            "start_stop_id": 669,
            "stop_lat": 50.953963,
            "stop_lon": 7.115585,
            "end_stop_id": 669,
            "next_lat": 50.951587,
            "next_lon": 7.102577,
            "runtime_sec": 60
        },
        {
            "segment_id": "187 - 186",
            "start_stop_id": 668,
            "stop_lat": 50.951587,
            "stop_lon": 7.102577,
            "end_stop_id": 668,
            "next_lat": 50.94901,
            "next_lon": 7.079235,
            "runtime_sec": 120
        },
        {
            "segment_id": "186 - 181",
            "start_stop_id": 547,
            "stop_lat": 50.94901,
            "stop_lon": 7.079235,
            "end_stop_id": 547,
            "next_lat": 50.94765,
            "next_lon": 7.072644,
            "runtime_sec": 60
        },
        {
            "segment_id": "181 - 180",
            "start_stop_id": 546,
            "stop_lat": 50.94765,
            "stop_lon": 7.072644,
            "end_stop_id": 546,
            "next_lat": 50.944071,
            "next_lon": 7.048102,
            "runtime_sec": 60
        },
        {
            "segment_id": "180 - 179",
            "start_stop_id": 540,
            "stop_lat": 50.944071,
            "stop_lon": 7.048102,
            "end_stop_id": 540,
            "next_lat": 50.942515,
            "next_lon": 7.042148,
            "runtime_sec": 60
        },
        {
            "segment_id": "179 - 178",
            "start_stop_id": 539,
            "stop_lat": 50.942515,
            "stop_lon": 7.042148,
            "end_stop_id": 539,
            "next_lat": 50.941749,
            "next_lon": 7.029212,
            "runtime_sec": 60
        },
        {
            "segment_id": "178 - 144",
            "start_stop_id": 518,
            "stop_lat": 50.941749,
            "stop_lon": 7.029212,
            "end_stop_id": 518,
            "next_lat": 50.941564,
            "next_lon": 7.022591,
            "runtime_sec": 60
        },
        {
            "segment_id": "144 - 143",
            "start_stop_id": 517,
            "stop_lat": 50.941564,
            "stop_lon": 7.022591,
            "end_stop_id": 517,
            "next_lat": 50.938927,
            "next_lon": 7.008548,
            "runtime_sec": 60
        },
        {
            "segment_id": "143 - 28",
            "start_stop_id": 513,
            "stop_lat": 50.938927,
            "stop_lon": 7.008548,
            "end_stop_id": 513,
            "next_lat": 50.937512,
            "next_lon": 6.998488,
            "runtime_sec": 60
        },
        {
            "segment_id": "28 - 27",
            "start_stop_id": 512,
            "stop_lat": 50.937512,
            "stop_lon": 6.998488,
            "end_stop_id": 512,
            "next_lat": 50.936467,
            "next_lon": 6.986145,
            "runtime_sec": 60
        },
        {
            "segment_id": "27 - 2",
            "start_stop_id": 44,
            "stop_lat": 50.936467,
            "stop_lon": 6.986145,
            "end_stop_id": 44,
            "next_lat": 50.939594,
            "next_lon": 6.978799,
            "runtime_sec": 60
        },
        {
            "segment_id": "2 - 1",
            "start_stop_id": 802,
            "stop_lat": 50.939594,
            "stop_lon": 6.978799,
            "end_stop_id": 802,
            "next_lat": 50.936662,
            "next_lon": 6.970358,
            "runtime_sec": 60
        },
        {
            "segment_id": "1 - 39",
            "start_stop_id": 39,
            "stop_lat": 50.936662,
            "stop_lon": 6.970358,
            "end_stop_id": 39,
            "next_lat": 50.935705,
            "next_lon": 6.959995,
            "runtime_sec": 60
        },
        {
            "segment_id": "39 - 802",
            "start_stop_id": 1,
            "stop_lat": 50.935705,
            "stop_lon": 6.959995,
            "end_stop_id": 1,
            "next_lat": 50.93577,
            "next_lon": 6.947677,
            "runtime_sec": 60
        },
        {
            "segment_id": "802 - 44",
            "start_stop_id": 2,
            "stop_lat": 50.93577,
            "stop_lon": 6.947677,
            "end_stop_id": 2,
            "next_lat": 50.936343,
            "next_lon": 6.93901,
            "runtime_sec": 60
        },
        {
            "segment_id": "44 - 512",
            "start_stop_id": 27,
            "stop_lat": 50.936343,
            "stop_lon": 6.93901,
            "end_stop_id": 27,
            "next_lat": 50.936071,
            "next_lon": 6.932603,
            "runtime_sec": 60
        },
        {
            "segment_id": "512 - 513",
            "start_stop_id": 28,
            "stop_lat": 50.936071,
            "stop_lon": 6.932603,
            "end_stop_id": 28,
            "next_lat": 50.936637,
            "next_lon": 6.924647,
            "runtime_sec": 60
        },
        {
            "segment_id": "513 - 517",
            "start_stop_id": 143,
            "stop_lat": 50.936637,
            "stop_lon": 6.924647,
            "end_stop_id": 143,
            "next_lat": 50.936745,
            "next_lon": 6.916711,
            "runtime_sec": 60
        },
        {
            "segment_id": "517 - 518",
            "start_stop_id": 144,
            "stop_lat": 50.936745,
            "stop_lon": 6.916711,
            "end_stop_id": 144,
            "next_lat": 50.936998,
            "next_lon": 6.90855,
            "runtime_sec": 60
        },
        {
            "segment_id": "518 - 539",
            "start_stop_id": 178,
            "stop_lat": 50.936998,
            "stop_lon": 6.90855,
            "end_stop_id": 178,
            "next_lat": 50.937177,
            "next_lon": 6.899363,
            "runtime_sec": 60
        },
        {
            "segment_id": "539 - 540",
            "start_stop_id": 179,
            "stop_lat": 50.937177,
            "stop_lon": 6.899363,
            "end_stop_id": 179,
            "next_lat": 50.937314,
            "next_lon": 6.894315,
            "runtime_sec": 60
        },
        {
            "segment_id": "540 - 546",
            "start_stop_id": 180,
            "stop_lat": 50.937314,
            "stop_lon": 6.894315,
            "end_stop_id": 180,
            "next_lat": 50.937452,
            "next_lon": 6.889253,
            "runtime_sec": 60
        },
        {
            "segment_id": "546 - 547",
            "start_stop_id": 181,
            "stop_lat": 50.937452,
            "stop_lon": 6.889253,
            "end_stop_id": 181,
            "next_lat": 50.937689,
            "next_lon": 6.881746,
            "runtime_sec": 60
        },
        {
            "segment_id": "547 - 668",
            "start_stop_id": 186,
            "stop_lat": 50.937689,
            "stop_lon": 6.881746,
            "end_stop_id": 186,
            "next_lat": 50.93759,
            "next_lon": 6.874588,
            "runtime_sec": 60
        },
        {
            "segment_id": "668 - 669",
            "start_stop_id": 187,
            "stop_lat": 50.93759,
            "stop_lon": 6.874588,
            "end_stop_id": 187,
            "next_lat": 50.937636,
            "next_lon": 6.868372,
            "runtime_sec": 60
        },
        {
            "segment_id": "669 - 670",
            "start_stop_id": 200,
            "stop_lat": 50.937636,
            "stop_lon": 6.868372,
            "end_stop_id": 200,
            "next_lat": 50.937957,
            "next_lon": 6.855375,
            "runtime_sec": 60
        },
        {
            "segment_id": "670 - 671",
            "start_stop_id": 142,
            "stop_lat": 50.937957,
            "stop_lon": 6.855375,
            "end_stop_id": 142,
            "next_lat": 50.938112,
            "next_lon": 6.845191,
            "runtime_sec": 60
        },
        {
            "segment_id": "671 - 667",
            "start_stop_id": 830,
            "stop_lat": 50.938112,
            "stop_lon": 6.845191,
            "end_stop_id": 830,
            "next_lat": 50.938239,
            "next_lon": 6.835035,
            "runtime_sec": 60
        },
        {
            "segment_id": "667 - 666",
            "start_stop_id": 261,
            "stop_lat": 50.938239,
            "stop_lon": 6.835035,
            "end_stop_id": 261,
            "next_lat": 50.938383,
            "next_lon": 6.828664,
            "runtime_sec": 60
        },
        {
            "segment_id": "666 - 655",
            "start_stop_id": 241,
            "stop_lat": 50.938383,
            "stop_lon": 6.828664,
            "end_stop_id": 241,
            "next_lat": 50.940897,
            "next_lon": 6.815136,
            "runtime_sec": 60
        },
        {
            "segment_id": "655 - 665",
            "start_stop_id": 702,
            "stop_lat": 50.940897,
            "stop_lon": 6.815136,
            "end_stop_id": 702,
            "next_lat": 50.940897,
            "next_lon": 6.815136,
            "runtime_sec": 60
        }
    ]
}

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

        # Get the input values from the GUI entry fields
        # route_id = int(self.route_id_value.get())
        # direction_id = int(self.direction_id_value.get())
        # future_time = self.future_time_entry.get()

        df = run_model.run_model(data_in)
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
