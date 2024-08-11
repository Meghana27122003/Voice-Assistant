import pyttsx3 as p
import speech_recognition as sr
from datetime import datetime
from Selenium import infow  # Adjust import according to your actual file structure
from video import music
from news import news
import randfacts
from weather import temp, des

# Function to initialize the text-to-speech engine and speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get current date and time in a detailed manner
def speak_date_time():
    now = datetime.now()
    day = now.strftime("%A")
    date = now.strftime("%d %B %Y")
    time = now.strftime("%H:%M %p")
    detailed_time = f"Today is {day}, {date}. The current time is {time}."
    speak(detailed_time)

# Initialize text-to-speech engine
engine = p.init()

# Adjust the rate of speech
engine.setProperty('rate', 150)

# Select a voice from the available voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Initialize the speech recognizer
r = sr.Recognizer()

# Greet the user
speak("Hello, I am your voice assistant")

# Speak the date and time in detail
speak_date_time()

speak("Temperature in Kurnool is " + str(temp()) + " degrees Celsius and with " + str(des()))
speak("What can I do for you?")

# Listen to the user's request and process it
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening........")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

# Process the recognized text
if "information" in text:
    speak("You need information on which topic?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening........")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("Searching {} in Wikipedia".format(infor))
    # Fetch information using Selenium
    assist = infow()
    assist.get_info(infor)

elif "play" in text and "video" in text:
    speak("You want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening........")
        audio = r.listen(source)
        video = r.recognize_google(audio)
    print("Playing {} on YouTube........".format(video))
    assist = music()
    assist.play(video)

elif "news" in text:
    print("Sure, here is the news for you!")
    speak("Sure, here is the news for you!")
    arr = news()  # Fetch fresh news items
    for item in arr:
        print(item)
        speak(item)

elif "fact" in text or "facts" in text:
    speak("Here is a fact for you!")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that, " + x)
