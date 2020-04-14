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
from Classes.Landmark import *
from Classes.Viewframe import *
from numpy import array
import matplotlib.pyplot as plt

##

class Ltreemap:
    
    # root : landmark
    # childs : list of Ltreemaps
    def __init__(self , root , childs):
        self.root = root
        self.childs = childs
        self.nbViewframes = 0
        self.viewframes = self.getViewframes()
    
    # adds the viewframe to self
    def add(self , viewframe):
        # Recursivity :
        
        if viewframe.landmarks == []:
            return
            
        if self.childs != []:
            for c in self.childs:
                if c.root in viewframe.landmarks:
                    c.add(Viewframe([l for l in viewframe.landmarks if l != self.root]))
                    self.nbViewframes += 1
                    return
        
        self.childs.append(Ltreemap.toTree(Viewframe([l for l in viewframe.landmarks if l != self.root])))
        self.nbViewframes += 1
        self.viewframes.append(viewframe)
        
    # Changes a viewframe to a flat vertical tree
    def toTree(viewframe):
        res = []
        n = len(viewframe.landmarks)
        for i in range(n):
            res = [Ltreemap(viewframe.landmarks[n-i-1],res)]
        return res.pop()

    # Counts the number of biffurcations in a tree
    def nbBiff(self):
        # DE : depth exploration
        pile = [] #DE
        pile.append(self) #DE
        
        nb = 0
        
        while pile != []: #DE
            cur = pile.pop() #DE
            
            if len(cur.childs)>1:
                nb += 1
                
            for c in cur.childs: #DE
                pile.append(c) #DE
                
        return nb
        
    # Counts the number of leafs in a tree, must be equal to the number of viewframes !
    def nbLeafs(self):
        # DE : depth exploration
        pile = [] #DE
        pile.append(self) #DE
        
        nb = 0
        
        while pile != []: #DE
            cur = pile.pop() #DE
            
            if len(cur.childs)<1:
                nb += 1
                
            for c in cur.childs: #DE
                pile.append(c) #DE
                
        return nb
        
    # Updates and returns the viewframes of self
    def getViewframes(self):
        self.viewframes = []
        
        #  DE : depth exploration
        pile = [] #DE
        pile.append(self) #DE
        path = []
        while pile != []: #DE
            cur = pile.pop() #DE
            
            # while the last node in the path is not the father of the current processed node, we must pop it!
            prev_cur = None
            if path != []:
                prev_cur = path.pop()
            while prev_cur != None and cur not in prev_cur.childs:
                prev_cur = path.pop()
            if prev_cur != None:
                path.append(prev_cur) # at the end, we must return the correct father to the path if not null
            path.append(cur)
            
            if cur.childs == []:
                self.viewframes.append(Viewframe([x.root for x in path if x.root != None]))
            
            for c in cur.childs: #DE
                pile.append(c) #DE
                
        return self.viewframes
        
    # Plots the y-coordinates of the direction vector as a function of the x-coordinates of the direction vector
    def plotDirectionVector(self):
        # X = np.array([i for i in range(self.nbViewframes)])
        T2 = array([v.t() for v in self.viewframes])
        T1 = array(list(T2)[1:]+[array([0,0])])
        T = T2-T1
        Tx = [t[0] for t in T]
        Ty = [t[1] for t in T]
        plt.plot(Tx,Ty)
        plt.title("Direction vector in time")
        plt.xlabel("x coordinate of the direction vector")
        plt.ylabel("y coordinate of the direction vector")
        plt.show()