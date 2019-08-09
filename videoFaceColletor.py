import os
from dataScraper import faceshot

def folderScan():
    face = faceshot.faceFinder()
    cwd = os.getcwd()
    cwd +=  "/data"
    os.chdir(cwd)
    for folder in os.listdir():
        if(folder=="debug.log"):
            continue
        try:
            os.chdir(cwd+"/"+folder)
        except:
            continue

        print(folder)
        for file in os.listdir():
            if(file[-4:]=='webm'):
                print(file)
                face.isFaceVideo(file)

folderScan()