# Smart-Playlist app

import config
import os.path

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

print("Welcome to Smart-Playlist \nCreated by Tyler Moen\n")

# Checks for config folder
config_exists = os.path.isdir('config')
if (config_exists == False):
    config.genConfig()

config.readConfig()

#config.init()
x = config.id
print("X equals = " + x)

config.formatCheck()

print(config.gPlayl)
print(config.playl)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config.id,
                                                           client_secret=config.secret))

def testRun():
    results = sp.search(q='weezer', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])

