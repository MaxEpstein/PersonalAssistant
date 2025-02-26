from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# Speech engine init
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 is male, 1 female
activationWord = 'computer'

# Browser Config
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print('Recognizing Speech...')
        query = listener.recognize_google(input_speech, language='en_us')
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('Error transcribing speech')
        speak('I did not quite catch that')
        print(exception)
        return 'None'
    
    return query

# Main Loop
if __name__ == '__main__':
    speak('Hello Max...')

    while True:
        # Parse
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            # List Commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greetings, all.')
                else:
                    query.pop(0)
                    speech = ' '.join(query)
                    speak(speech)
            
            # Website Navigation
            if query[0] == 'go' and query[1] == 'to':
                query = ' '.join(query[2:])
                speak('Opening ' + query)
                webbrowser.get('chrome').open_new_tab(query)
            