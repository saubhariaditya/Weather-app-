import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(api_key, city):
    """
    Fetch weather details for a specific city using OpenWeatherMap API.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = { 
        'q': city,
        'appid': api_key,
        'units': 'metric'  # For temperature in Celsius
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    except KeyError:
        return "Invalid response received from the server."

def fetch_weather():
    """
    Fetch weather data and update the GUI.
    """
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    api_key = '4fe89575303fffeeb70f036298389f59'  
    weather = get_weather(api_key, city)
    
    if isinstance(weather, dict):
        result = (
            f"Weather in {weather['city']}:\n"
            f"Temperature: {weather['temperature']}°C\n"
            f"Description: {weather['description']}\n"
            f"Humidity: {weather['humidity']}%\n"
            f"Wind Speed: {weather['wind_speed']} m/s"
        )
    else:
        result = weather
    
    result_label.config(text=result)

# GUI Setup
root = tk.Tk()
root.title("Weather App")

# Input Frame
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack()

city_label = tk.Label(input_frame, text="City:", font=("Arial", 14))
city_label.grid(row=0, column=0, padx=5, pady=5)

city_entry = tk.Entry(input_frame, font=("Arial", 14))
city_entry.grid(row=0, column=1, padx=5, pady=5)

fetch_button = tk.Button(input_frame, text="Get Weather", font=("Arial", 14), command=fetch_weather)
fetch_button.grid(row=0, column=2, padx=5, pady=5)

# Output Frame
output_frame = tk.Frame(root, padx=10, pady=10)
output_frame.pack()

result_label = tk.Label(output_frame, text="", font=("Arial", 14), justify="left", wraplength=400)
result_label.pack()

# Run the GUI
root.mainloop()