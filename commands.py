import pyttsx3
import webbrowser
import os

# Speech engine init
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 is male, 1 female

# Browser Config
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def speak(text, rate = 140):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def hello(query):
    if 'hello' in query:
        speak('Greetings, all.')
    else:
        query.pop(0)
        speech = ' '.join(query)
        speak(speech)

def openSite(query):
    query = ' '.join(query[2:])
    speak('Opening ' + query)
    if query.__contains__('.com'):
        webbrowser.get('chrome').open_new_tab(query)
    else:
        webbrowser.get('chrome').open_new_tab(query+'.com')

def openProgram(query):
    query = ' '.join(query[1:])
    speak('Opening ' + query)
    try:
        os.system(query)
    except:
        speak(query + ' not found')