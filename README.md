Weather Fetcher

Description

The Weather Fetcher is a Python script designed to retrieve current weather information for a specified city using the OpenWeatherMap API. It demonstrates how to load an API key from an environment variable, make a HTTP request to an external API, and process the response to extract and display the weather details.

Features

- Load API key securely from an environment file
- Fetch weather data using OpenWeatherMap API
- Handle errors for missing API key or city not found
- Display weather information: condition, description, and temperature

Prerequisites

- Python 3.x
- Requests library
- python-dotenv library

To install the required Python libraries, run:

```bash
pip install requests python-dotenv
```

Setup

1. Get an API Key**: Sign up at [OpenWeatherMap](https://openweathermap.org/api) and obtain an API key.
2. Environment Variables**: Create a `.env` file in the root directory of your project and add your OpenWeatherMap API key as follows:

    ```env
    OPENWEATHERMAP_API_KEY=your_api_key_here
    ```

3. Running the Script**: Navigate to the directory containing the script and run:

    ```bash
    python weather_fetcher.py
    ```

Replace `weather_fetcher.py` with the appropriate filename if different.

Code Overview

The script follows these steps:

- Loads the API key from the `.env` file using `dotenv`.
- Checks if the API key is available. If not, it raises an error.
- Constructs a request URL with the city name and API key, then makes an HTTP GET request to the OpenWeatherMap API.
- Processes the JSON response, extracting and printing the weather condition, description, and temperature in Celsius.

Error Handling

- If the API key is not set, the script raises a `ValueError`.
- If the city is not found, it prints a message indicating the city was not found.

Customization

To fetch weather data for a different city, modify the `city_name` variable in the script.
