import tkinter as tk
import requests

apiKey = "2f42e0add6c953de95b3122f4c151e1d"
def searchLocation():
    cityName=Location_entry.get()
    if cityName :
         

      weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}")
      data = weather_data.json()
      if data.get('cod') != 200:
          tempC_labbel.config(text=f"City '{cityName}' not found.")
          Wind_Speed_labbel.config(text="")
          humidity_labbel.config(text="")
          pressure_labbel.config(text="")
          precipitation_labbel.config(text="")

      else: 
            
        tempK = data['main']['temp']
        windSpeedms = data['wind']['speed']    
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']

        lat = data['coord']['lat']
        lon = data['coord']['lon']
        one_call_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={apiKey}&exclude=current,minutely,daily"

        forecast_data = requests.get(one_call_url)
        forecast = forecast_data.json()

        if 'hourly' in forecast:
            precipitation_probability = forecast['hourly'][0].get('pop', 0)
        else:
            precipitation_probability = 0
            print("Hourly data not available")

        tempC = tempK - 273.15
        windSpeedkmh= windSpeedms *(5/18)

        tempC_labbel.config(text=f"Temperature: {tempC:.2f}°C ")
        Wind_Speed_labbel.config(text=f"Wind Speed: {windSpeedkmh}km/h")
        pressure_labbel.config(text=f"Pressure: {pressure} hPa")
        precipitation_labbel.config(text=f"Precipitation: {precipitation_probability}%")
     
    else:
      tempC_labbel.config(text="")
      Wind_Speed_labbel.config(text="")
      humidity_labbel.config(text="")
      pressure_labbel.config(text="")
      precipitation_labbel.config(text="")

#***************************************************************************************
Window=tk.Tk()
Window.title("Weather Forcast")
Window.rowconfigure(0 ,minsize=200)
Window.columnconfigure(0 ,minsize=450)
fram_buttons=tk.Frame(Window ,relief=tk.RAISED)


btn_search=tk.Button(fram_buttons , text="Search", command=searchLocation)

Location_entry = tk.Entry(Window, width=35) 
Location_entry.grid(pady=10 , padx=10,sticky="N" , column=0)

fram_buttons.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
btn_search.grid(row=0, column=0, padx=5, pady=5)


label = tk.Label(Window, text="Location: ", font=("Arial", 16))
label.grid(pady=5 ,padx=10,column=0,row=0 ,sticky="nw")

tempC_labbel=tk.Label(Window ,text=f"Temperature: 0°C " , font=("Arial", 14))


Wind_Speed_labbel=tk.Label(Window ,text=f"Wind Speed: 0km/h" , font=("Arial", 14))

humidity_labbel=tk.Label(Window ,text=f"Humidity: 0%" , font=("Arial", 14))

pressure_labbel=tk.Label(Window ,text=f"Pressure: 0 hpa" , font=("Arial", 14))

precipitation_labbel=tk.Label(Window ,text=f"precipitation: 0%"  , font=("Arial", 14))

tempC_labbel.grid(row=0, column=0, pady=0, padx=10, sticky="w")
Wind_Speed_labbel.grid(row=1, column=0, pady=0, padx=10, sticky="w")
humidity_labbel.grid(row=2, column=0, pady=0, padx=10, sticky="w")
pressure_labbel.grid(row=3, column=0, pady=0, padx=10, sticky="w")
precipitation_labbel.grid(row=4, column=0, pady=0, padx=10, sticky="w")



Window.mainloop()