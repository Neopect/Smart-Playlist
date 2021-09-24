# Smart-Playlist app

import config
import os.path
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

plist_org = []
plist_sec = []
plist_act = []
global sp

print("Welcome to Smart-Playlist \nCreated by Tyler Moen\n")

# Checks for config folder
config_exists = os.path.isdir('config')
if (config_exists == False):
    config.genConfig()
    quit()
else:
    config.readConfig()
    config.formatCheck()
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config.id,
                                                           client_secret=config.secret))


#config.init()
# x = config.id
# print("X equals = " + x)



# print(config.gPlayl)
# print(config.playl)



def testRun():
    results = sp.search(q='weezer', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])

def createRands():
    # Creates the random playlists
    print()
    
    # Just wporking demo so far
    playlist_id = 'spotify:user:spotifycharts:playlist:3PGHzE2Tqab3V5xH6JyVcW'
    results = sp.playlist_tracks(playlist_id,fields="items(track(name,artists(name),id,href))", market="US")

    fw = open("dump_tracks3.json", "w")
    fw.write(json.dumps(results, indent=4))

    print(json.dumps(results, indent=4))

def exceptions():
    print()

def mixComb():
    print()

def dupCheck():
    print()
