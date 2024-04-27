import datetime
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty("voice", id)
    newVoiceRate = 150  # Will Speak with 150 wpm
    engine.setProperty("rate", newVoiceRate)
    engine.say(text=text)
    engine.runAndWait()


currenttime = datetime.datetime.now()
time1 = currenttime.strftime("%I:%M %p")
print(f"The current timing is: {time1}")
speak(f"The current timing is: {time1}")


currenttime = datetime.datetime.now()
date1 = currenttime.strftime("%B %d, %Y")
print(f"The current Date is: {date1}")
speak(f"The current Date is: {date1}")