import requests
import pyttsx3
import speech_recognition as sr
import warnings

# Suppress warnings
warnings.simplefilter("ignore")

# Initialize speech engine
engine = pyttsx3.init()
# Set properties for speech
engine.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
engine.setProperty('rate', 150)  # Speed of speech

# Function to speak text
def speak(text):
    engine.say(text=text)
    engine.runAndWait()

# Function to take command from microphone
def take_cmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aura: Awaiting for command...")
        r.pause_threshold = 2
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User: {query}\n")
    except Exception as e:
        print("Aura: Aayien!! ?")
        return "None"
    return query

# Function to fetch city name from IP info
def get_city_from_ipinfo(api_token):
    try:
        response = requests.get(f'https://ipinfo.io?token={api_token}')
        data = response.json()
        city = data['city']
        # Normalize city name
        if city == "Dehra Dūn":
            city = "Dehradun"
        return city
    except Exception as e:
        print(f"Error obtaining city from IP: {e}")
        return None

# Function to get weather information
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_info = (f"Weather in {city}: {weather_description}\n"
                            f"Temperature: {temperature}°C\n"
                            f"Humidity: {humidity}%")
            return weather_info
        else:
            return f"Error fetching weather: {data['message']}"
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
def main():
    
    
    # Hardcoded for demonstration purposes
    ipinfo_api_token = 'c9af1030a48637' 
    openweathermap_api_key = 'c401b6438bd509ac66fddd53ce9da887'

    city = get_city_from_ipinfo(ipinfo_api_token)
    if city:
        print(f"Detected city: {city}")
        weather_info = get_weather(openweathermap_api_key, city)
        print(weather_info)
        speak(weather_info)
    else:
        print("Could not detect city based on IP address.")

if __name__ == "__main__":
    main()
