
# -*-coding:utf-8-*-
# Author: 
# Email: wp2204@gmail.com

import numpy as np
from math import *

def normalize(v):
    norm=np.linalg.norm(v)
    if norm==0:
       return v
    return v/norm


class obst(object):
    
    """
    screen: (Not used)
        Obstacles exists on a screen element 
    id:
        obstacle id 
    mode: 
        obstacle type (Line, Rect, Circle)
    params:
        Obstacle parameters according to the type. This in the form 
        of: Line -> [x1,y1,x2,y2]
        Rect -> [x,y,w,h] 
        Circle -> [x,y,r,None]
    """
    
    def __init__(self, oid=0, mode='line', params=[0,0,0,0]):
        
        self.params = np.array([0.0, 0.0, 0.0, 0.0])
        self.id = 0
        self.mode = 'line'
        
        #self.startPx = np.array([params[0], params[1]])
        #self.endPx = np.array([params[2], params[3]])
        
        self.attachedDoors=[]
        self.isSingleWall = False
        self.inComp = 1
        self.arrow = 0
        #self.direction = None #self.arrow*normalize(self.endPx - self.startPx)
        self.pointer1 = np.array([float('NaN'), float('NaN')])
        self.pointer2 = np.array([float('NaN'), float('NaN')])


    def direction(self, arrow):
        if self.mode=='line':
            # Direction: (StartX, StartY) --> (EndX, EndY)
            direction = -np.array([self.params[0], self.params[1]]) -np.array([self.params[2], self.params[3]])
            direction = normalize(direction)
            if arrow>0:
                return direction
            elif arrow<0:
                return -direction
            elif arrow==0:
                return np.array([0.0, 0.0])
        
        elif self.mode=='rect':
            pass
            # What is a good representation of no direction?  
            direction = None  # np.array([0.0, 0.0])  #NaN

            ### +1: +x
            ###  -1: -x
            ### +2: +y
            ###  -2: -y 
            if arrow == 1:
                direction = np.array([1.0, 0.0])
            elif arrow == -1:
                direction = np.array([-1.0, 0.0])
            elif arrow == 2:
                direction = np.array([0.0, 1.0])
            elif arrow == -2:
                direction = np.array([0.0, -1.0])
            elif arrow == 0:
                direction = np.array([0.0, 0.0])
            return direction
    
    

class passage(object):
    
    """
    screen: (Not used)
        Passages exist on a screen element 
    id:
        door id 
    mode: 
        door type (Rect, Circle)
    params:
        Obstacle parameters according to the type. This in the form 
        of: Rect -> [x,y,w,h] 
        Circle -> [x,y,r,None]
    """
    
    def __init__(self, oid=0, mode='rect', params=[0,0,0,0]):
        
        self.params = np.array([0.0, 0.0, 0.0, 0.0])
        self.oid = 0
        #self.mode = 'rect' # All the door are in form of rect
        self.exitSign = 0

        #self.startPx = np.array([params[0], params[1]])
        #self.endPx = np.array([params[2], params[3]])

        self.attachedWalls=[]
        self.inComp = 1
        self.isSingleDoor = False
        self.arrow = 1
        #self.direction = None #self.arrow*normalize(self.endPx - self.startPx)
        #self.pointer1 = np.array([0, 0])
        #self.pointer2 = np.array([0, 0])
        self.pos = (np.array([self.params[0], self.params[1]]) + np.array([self.params[2], self.params[3]]))*0.5


    def direction(self, arrow):
        ### +1: +x
        ###  -1: -x
        ### +2: +y
        ###  -2: -y 
        if arrow == 1:
            direction = -np.array([self.params[0], self.params[3]]) -np.array([self.params[2], self.params[3]])
            direction = normalize(direction)
            direction = np.array([1.0, 0.0])
        elif arrow == -1:
            direction = np.array([self.params[0], self.params[3]]) -np.array([self.params[2], self.params[3]])
            direction = normalize(direction)
            direction = np.array([-1.0, 0.0])
        elif arrow == 2:
            direction = -np.array([self.params[0], self.params[1]]) -np.array([self.params[0], self.params[3]])
            direction = normalize(direction)
            direction = np.array([0.0, 1.0])
        elif arrow == -2:
            direction = np.array([self.params[0], self.params[1]]) -np.array([self.params[0], self.params[3]])
            direction = normalize(direction)
            direction = np.array([0.0, -1.0])
        elif arrow == 0:
            direction = np.array([0.0, 0.0])
        return direction
            

    def edge(self):
        p1 = np.array([self.params[0], self.params[1]])
        p2 = np.array([self.params[0], self.params[3]])
        p3 = np.array([self.params[2], self.params[3]])
        p4 = np.array([self.params[2], self.params[1]])
        return p1, p2, p3, p4




if __name__ == '__main__':
    obst = obst()
    print ('OBST Test OK')
    
    doorTest2 = passage()
    doorTest2.params = np.array([60.3, 3.0, 66.0, 6.0])
    doorTest2.arrow = -2
    #doorTest2.visiblePx(pos, walls):
    print (doorTest2.direction(-2))
    print (doorTest2.edge())

    doorTest3 = passage()
    doorTest3.params = np.array([18.9, 16, 23, 20])
    doorTest3.arrow = 1
    print (doorTest3.direction(doorTest3.arrow))
    print ('DOOR Test OK')
