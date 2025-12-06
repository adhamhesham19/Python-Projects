import tkinter as tk
import requests
from tkinter import messagebox

# Define your API key
apiKey = "2f42e0add6c953de95b3122f4c151e1d"

# Function to fetch weather data
def searchLocation():
    cityName = Location_entry.get()
    if not cityName:
        clear_labels()
        return
    
    try:
        # Get current weather data
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}")
        data = weather_data.json()

        # Check for valid city
        if data.get('cod') != 200:
            show_error(f"City '{cityName}' not found.")
            clear_labels()
            return

        # Extract necessary data
        tempK = data['main']['temp']
        windSpeedms = data['wind']['speed']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        lat = data['coord']['lat']
        lon = data['coord']['lon']

        # Get hourly forecast for precipitation
        one_call_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={apiKey}&exclude=current,minutely,daily"
        forecast_data = requests.get(one_call_url)
        forecast = forecast_data.json()
        precipitation_probability = forecast['hourly'][0].get('pop', 0) if 'hourly' in forecast else 0

        # Convert from Kelvin to Celsius and meters per second to km/h
        tempC = tempK - 273.15
        windSpeedkmh = windSpeedms * (5 / 18)

        # Update the labels with weather data
        update_labels(tempC, windSpeedkmh, pressure, humidity, precipitation_probability)
    
    except requests.exceptions.RequestException as e:
        show_error("Network error. Please try again later.")
        clear_labels()
    except KeyError as e:
        show_error("Error fetching weather data.")
        clear_labels()


# Function to update the UI labels
def update_labels(tempC, windSpeedkmh, pressure, humidity, precipitation_probability):
    tempC_labbel.config(text=f"Temperature: {tempC:.2f}°C")
    Wind_Speed_labbel.config(text=f"Wind Speed: {windSpeedkmh:.2f} km/h")
    pressure_labbel.config(text=f"Pressure: {pressure} hPa")
    humidity_labbel.config(text=f"Humidity: {humidity}%")
    precipitation_labbel.config(text=f"Precipitation: {precipitation_probability}%")

# Function to clear all labels
def clear_labels():
    tempC_labbel.config(text="")
    Wind_Speed_labbel.config(text="")
    humidity_labbel.config(text="")
    pressure_labbel.config(text="")
    precipitation_labbel.config(text="")

# Function to show error messages in a pop-up
def show_error(message):
    messagebox.showerror("Error", message)

# UI Setup
Window = tk.Tk()
Window.title("Weather Forecast")

# Setting a minimum window size to prevent shrinking too much
Window.geometry("500x350")  # You can adjust this size, but it will not shrink below 500x350

# Configure row and column weights to make the layout more flexible
Window.rowconfigure(0, weight=0)  # First row for button frame
Window.rowconfigure(1, weight=1)  # The second row for labels
Window.columnconfigure(0, weight=1)  # Only one column of interest for expansion

# Frame for buttons
fram_buttons = tk.Frame(Window, relief=tk.RAISED)
fram_buttons.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Button to trigger search
btn_search = tk.Button(fram_buttons, text="Search", command=searchLocation)
btn_search.grid(row=0, column=0, padx=5, pady=5)

# Entry widget for city name
Location_entry = tk.Entry(Window, width=35)
Location_entry.grid(pady=10, padx=10, column=0, row=0)

# Labels for output
label = tk.Label(Window, text="Location: ", font=("Arial", 16))
label.grid(pady=5, padx=10, column=0, row=1, sticky="nw")

tempC_labbel = tk.Label(Window, text="Temperature: 0°C", font=("Arial", 14))
Wind_Speed_labbel = tk.Label(Window, text="Wind Speed: 0 km/h", font=("Arial", 14))
humidity_labbel = tk.Label(Window, text="Humidity: 0%", font=("Arial", 14))
pressure_labbel = tk.Label(Window, text="Pressure: 0 hPa", font=("Arial", 14))
precipitation_labbel = tk.Label(Window, text="Precipitation: 0%", font=("Arial", 14))

# Placing the labels on the window
tempC_labbel.grid(row=2, column=0, pady=5, padx=10, sticky="w")
Wind_Speed_labbel.grid(row=3, column=0, pady=5, padx=10, sticky="w")
humidity_labbel.grid(row=4, column=0, pady=5, padx=10, sticky="w")
pressure_labbel.grid(row=5, column=0, pady=5, padx=10, sticky="w")
precipitation_labbel.grid(row=6, column=0, pady=5, padx=10, sticky="w")

# Start the main loop
Window.mainloop()
