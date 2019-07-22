import numpy as np
from PIL import ImageGrab
from PIL import Image
import cv2
import time
import os

class faceFinder:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('face.xml')

    def isFace(self,folderName='',timeout=540,facesNeed = 5,sleeptime=5):
        t = time.time()
        cwd = os.getcwd()
        faceFound = 0
        try:
            os.chdir(folderName)
        except:
            os.makedirs('./'+folderName)
            os.chdir(folderName)

        while(True):
            t1 = time.time()
            printscreen_pil =  ImageGrab.grab()
            printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
            .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
            # cv2.imshow('window',printscreen_numpy)
            gray =cv2.cvtColor(printscreen_numpy,cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(gray,1.1,5)

            for (x,y,w,h) in faces:
                img = Image.fromarray(printscreen_numpy)
                img.save(folderName+"face"+str(faceFound+1)+".jpeg")
                cv2.rectangle(printscreen_numpy,(x, y), (x + w, y + h), (255, 0, 0), 2)
                print("FACE FOUND")
                # cv2.imshow('face',printscreen_numpy)

                faceFound += 1
                time.sleep(sleeptime)
                if(faceFound>=facesNeed):
                    os.chdir(cwd)
                    return 1

            if(t1-t>timeout):
                os.chdir(cwd)
                return 0

if __name__=="__main__":
    f = faceFinder()
    f.isFace('test1')