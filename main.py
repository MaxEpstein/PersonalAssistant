from datetime import datetime
import speech_recognition as sr
import os
from dotenv import load_dotenv

import commands as command
import spotifyControl as spotify

load_dotenv()

listener = sr.Recognizer()
listener.pause_threshold = 2
audioAdjusted = False
gameMode = False

def parseCommand():
    print('Listening for a command')

    with sr.Microphone() as source:
        if not audioAdjusted:
            listener.adjust_for_ambient_noise(source)
        input_speech = listener.listen(source)

    try:
        print('Recognizing Speech...')
        query = listener.recognize_google(input_speech, language='en_us')
        print(f'The input was: {query}')
    except Exception as exception:
        print('Error transcribing speech')
        print(exception)
        return 'None'
    
    return query.lower()

# Main Loop
if __name__ == '__main__':
    command.speak('Hello. How can I help you?')

    while True:
        # Parse
        query = parseCommand().lower().split()
        try:
            if query[0] == os.getenv("ACTIVATION_WORD"):
                query.pop(0)
                if not gameMode:
                    # List Commands
                    if query[0] == 'say':
                        command.hello(query)
                    # Website Navigation
                    if query[0] == 'go' and query[1] == 'to':
                        command.openSite(query)
                    if query[0] == 'open':
                        command.openProgram(query)
                    if query[0] == 'google' or query[0] == 'when' or query[0] == 'what' or query[0] == 'where' or query[0] == 'who' or query[0] == 'why':
                        command.googleSearch(query)
                    if query[0] == 'enter':
                        if query[1] == 'game' and query[2] == 'mode':
                            command.speak('Entering Game Mode')
                            gameMode = True
                    if query[0] == 'play' and query[query.__len__()-1] == 'youtube':
                        command.playYoutube(query)
                    if query[0] == 'play' and query[query.__len__()-1] == 'spotify':
                        spotify.playSpotify(query)


                    # Terminiate Assistant Program
                    if query[0] == 'shut' and query[1] == 'down' or query[0] == 'shutdown':
                        command.speak('Shutting Assistant Down')
                        break;
                else:
                    if query[0] == 'exit':
                        if query[1] == 'game' and query[2] == 'mode':
                            command.speak('Exiting Game Mode')
                            gameMode = False
        except:
            continue
            