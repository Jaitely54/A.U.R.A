# Weather Information Retrieval
This Python script utilizes the requests library to retrieve weather information from the OpenWeatherMap API for a specified city.

## Import Statement
```python

import requests
```
## Function
### 'get_weather'
This function takes an API key and a city name as input, makes a request to the OpenWeatherMap API, and prints the weather information (description, temperature, and humidity) for the specified city.

```python
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change units to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']

            print(f"Weather in {city}: {weather_description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    api_key = 'your_api_key'
    
    city = input("Enter the city name: ")
    
    get_weather(api_key, city)

```
## Usage
Replace 'your_api_key' with the provided API key from OpenWeatherMap.

## License
This project is licensed under the MIT License 
