import pyxel

from collections import namedtuple
from random import randint

Point = namedtuple('location',['x','y'])
WIDTH = 255
HEIGHT = 255
FLOOR = HEIGHT-50

class Bacon:

    def __init__(self):
        self.location = Point(randint(0,WIDTH-7),FLOOR+2)
        self.eaten = False

    def disaply_bacon(self):
        if not self.eaten:
            self.draw_bacon()
        else:
            self.update_bacon_location()
      
    def update_bacon_location(self):
            location = self.location
            self.location = location._replace(x=randint(0,WIDTH-15))
            self.eaten = False

    
    def draw_bacon(self):
        location = self.location
        #pyxel.cls(0)
        pyxel.blt(x=location.x,y=location.y,img = 1, u=16,v=0,w=7,h=7,colkey=0)

  


        
