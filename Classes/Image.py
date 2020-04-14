"""
@Author : Niama ELKHBIR
@Last update : 21/03/2020
"""
## TODO :

# Globals :
path = 'C:\\Users\\zouha\\Desktop\\Project\\'

# Imports :
from os import chdir
chdir(path)
from Classes.Landmark import *
from Classes.Viewframe import *
import cv2
from math import floor

##

class Image:
    
    N = 10
    threshold = 100
    
    def __init__(self, path):
        self.path = path
        self.viewframe = None
    
    def getKeyPointsAndDescriptors(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        return cv2.BRISK_create(Image.N).detectAndCompute(gray,None)
        
    def getViewframe(self):
        if self.viewframe is None:
            kp, descriptors = self.getKeyPointsAndDescriptors()
            self.viewframe = Viewframe([])
            for i in range(len(kp)):
                if kp[i].response >= Image.threshold:
                    angles = [0 for i in range(360)]
                    angles[floor(kp[i].angle)] = 1
                    lm = Landmark(angles, list(descriptors[i]))
                    self.viewframe.add(lm)
        return self.viewframe