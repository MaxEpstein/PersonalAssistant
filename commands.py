import pyttsx3
import webbrowser
import os
import re
import pywhatkit as kit
from dotenv import load_dotenv
load_dotenv()

# 15 requests per minute, 1500 requests per day, 1M tokens per minute limit
from google import genai
from google.genai import types

# Speech engine init
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 is male, 1 female
# summarizer = pipeline("summarization", model="t5-small")

# Browser Config
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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

def googleSearch(query):
    prompt = " ".join(query)
    speak("Generating Response")
    repsonse = client.models.generate_content(model="gemini-2.0-flash", contents=prompt, config=types.GenerateContentConfig(max_output_tokens=500, temperature=0.5))
    print(repsonse.text)
    speak(repsonse.text)

def getYTTerm(query):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, query, re.IGNORECASE)
    return match.group(1) if match else None

def playYoutube(query):
    query = ' '.join(query)
    searchTerm = getYTTerm(query)
    speak('playing ' + searchTerm + ' on youtube')
    kit.playonyt(searchTerm)
