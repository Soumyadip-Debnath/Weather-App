import tkinter as tk
import requests
import json

api_url = 'http://api.weatherstack.com/current'
access_key = '47bacc75fc68861631b58fb317d8f80c'


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
            weather_label.config(
                text='Unable to retrieve weather information.')
            return

        temperature = data['current'].get('temperature')
        description = data['current'].get('weather_descriptions', ['N/A'])[0]
        feels_like_temperature = data['current'].get('feelslike')
        humidity = data['current'].get('humidity')

        if temperature is None:
            weather_label.config(text='Temperature is not available!')
        else:
            # Display the weather information and hide the input box and button
            location_entry.grid_forget()
            get_weather_button.grid_forget()
            weather_label.config(
                text=f"Temperature of {location} is {temperature}°C\nDescription: {description}\nFeels Like Temperature: {feels_like_temperature}°C\nHumidity: {humidity}%rh",
                font=('Roboto', 12)  # Change the font style and size
            )

    except requests.exceptions.RequestException as e:
        weather_label.config(text=f"Error Occurred: {e}")


root = tk.Tk()
root.title('Weather Application')

# Configure the grid layout
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Change the font style and size
location_entry = tk.Entry(root, font=('Roboto', 12))
location_entry.grid(row=0, column=0, padx=10, pady=10)

get_weather_button = tk.Button(
    root, text='Get Weather', command=get_weather, bg='green', fg='white')  # Set button color
get_weather_button.grid(row=0, column=1, padx=10, pady=10)

weather_label = tk.Label(root, text='', font=(
    'Roboto', 12))  # Change the font style and size
weather_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
