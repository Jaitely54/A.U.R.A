
# Voice Greeting System
This Python script utilizes the pyttsx3 library to create a voice greeting system. The script greets the user based on the current time and prompts for further interaction.

# Import Statements
```python

import pyttsx3 
import datetime
```
## Initialization
```python

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)
```
## Functions
### 'speak'
This function takes an audio message as input, uses the text-to-speech engine to speak the message, and runs the engine to wait for the speech to complete.

```python

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
```
### 'greet'
This function greets the user based on the current time of the day (morning, afternoon, or evening) and prompts for further interaction.

```python

def greet():
    current_hour = int(datetime.datetime.now().hour)

    if current_hour < 12:
        greeting_message = "Good morning!"
    elif current_hour < 18:
        greeting_message = "Good afternoon!"
    else:
        greeting_message = "Good evening!"

    speak(greeting_message)
    speak("Is there anything I can do for you?")
```
## Example Usage
```python

greet()
```
## License
This project is licensed under the MIT License
