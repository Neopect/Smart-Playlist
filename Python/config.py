import os.path

file_exists = os.path.isdir("test")

print(file_exists)

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
