import pyxel
import time
import random
from collections import namedtuple


"""
CONSTANTS
"""
HEIGHT = 180
Point = namedtuple("location", ['x','y'])
MIN_CLOUD_HEIGHT = HEIGHT - 90
CLOUD_V1 = {'u':0, 'v':0, 'w':96, 'h':32}
CLOUD_V2 = {'u':0, 'v':32, 'w':96, 'h':32}
class Background:
    """
    Initial the clouds with V1 cloud as first cloud
    """
    def __init__(self,cloud_type = CLOUD_V1):
        first_cloud_y = random.randint(0,MIN_CLOUD_HEIGHT)
        second_cloud_y = random.randint(0,MIN_CLOUD_HEIGHT)
        self.cloud_type = cloud_type
        self.first_cloud_location = Point(255, first_cloud_y)
        self.second_cloude_location = Point(420, second_cloud_y)

    """
    handle drawing session
    """
    def disaply_background(self):
        self.show_sky()
        self.run_clouds()

    """
    on game update
    """
    def update_clouds(self):
        if self.first_cloud_location.x >= -200:
            first_location = self.first_cloud_location
            self.first_cloud_location = self.first_cloud_location._replace(x= first_location.x - .5)
            second_location = self.second_cloude_location
            self.second_cloude_location = self.second_cloude_location._replace(x= second_location.x - .6)

        elif self.first_cloud_location.x < -200 :
            first_cloud_y = random.randint(0,MIN_CLOUD_HEIGHT)
            self.first_cloud_location = self.first_cloud_location._replace(x = 255, y= first_cloud_y)

        if self.second_cloude_location.x < -200:
            second_cloud_y = random.randint(0,MIN_CLOUD_HEIGHT)
            self.second_cloude_location = self.second_cloude_location._replace(x = 420, y= second_cloud_y)

    """
    show the sky
    """
    def show_sky(self):
        pyxel.bltm(x= 0, y= 0, tm= 1, u= 0,v= 0, w= 35, h= 28 )
    
    """
    run the clouds in the background
    """
    def run_clouds(self):
        # pairs of (u,v) and (w,h)
        u1, v1= CLOUD_V1.get('u'), CLOUD_V1.get('v')
        w1, h1= CLOUD_V1.get('w'), CLOUD_V1.get('h')

        u2, v2= CLOUD_V2.get('u'), CLOUD_V2.get('v')
        w2, h2= CLOUD_V2.get('w'), CLOUD_V2.get('h')

        # save locations in new variable
        first_loc = self.first_cloud_location
        second_loc = self.second_cloude_location

        # draw clouds
        pyxel.blt(x= first_loc.x, y= first_loc.y, img = 2, u= u1, v= v1, w= w1, h= h1, colkey= 12)
        pyxel.blt(x= second_loc.x, y= second_loc.y, img = 2, u= u2, v= v2, w= w2, h= h2, colkey= 12)

