# Voice Assistant Control
This Python script uses the pyttsx3 library for text-to-speech functionality and the speech_recognition library for voice recognition. It defines functions to let the voice assistant speak and listen to user commands.

# Import Statements
```python

import pyttsx3
import speech_recognition as sr
```

## Functions

### 'speak'
This function initializes the text-to-speech engine and sets the voice and rate. It then speaks the provided text.

```python

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice', id)
    newVoiceRate = 150
    engine.setProperty('rate', newVoiceRate)

    engine.say(text=text)
    engine.runAndWait()
```
### 'takecmd'
This function uses the microphone to listen to user commands. It sets thresholds for pause and energy, listens to the audio, and then uses Google's Speech Recognition to convert the audio into text.

```python

def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Awaiting your command...")

        r.pause_threshold = 2
        r.energy_threshold = 200
        audio = r.listen(src, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User: {query}\n")

    except Exception as e:
        print("Sorry, I didn't get that. Could you please repeat?")
        return "None"

    return query
```
## Usage
You can use these functions to integrate voice control into your application. The speak function allows the assistant to communicate through voice, and takecmd allows the assistant to listen to user commands.
## License
This project is licensed under the MIT License
