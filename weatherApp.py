# main.py

import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Access API key from environment variable
api_key = os.getenv("OPENWEATHERMAP_API_KEY")

# Check if API key is available
if api_key is None:
    raise ValueError("API key is not set. Check your .env file.")

# Continue with making the HTTP request using the API key
city_name = 'Vancouver, US'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
response = requests.get(url)

# Rest of your code...
weather_data = response.json()

if weather_data['cod'] == '404':
    print('City not found. Please check the city name.')
else:
    main_weather = weather_data['weather'][0]['main']
    description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']

    print(f'Weather: {main_weather}')
    print(f'Description: {description}')
    print(f'Temperature: {temperature}°C')


