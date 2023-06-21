import tkinter as tk
import requests
import json

api_url = 'http://api.weatherstack.com/current'
access_key = 'YOUR_API_KEY'


def get_weather():
    location = location_entry.get()

    if not location:
        weather_label.config(text='Please enter a location')
        return

    params = {
        'access_key': access_key,
        'query': location
    }

    try:
        response = requests.get(api_url, params=params)
        data = json.loads(response.text)

        if 'current' not in data:
            weather_label.config(text='Unable to retrive weather information.')

        temperature = data['current'].get('temperature')
        description = data['current'].get('weather_descriptions', ['N/A'])[0]
        feels_like_temperature = data['current'].get('feelslike')
        humidity = data['current'].get('humidity')

        if temperature is None:
            weather_label.config(text='Temperature is not available!')
        else:
            weather_label.config(
                text=f"Temperature of {location} is {temperature}°C\nDescription: {description}\nFeels Like Temperature: {feels_like_temperature}°C\nHumidity: {humidity}%rh")

    except requests.exceptions.RequestException as e:
        weather_label.config(text=f"Error Occurred: {e}")


root = tk.Tk()
root.title('Weather Application')
root.geometry('400x300')

location_entry = tk.Entry(root, takefocus='Enter the Location')
location_entry.pack()

get_weather_button = tk.Button(root, text='Get Weather', command=get_weather)
get_weather_button.pack()

weather_label = tk.Label(root, text='')
weather_label.pack()

root.mainloop()
