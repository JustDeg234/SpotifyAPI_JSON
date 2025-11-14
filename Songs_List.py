# Importing Spotipy saves writing manual HTTP requests, opting for a Python wrapper around the Spotify Web API
# SpotifyOAuth handles entire authentification workflow by opening browser to get tokens, refresh, saves them, etc.

import spotipy
from spotipy.oauth2 import SpotifyOAuth

#'sp' spotify client object to talk to spotify. Pass in auth_manager which is the OAuth handler

sp = spotipy.Spotipy(auth_manager = SpotifyOAuth(
    client_id = "",
    client_secret = "",
    redirect_uri = "",
    scope = "user-library-read"
))

#executes a GET request to the Spotify API endpoint
results = sp.current_user_saved_tracks()

songs = [] #holds post-filtered metadeta

for item in results['items']: #each item is a dict containing a track's info
    track = item['track']
    songs.append({
        "name": track['name'],
        "artist": track['artists'][0]['name'],
        "id": track['id'],
        "album": track['album']['name'],
        "release_date": track['album']['release_date'],
        "duration_ms": track['duration_ms'],
        "popularity": track['popularity']
    })
import json

print(json.dumps(songs, indent=4))
        
