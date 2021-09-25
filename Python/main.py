# Smart-Playlist app

import config
import os.path
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

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





def testRun():
    results = sp.search(q='weezer', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])

def createRands(pid, name):
    # Creates the random playlists
    print("Downloading playlist info...")
    
    playlist_id = 'spotify:playlist:' + pid
    results = sp.playlist_tracks(playlist_id,fields="items(track(name,artists(name),id,href)),total", market="US")

    fw = open("config/playlist_org_"+name+".json", "w")
    fw.write(json.dumps(results, indent=4))

    # print(json.dumps(results, indent=4))

    print("Adding tracks to memory...")
    fw = open("config/playlist_org_"+name+".json", "r")
    dTrack = json.load(fw)
    print(dTrack['items'][0]['track']['name'])

    for x, val in enumerate(dTrack['items']):
        print()
        plist_sec.append[val['track']['name'], val['track']['artists']['name'], val['track']['id']]

def exceptions():
    print()

def mixComb():
    print()

def dupCheck():
    print()



for x, val in enumerate(config.gPlayl):
    print("Opening universal playlists...")
    xstr = str(x)
    createRands(val, 'uni_'+ xstr)
    

for x, val in enumerate(config.playl):
    print("Opening personal playlists...")
    xstr = str(x)
    createRands(val, 'per_'+ xstr)



# fw = open("dump_tracks3.json", "r")
# dTrack = json.load(fw)
# print(dTrack)