import datetime
import pyttsx3



def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    
    # * Voice ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0

    voice = engine.getProperty("voices")
    id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty("voice", id)
    newVoiceRate = 150  # Will Speak with 150 wpm
    engine.setProperty("rate", newVoiceRate)
    engine.say(text=text)
    engine.runAndWait()

#! Geeting According to time.
def greet():
    current_hour = int(datetime.datetime.now().hour)
    if current_hour < 12:
        greeting_message = "Good morning!"
    elif current_hour < 16:
        greeting_message = "Good afternoon!"
    else:
        greeting_message = "Good evening!"

    message = f"{greeting_message} Is there anything I can do for you?"
    speak(message)

greet()