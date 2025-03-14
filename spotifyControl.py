import spotipy
from commands import speak
from spotipy.oauth2 import SpotifyOAuth
import os
import re
from dotenv import load_dotenv
load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                                               client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
                                               redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
                                               scope="user-modify-playback-state "
                                               "user-read-currently-playing "
                                               "playlist-modify-private "
                                               "playlist-modify-public "
                                               "user-library-modify "
                                               "app-remote-control "
                                               "streaming"))
def pausePlay(query):
    if ("play" in query):
        print("Playing Spotify")
        speak("Playing Spot-tea-Phi")
        sp.start_playback()
    elif ("pause" in query):
        print("Pausing Spotify")
        speak ("Pausing Spot-tea-Phi")
        sp.pause_playback()

def nextTrack():
    sp.next_track()

def volume(query):
    # Set spotify volume to 50 percent
    print("changing volume")
    volume = query[query.__len__()-1]
    if (volume.endswith('%')):
        volume = volume[:-1]
    try:
        sp.volume(int(volume))
        print("setting spotify volume to " + volume)
        speak("setting Spot-tea-Phi volume to " + volume)
    except:
        print("error changing spotify volume")
        speak("There was an error adjusting the volume. Please try again")

def currentlyPlaying():
    current = sp.currently_playing('US')
    print(current.context.uri)
    print(current + " is currently playing on Spotify")
    speak(current + " is currently playing on Spotify")

def getSongTerm(query):
    pattern = r'play\s+(.+?)(?:\s+on\s+spotify)?$'
    match = re.search(pattern, query, re.IGNORECASE)
    return match.group(1) if match else None

def playSong(query):
    query = ' '.join(query)
    songTerm = getSongTerm(query)
    print("Playing " + songTerm + " on spotify")
