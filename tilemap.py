import pyxel
import time

from random import randint
from collections import namedtuple


"""
CONSTANTS
"""
HEIGHT = 255
Point = namedtuple("location", ['x','y'])
MIN_CLOUD_HEIGHT = HEIGHT - 90
CLOUD_V1 = {'u':0, 'v':16, 'w':16, 'h':16}
CLOUD_V2 = {'u':0, 'v':32, 'w':16, 'h':16}
CLOUD_V3 = {'u':16, 'v':16, 'w':16, 'h':16}
CLOUD_V4 = {'u':16, 'v':32, 'w':16, 'h':16}

class Background:
    
    def __init__(self,cloud_type = CLOUD_V1):
        cloud_y = randint(0,MIN_CLOUD_HEIGHT)
        self.cloud_type = cloud_type
        self.location = Point(255,cloud_y)



    def display_sky(self):
        self.show_sky()
        self.run_clouds()


    def update_clouds(self):
        #infinte loop trough clouds
        location = self.location
        self.location = self.location._replace(x = location.x - .5)


    def show_sky(self):
        pyxel.bltm(x= 0, y= 0, tm= 1, u= 0,v= 0, w= 35, h= 28 )
    

    def run_clouds(self):
        u= self.cloud_type.get('u')
        v= self.cloud_type.get('v')
        w= self.cloud_type.get('w')
        h= self.cloud_type.get('h')
        pyxel.blt(x= self.location.x, y= self.location.y, img = 2, u= u, v= v, w= w, h= h,colkey= 12)
