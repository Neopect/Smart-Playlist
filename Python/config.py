import os

confFile = []
id = "null"
secret = "null"
gPlayl = []
Playl = []

def genConfig():
    print("Generating config folder...")
    os.mkdir("config")

    print("Generating config file...")
    fw = open("config/config.conf", "w")
    fw.write("# Config file for SP\n\n# Credentials\n")
    fw.write("[Client-ID]\nInsert Client ID\n\n")
    fw.write("[Client-Secret]\nInsert Client Secret\n\n")
    fw.write("# Playlists\n")
    fw.write("[Global-Playlists]\nInsert URI's for each global playlist\n\n")
    fw.write("[Playlists]\nInsert URI's for each users playlist\n\n")
    fw.close()

def readConfig():
    fw = open("config/config.conf", "r")
    for x in fw:
        confFile.append(x)
    print(confFile)
    # Clean file
    xdex = 0
    for x in confFile:
        if x == '\n' or "#" in x:
            print("removing x=" + str(x) +" xdex= " + str(xdex) + "\n")
            # confFile.pop(xdex)
            if xdex != 0:
                 confFile.pop(xdex-1)
            else:
                confFile.pop(xdex)
        print(confFile)
        xdex += 1
    
    # xdex = 0
    # for x in confFile:
    #     if x == "\n":
    #         confFile.pop(xdex)
    #     elif "\n" in x:
    #        confFile[xdex] = x.strip('\n')
        
    #     xdex += 1
    

    
