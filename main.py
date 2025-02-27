from datetime import datetime
import speech_recognition as sr
import wikipedia
import wolframalpha
import commands as command

listener = sr.Recognizer()
listener.pause_threshold = 2
audioAdjusted = False

activationWord = 'computer'

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
    command.speak('Hello Max...')

    while True:
        # Parse
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            # List Commands
            if query[0] == 'say':
                command.hello(query)
            # Website Navigation
            if query[0] == 'go' and query[1] == 'to':
                command.openSite(query)
            if query[0] == 'open':
                command.openProgram(query)

            # Terminiate Assistant Program
            if query[0] == 'shut' and query[1] == 'down' or query[0] == 'shutdown':
                command.speak('Shutting Assistant Down')
                break;
            