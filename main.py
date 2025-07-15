from src.api_handler import fetch_weather
from src.data_processor import process_weather_data
from src.plotter import plot_weather
from tkinter import Tk
from src.gui import WeatherApp

def main():
    city = input("Enter a city name: ")
    try:
        weather_json = fetch_weather(city)
        df = process_weather_data(weather_json)
        print("\n📋 Weather Data:")
        print(df.to_string(index=False))
        plot_weather(df, city)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
    root = Tk()
    app = WeatherApp(root)
    root.mainloop()
