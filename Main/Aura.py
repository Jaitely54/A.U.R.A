#                                                      Radhe Radhe

#  importing necessary libraries -------------->
import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import random

import warnings
warnings.simplefilter('ignore')



#  Creating a function for the voice of the Assistant ------------>
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice',id)
    newVoiceRate = 150
    engine.setProperty('rate',newVoiceRate)
    engine.say(text=text)
    engine.runAndWait()




# Creating a function for the Assistant to listern us -------->
    
def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Aura: Awaiting for command...")
        r.pause_threshold = 2
        r.energy_threshold = 300
        audio = r.listen(src,0,4)

    try:
        print("understanding...")
        query = r.recognize_google(audio,language="en-in")
        print(f"user: {query}\n")

    except Exception as e:
        print("Aura: aayien!! ?")
        return "None"
    return query

# creating Functions perform by the Assistant ----------> 


     
def greet():
    
    current_hour = int(datetime.datetime.now().hour)

    if current_hour < 12:
        greeting_message = "Good morning!"
    elif current_hour < 18:
        greeting_message = "Good afternoon!"
    else:
        greeting_message = "Good evening!"

    message = greeting_message +"Is there anything I can do for you?"
    speak(message)


def currenttime():
    currenttime = datetime.datetime.now()
    time1 = currenttime.strftime("%I %M:%p")
    print(f"the current timimg is: {time1}")
    speak(f"the current timimg is: {time1}")
1
def Currentdate():
    currenttime = datetime.datetime.now()
    date1  = currenttime.strftime("%A, %d/%m/%Y")
    print(f"the current Date is: {date1}")
    speak(f"the current Date is: {date1}")


def google_search(query):
    speak("This is what I found for your search!") 
    query = query.replace("google search","")
    query = query.replace("search","")
    query = query.replace("aura","")
    query = query.replace("google","")
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)


reboot_1 = ["reboot the system","reboot the laptop","reboot system","shutdown the laptop",
             "shutdown the system" , "shutdown system" ,"restart the laptop","restart the system", "restart system","shutdown the pc",
             "restart the pc", "reboot the pc"]

def reboot():
    for reboot_string in reboot_1:
        if reboot_string in query:
            print("do you want me to restart the system or shut it down ?")
            speak("do you want me to restart the system or shut it down ?")
            print("\n")
            print("***use cancel to aboort the task***")
            while True:
                user_input = takecmd().lower()

                if "restart" in user_input:
                    print("Restarting the system")
                    speak("Restarting the system")
                    os.system("shutdown /r /t 1")
                elif "shutdown" in user_input:
                    print("Shutting down the system")
                    speak("Shutting down the system")
                    os.system("shutdown /s /t 1")
                elif "cancel" in user_input:
                    print("Aura: task aborted")
                    speak("task aborted")
                    break    
def welcome_response():
    greetings = {
        "patterns": ["hello", "hi", "hey", "howdy", "greetings", "good morning",
                      "good afternoon", "good evening", "hi there", "hey there", "what's up", "hello there"],
        "responses": [
            "Hello! How can I assist you?", "Hi there!", "Hey! What can I do for you?", 
            "Howdy! What brings you here?", "Greetings! How may I help you?", 
            " How can I be of service?", " What do you need assistance with?", 
            " How may I assist you?", "Hey there! How can I help?", 
            "Hi! What's on your mind?", "Hello there! How can I assist you today?",
            "Hey! What's up?", "Hi there! Ready to help.", "Hello! What brings you here?", 
            "Hi! How can I assist you today?", "Greetings! What can I do for you?", 
            " Ready to assist.", " How may I help?", 
            " Ready to assist.", "Hi there! What's on your mind?", 
            "Hey there! Ready to help.", "Hello! Ready to assist."
            # Add more responses as needed
        ]
    }

    # Taking user input (you can replace this with your speech recognition logic)
    user_input =query.lower()

    # Checking if any pattern is present in the user input
    if any(pattern in user_input for pattern in greetings["patterns"]):
        response = random.choice(greetings["responses"])
        print("Assistant:", response)
        speak(response)
    else:
        print("Assistant: I'm here to help. Feel free to ask anything!")
        speak(" I'm here to help. Feel free to ask anything!")


def thank_responses():
    patterns = ["thank you", "thanks", "well done", "thank you so much", "thanks a lot", "nice"]
    responses = [
        "You're welcome!", 
        "Happy to help!", 
        "Glad I could assist.", 
        "Anytime!", 
        "You're welcome! Have a great day.", 
        "No problem!",
        "It was my pleasure!",
        "You got it!",
        "No worries!",
        "I'm here for you!",
        "Don't mention it!",
        "Not a problem!",
        "Anytime you need help, just ask!",
        "You're welcome! Let me know if there's anything else I can do for you.",
        "It's what I'm here for!",
        "Absolutely!",
        "I'm always here to assist you!",
        "You're welcome! If you have more questions, feel free to ask."
    ]
# Instructions before using ::
print("\n")
print("\tHey there, i am AURA an AI powered Desktop Assistant")
print("\n")
print("\t\tAURA is Sleeping, Wake her up")
print("\n")
print("\t\t***Clear Instruction for Aura***")

print("Certainly! To exit the program, you can use the command 'Exit'.")
print("Certainly! To make Aura go into sleep mode, you can use the command 'Sleep'.")
print("\n")
#  Executing the commands-------------->
    
while True:
    query = takecmd().lower()



        #  Starting the Assistant with a Wake up call --------->
    if "aura" in query:
        greet()

        while True:
            query = takecmd().lower()

            if "time" in query:
                currenttime()

            elif "date" in query:
                Currentdate()

            if any(keyword in query for keyword in reboot_1):

                reboot()

            elif "google" in query or "search" in query or "browse" in query:

                google_search(query)


            elif "thank you" in query or "thanks" in query or "good job" in query or "well done" in query:

                thank_responses()

            elif "hi" in query or "hello" in query or "hey" in query:
                welcome_response()

            #  exiting the Assistant wiht the end call command ---------->
                
            elif "exit" in query or "kill" in query:

                print("Glad to work with you")
                speak("Glad to work with you")
                exit()
                
            

        
    else:
        speak("Aura is set to sleep, wake her up")



