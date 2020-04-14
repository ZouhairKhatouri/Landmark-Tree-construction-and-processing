"""
@Author : Niama ELKHBIR
@Last update : 22/03/2020
"""
## TODO :

# Globals :

# Imports :
from math import cos, sin, pi

##

class Landmark:
    
    # angles : list of floats, with size 360
    # descriptors : list of floats, with size 64
    def __init__(self , angles = [], descriptor = []):
        self.angles = angles
        self.descriptor = descriptor
        
    def __eq__(self, l):
        return isinstance(l,Landmark) and self.angles == l.angles and self.descriptor == l.descriptor
        
    # Mean cosinus of the angles of self
    def cos(self):
        Z = sum([a for a in self.angles])
        if Z != 0:
            return sum([self.angles[i]*cos(i*pi/180) for i in range(len(self.angles))])/Z
        else:
            return 0
            
    # Mean sinus of the angles of self
    def sin(self):
        Z = sum([a for a in self.angles])
        if Z != 0:
            return sum([self.angles[i]*sin(i*pi/180) for i in range(len(self.angles))])/Z
        else:
            return 0