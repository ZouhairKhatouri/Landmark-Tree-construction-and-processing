"""
@Author : Niama ELKHBIR
@Last update : 22/03/2020
"""
## TODO : 

# Globals :
path = 'C:\\Users\\zouha\\Desktop\\Project\\'

# Imports :
from os import chdir
chdir(path)
from utils import *
from Classes.Image import *
from Classes.Viewframe import *
from Classes.Ltreemap import *

##

ltreemap = Ltreemap(None,[])

l = [ Landmark([],[i]) for i in range(10) ]

v1 = Viewframe([])
v2 = Viewframe([])
v3 = Viewframe([])
v4 = Viewframe([])
v5 = Viewframe([])

v1.add(l[1])
v1.add(l[2])
v1.add(l[4])

v2.add(l[1])
v2.add(l[3])
v2.add(l[5])
v2.add(l[6])

v3.add(l[1])
v3.add(l[3])
v3.add(l[5])
v3.add(l[7])

v4.add(l[1])
v4.add(l[3])
v4.add(l[5])
v4.add(l[8])
v4.add(l[9])

ltreemap.add(v1)
ltreemap.add(v2)
ltreemap.add(v3)
ltreemap.add(v4)

# number of biffurcations, must be 2!
print(ltreemap.nbBiff())

# must all be equal!
print(ltreemap.nbLeafs())
print(ltreemap.nbViewframes)
print(len(ltreemap.getViewframes()))