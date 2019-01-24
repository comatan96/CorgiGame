import pyxel

from collections import namedtuple
from random import randint

Point = namedtuple('location',['x','y'])
WIDTH = 255
HEIGHT = 255
FLOOR = HEIGHT-50

class Bacon:

    def __init__(self):
        self.location = Point(randint(0,WIDTH),FLOOR)

    def appear(self):
        pyxel.blt(x=self.location.x,y=self.location.y,img = 1, u=16,v=0,w=7,h=7,colkey=0)

    def eaten(self):
        self.location = Point(randint(0,WIDTH),FLOOR)
        pyxel.cls(0)
        self.appear()
