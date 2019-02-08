import pyxel
import os

from corgi import Corgi
from bacon import Bacon
from ghosts import Ghost
from tilemap import Background
from collections import namedtuple

"""
CONSTANTS
"""
Point = namedtuple("point",['x','y'])
WIDTH = 255
HEIGHT = 255
FLOOR = HEIGHT-50
FPS = 50
START_LOCATION = Point((WIDTH/2),FLOOR)
LIVES_LOCATION = Point((5),HEIGHT-250)
OFFSET_LEFT = -6.5
OFFSET_RIGHT = 8.5
assets = os.path.join(os.getcwd(),os.path.dirname(__file__),'resources.pyxel')

class Game:

    """
    Initial objects and assets
    """
    def __init__(self):
        pyxel.init(WIDTH,HEIGHT,caption="Corgi",fps=FPS)
        pyxel.load(assets)
        self.corgi = Corgi(START_LOCATION)
        self.bacon = Bacon()
        self.ghost = Ghost()
        self.background = Background()
        self.offset_map = {-1: OFFSET_LEFT, 1: OFFSET_RIGHT}
        self.lives_location = LIVES_LOCATION
        pyxel.run(self.update, self.draw)
        
    """
    On update
    """
    def update(self):
        if self.corgi.lives != -1:  # check for life count
            self.corgi.update_corgi_location()
            self.ghost.update_ghosts()
            self.update_life_count()
            self.eat()
            self.track_location()
            self.background.update_clouds()

        else:
            pass      
        
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        
    def draw(self):
        pyxel.cls(0)
        self.background.display_sky()
        self.draw_lives()
        self.draw_floor()
        self.corgi.display_corgi()
        self.bacon.disaply_bacon()
        self.ghost.activate_ghost()


    def draw_floor(self):
        pyxel.bltm(x= 0,y= FLOOR+12,tm= 0,u= 0,v= 0,w= 35,h= 5)

    def draw_lives(self):
        x =int(self.lives_location.x)
        for heart in range (0,self.corgi.lives):
            pyxel.blt(x = x, y = self.lives_location.y, img = 0, u = 16, v = 0, w = 8, h = 8, colkey=0)
            x+=9

    def eat(self):
        direction = self.corgi.walking_direction
        offset = self.offset_map.get(direction)
        if not self.corgi.jump:
            if self.corgi.location.x + offset == self.bacon.location.x:
                self.bacon.eaten = True

              
    def update_life_count(self):
        direction = self.corgi.walking_direction
        offset = self.offset_map.get(direction)
        if self.corgi.location.x + offset + (self.corgi.walking_direction*.75) == self.ghost.location.x:
            if self.corgi.location.y < 210: 
                self.corgi.hit = True
                self.ghost.appear = False
    
    
    def track_location(self):
        print(self.corgi.location.y)
        print(self.ghost.location.x)
        print(self.ghost.location.y)
  

Game()
