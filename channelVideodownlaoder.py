import cv2
import os
import time
from pytube import YouTube
from dataScraper import faceshot

class channelSearch:
    def __init__(self):
        search = "channelList.txt"
        with open(search) as f:
            terms = f.read().splitlines()

        self.channelNames=[]
        self.channelLinks=[]
        for i,line in enumerate(terms):
            if(i%2==0):
                self.channelNames.append(line)
            else:
                self.channelLinks.append(line)

        self.videoCount = 0
        self.face = faceshot.faceFinder()

    def getLinks(self,neededLinks = 3,channels = 25):
        cwd = os.getcwd()
        cwd += '/data'
        os.chdir(cwd)

        channelCount = 0
        linkCount = 0
        for folder in os.listdir():
            print(folder)
            try:
                os.chdir(cwd+"/"+folder)
            except:
                continue

            fileName = folder+".txt"
            try:
                with open(fileName) as f:
                    content = f.readlines()

            except:
                continue

            for line in content:
                print("link - ",line),
                linkCount += 1
                self.videoDownloader(line)
                if(linkCount>neededLinks):
                    linkCount = 0
                    break

            channelCount += 1

            os.chdir(cwd)
            if(channelCount>channels):
                break

        print("Downloaded ALL")

    def videoDownloader(self,url):
        yt = YouTube(url)
        # print(yt.streams.all())
        # fileSizes = []
        for st in yt.streams.all():
            # print(dir(st),st.resolution)
            if(st.resolution=='360p' and st.subtype=='webm'):
                self.videoCount += 1
                # fileSizes.append(st)
                print("downloading ",self.videoCount)
                st.download()
                return

if __name__=='__main__':
    n = channelSearch()
    n.getLinks()
