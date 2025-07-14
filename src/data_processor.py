import pandas as pd

def process_weather_data(json_data):
    data = {
        "City": json_data["name"],
        "Temperature (°C)": json_data["main"]["temp"],
        "Humidity (%)": json_data["main"]["humidity"],
        "Pressure (hPa)": json_data["main"]["pressure"],
        "Wind Speed (m/s)": json_data["wind"]["speed"]
    }
    return pd.DataFrame([data])
