import pyxel
import os
from collections import namedtuple

Point = namedtuple('location',['x','y'])
WIDTH = 255
HEIGHT = 255
FLOOR = HEIGHT - 50
START_LOCATION = Point((WIDTH/8),FLOOR)
assets = os.path.join(os.getcwd(),os.path.dirname(__file__),'resources.pyxel')
class Corgi:
    def __init__(self, start_location):
        pyxel.load(assets)
        self.lives = 3
        self.velocity = 0
        self.jump = False
        self.walking = False
        self.walking_direction = 1
        self.location = start_location

        self.run_animation = 0

    def display_corgi(self):
        if self.walking:
            self.corgi_run_right()
        else:
            self.draw_corgi_stand()


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
            
    
    def draw_corgi_stand(self):
        direction = self.walking_direction
        pyxel.blt(x = self.location.x, y = self.location.y, img = 0, u = 0, v =0, w=11*direction, h =12, colkey=0)

    def corgi_run_right(self):
        location = self.location
        direction = self.walking_direction

        if self.run_animation > 25: self.run_animation=0
        if self.run_animation <= 25:
            pyxel.blt(x=location.x, y=location.y, img = 0, u = 0, v=16* (self.run_animation // 5), w=11*direction, h=12, colkey=0)
            self.run_animation+=1
