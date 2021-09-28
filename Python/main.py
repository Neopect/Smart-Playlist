# Smart-Playlist app

import config
import os.path
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import random

plist_org = []
plist_sec = []
plist_act = []
plist_mas = []
global sp
userTrackLim = 50

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



def downloadPlist(pid, name):
    # Creates the random playlists
    print("Downloading playlist info...")
    
    done = False
    ofs = 0
    plist_temp = []

    while done == False:

        playlist_id = 'spotify:playlist:' + pid
        results = sp.playlist_tracks(playlist_id,fields="items(track(name,artists(name),id,href)),total", offset=ofs, market="US")
        
        fw = open("config/playlist_org_"+name+"_part_"+str(int(ofs/100))+".json", "w")
        fw.write(json.dumps(results, indent=4))
        fw.close()

        print("Adding tracks to memory...")
        for x in range(len(results['items'])):
            plist_temp.append([results['items'][x]['track']['name'], results['items'][x]['track']['artists'][0]['name'], results['items'][x]['track']['id']])

        if results['total'] > ofs:
            ofs += 100
        else:
            done = True

    random.shuffle(plist_temp)
    plist_org.append(plist_temp)

def randPlists():
    
    print()

def exceptions():
    print()

def mixComb():
    print()

def dupCheck():
    print()


# Download the playlist tracks to json
for x, val in enumerate(config.gPlayl):
    print("Opening universal playlists...")
    downloadPlist(val, 'uni_'+ str(x))
    

for x, val in enumerate(config.playl):
    print("Opening personal playlists...")
    downloadPlist(val, 'per_'+ str(x))

plist_sec = plist_org
# plist_act = plist_org

# Creates a 3 day master track
z = 0
while z < 3:
    plist_act.append(plist_sec[0][z*50:userTrackLim]) # Appends global playlist
    for x in range(len(config.users)):
        plist_act.append(plist_sec[x+1][z*50:userTrackLim]) # Appends part of user plist based day
        print()
        
    random.shuffle(plist_act)
    plist_mas.append([plist_act])

    plist_act =[]
    z += 1
    

print(plist_org)