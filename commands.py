import pyttsx3
import webbrowser
import os
import re
import wikipedia
import pywhatkit as kit
from transformers import pipeline
# from gensim.summarization import summarize

# Speech engine init
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 is male, 1 female
summarizer = pipeline("summarization", model="t5-small")

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

def googleSearch(query):
    searchResult = wikipedia.search(query[1:])
    if not searchResult:
        speak('Sorry, no results found')
        return 'No result found'
    try:
        wikiPage = wikipedia.page(searchResult[0])
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    wikiSummary = summarizer(wikiSummary, max_length=200, min_length=15, do_sample=False)
    print(wikiSummary)
    speak(wikiSummary)

def getYTTerm(query):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, query, re.IGNORECASE)
    return match.group(1) if match else None

def playYoutube(query):
    query = ' '.join(query)
    searchTerm = getYTTerm(query)
    speak('playing ' + searchTerm + ' on youtube')
    kit.playonyt(searchTerm)
