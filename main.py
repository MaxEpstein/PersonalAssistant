from datetime import datetime
import speechrecognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# Speech engine init
engine = pyttsx3.init()
voices = engine.getProperty('voices')
