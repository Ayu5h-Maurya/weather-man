import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from src.api_handler import fetch_weather, fetch_historical_weather
from src.data_processor import process_weather_data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌤️ Weather Data Visualizer")
        self.root.geometry("450x400")

        tk.Label(root, text="Enter City:").pack(pady=5)
        self.city_entry = tk.Entry(root)
        self.city_entry.pack(pady=5)

        tk.Label(root, text="Select Date:").pack(pady=5)
        self.date_picker = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_picker.pack(pady=5)

        tk.Button(root, text="Get Weather", command=self.get_weather).pack(pady=15)

        self.output = tk.Text(root, height=10, width=50)
        self.output.pack()

    def get_weather(self):
        city = self.city_entry.get()
        selected_date = self.date_picker.get_date()
        today = datetime.now().date()

        try:
            if selected_date == today:
                json_data = fetch_weather(city)
            else:
                json_data = fetch_historical_weather(city, selected_date)

            df = process_weather_data(json_data)
            self.output.delete('1.0', tk.END)
            self.output.insert(tk.END, df.to_string(index=False))

        except Exception as e:
            self.output.delete('1.0', tk.END)
            self.output.insert(tk.END, f"❌ Error: {str(e)}")
    def plot_weather(self, df):
        plt.clf()
        df_plot = df.melt(id_vars=["City"], var_name="Metric", value_name="Value")

        fig, ax = plt.subplots(figsize=(6, 4))
        df_plot = df_plot[df_plot["Metric"] != "City"]
        ax.bar(df_plot["Metric"], df_plot["Value"], color="skyblue")
        ax.set_title(f"Weather in {df['City'][0]}")
        ax.set_ylabel("Value")

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

