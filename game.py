import pyxel
import os

from corgi import Corgi
from bacon import Bacon
from collections import namedtuple


Point = namedtuple("point",['x','y'])
WIDTH = 255
HEIGHT = 255
FLOOR = HEIGHT-50
START_LOCATION = Point((WIDTH/2),FLOOR)
LIVES_LOCATION = Point((5),HEIGHT-250)
LEFT_BACON = -6.5
RIGHT_BACON = 8.5
assets = os.path.join(os.getcwd(),os.path.dirname(__file__),'resources.pyxel')

class Game:
    def __init__(self):
        pyxel.init(WIDTH,HEIGHT,caption="Corgi",fps=50)
        pyxel.load(assets)
        self.corgi = Corgi(START_LOCATION)
        self.bacon = Bacon()
        self.bacon_offset = {-1: LEFT_BACON, 1: RIGHT_BACON}
        self.lives_location = LIVES_LOCATION
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if self.corgi.lives != -1:
            self.corgi.update_corgi_location()
            self.eat()
            self.track_location()
              
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        
    def draw(self):
        pyxel.cls(0)
        self.draw_lives()
        self.draw_floor()
        self.corgi.display_corgi()
        self.bacon.disaply_bacon()

    def draw_floor(self):
        pyxel.bltm(x=0,y=FLOOR+12,tm=0,u=0,v=0,w=35,h=5)

    def draw_lives(self):
        x =int(self.lives_location.x)
        for heart in range (0,self.corgi.lives):
            pyxel.blt(x = x, y = self.lives_location.y, img = 0, u = 16, v = 0, w = 8, h = 8, colkey=0)
            x+=9

    def eat(self):
        direction = self.corgi.walking_direction
        offset = self.bacon_offset.get(direction)
        if not self.corgi.jump:
            if self.corgi.location.x+(offset) == self.bacon.location.x:
                self.bacon.eaten = True
            
    
    def track_location(self):
        print(self.corgi.location.x)
        print(self.bacon.location.x)
  

Game()
