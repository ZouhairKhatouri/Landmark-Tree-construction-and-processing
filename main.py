"""
@Author : Niama ELKHBIR
@Last update : 22/03/2020
"""
## TODO : 

# Globals :
path = 'C:\\Users\\zouha\\Desktop\\Project\\'
N = 10 # Number of samples < 1101

# Imports :
from os import chdir
chdir(path)
from utils import *
from Classes.Image import *
from Classes.Viewframe import *
from Classes.Ltreemap import *

##

ltreemap = Ltreemap(None,[])

# Processing database images :
'''
for i in range(N):
    print("Processing: "+str(i))
    image = Image("DataBase\\"+getFileName(i))
    viewframe = image.getViewframe()
    ltreemap.add(viewframe)
print("Done !")
'''

# Test of correctness :

# number of biffurcations, must be 2!
'''
print(ltreemap.nbBiff())
'''

# must all be equal to N!
'''
print(ltreemap.nbLeafs())
print(ltreemap.nbViewframes)
print(len(ltreemap.getViewframes()))
'''

# Plotting the direction vector :
'''
ltreemap.plotDirectionVector()
'''

# Plotting keypoint above a source image :
'''
save_keypoints(path, 'source.jpg', 'new.jpg')
'''