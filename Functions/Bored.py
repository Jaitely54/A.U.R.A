import requests
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty("voice", id)
    newVoiceRate = 150  # Will Speak with 150 wpm
    engine.setProperty("rate", newVoiceRate)
    engine.say(text=text)
    engine.runAndWait()

def get_me_suggestion(*args, **kwargs):
    url = "http://www.boredapi.com/api/activity"
    response = requests.get(url)
    return response.json()["activity"]


suggestion = get_me_suggestion()
print("Aura:", suggestion)
speak(suggestion)