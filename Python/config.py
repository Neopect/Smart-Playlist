import os

confFile = []
id = "null"
secret = "null"
gPlayl = []
playl = []

# def init():
#     global confFile
#     global id
#     global secret
#     global gPlayl
#     global playl

# confFile = []
# id = "null"
# secret = "null"
# gPlayl = []
# playl = []

def genConfig():
    print("Generating config folder...")
    os.mkdir("config")

    print("Generating config file...")
    fw = open("config/config.conf", "w")
    fw.write("# Config file for SP\n\n# Credentials\n")
    fw.write("[Client-ID]\nInsert Client ID\n\n")
    fw.write("[Client-Secret]\nInsert Client Secret\n\n")
    fw.write("# Playlists\n")
    fw.write("# Example format conversion: https://open.spotify.com/playlist/2fhUKHlUCiCMdHKsFvg5Vf?si=91a60e2726964e1f --> spotify:playlist:2fhUKHlUCiCMdHKsFvg5Vf \n")
    fw.write("[Global-Playlists]\nInsert URI's for each global playlist\n\n")
    fw.write("[Playlists]\nInsert URI's for each users playlist\n\n")
    fw.close()

def readConfig():
    global id
    global secret
    global confFile
    global gPlayl
    global playl
    fw = open("config/config.conf", "r")
    for x in fw:
        confFile.append(x)
    print(confFile)
    
    # <<<<<<<<<<<<<<<<<< CLEAN FILE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    xdex = 0
    for x in confFile:
        if "#" in x:
            confFile.pop(xdex)
        xdex += 1
    print(confFile)

    xdex = 0
    for x in confFile:
        if x == "\n":
            confFile.pop(xdex)
        xdex += 1

    xdex = 0
    for x in confFile:
        if "\n" in x:
            confFile[xdex] = x.replace("\n","")
        xdex += 1

    xdex = 0
    for x in confFile:
        if x == "":
            confFile.pop(xdex)
        xdex += 1

    # =========================================================

    # global id
    id = confFile[1]
    # global secret
    secret = confFile[3]
    print(id)
    print(secret)

    xdex = 0
    ginst = False
    uinst = False
    for x, val in enumerate(confFile):

        if uinst == True:
            playl.append(val)
            print("Adding to playlist... " + val)
        if val == "[Playlists]":
            uinst = True
            ginst = False

        if ginst == True:
            gPlayl.append(val)
            print("Adding to global playlist... " + val)
        if val == "[Global-Playlists]":
            ginst = True

        
        
    print(id)
    print(secret)
    print(gPlayl)
    print(playl)
    # updateVar()

# def getID():
#     print(id)
#     return id

# def updateVar():
#     globals.confFile = confFile
#     print(id)
#     globals.id = id
#     globals.secret = secret
#     globals.gPlayl = gPlayl
#     globals.playl = playl