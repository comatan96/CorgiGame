import pyxel
import os
from collections import namedtuple

"""
CONSTANTS
"""
Point = namedtuple('location',['x','y'])
WIDTH = 255
HEIGHT = 180
FLOOR = HEIGHT - 50
START_LOCATION = Point((WIDTH/8),FLOOR)

class Corgi:
    def __init__(self, start_location):
        """
        Initializing the default corgi values
        """
        self.lives = 3
        self.velocity = 0
        self.jump = False
        self.walking = False 
        self.walking_direction = 1 # direction : 1=right , -1=left
        self.location = start_location
        self.run_animation = 0
        self.hit = False


    """
    handle the displaying of the corgi
    """
    def display_corgi(self):
        if self.walking:
            self.corgi_run()
        else:
            self.draw_corgi_stand()

    """
    handle the corgi state changing
    """
    def update_corgi_location(self):
        self.walking = False
        if pyxel.btn(pyxel.KEY_RIGHT) and not pyxel.btn(pyxel.KEY_LEFT):
            self.walking = True
            self.walking_direction = 1
            if self.location.x < WIDTH - 12:
                location = self.location
                self.location = location._replace(x=location.x + 1)

        if pyxel.btn(pyxel.KEY_LEFT) and not pyxel.btn(pyxel.KEY_RIGHT):
            self.walking = True
            self.walking_direction = -1
            if self.location.x > 0:
                location = self.location
                self.location = location._replace(x=location.x-1)

        if pyxel.btnp(pyxel.KEY_SPACE):
            if not self.jump:
                self.velocity = -10
                self.jump = True
            
        if not self.walking and not self.jump:
            self.draw_corgi_stand()

        if self.jump:
            self.velocity += 1
            location = self.location
            self.location = location._replace(y=location.y + self.velocity)

            if self.location.y > FLOOR:
                self.jump = False
                self.location = self.location._replace(y=FLOOR)
        
        if self.hit:
            location = self.location
            self.velocity = -9
            self.jump = True
            self.location = self.location._replace(x = location.x + (10*self.walking_direction))
            self.lives -=1
            self.hit = False
        
    """
    handle corgi animations - standing and running
    """
    def draw_corgi_stand(self):
        direction = self.walking_direction
        pyxel.blt(x = self.location.x, y = self.location.y, img = 0, u = 0, v =0, w=11*direction, h =12, colkey=0)

    def corgi_run(self):
        location = self.location
        direction = self.walking_direction

        if self.run_animation > 25:
            self.run_animation=0
        if self.run_animation <= 25:
            pyxel.blt(x=location.x, y=location.y, img = 0, u = 0, v=16* (self.run_animation // 5), w=11*direction, h=12, colkey=0)
            self.run_animation+=1

