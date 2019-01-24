import pyxel
import os

from corgi import Corgi
from collections import namedtuple


Point = namedtuple("point",['x','y'])
WIDTH = 255
HEIGHT = 255
FLOOR = HEIGHT-50
START_LOCATION = Point((WIDTH/8),FLOOR)
LIVES_LOCATION = Point((5),HEIGHT-245)
assets = os.path.join(os.getcwd(),os.path.dirname(__file__),'resources.pyxel')

class Game:
    def __init__(self):
        pyxel.init(WIDTH,HEIGHT,caption="Corgi",fps=60)
        pyxel.load(assets)
        self.corgi = Corgi(START_LOCATION)
        self.lives_location = LIVES_LOCATION
        self.run_animation = 0
        
        pyxel.run(self.update, self.draw)
        

    def update(self):
        if self.corgi.lives != -1:
            self.corgi.update_corgi_location()
            
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        

    def draw(self):
        pyxel.cls(0)
        self.draw_lives()
        self.corgi.display_corgi()
        self.draw_floor()

    def draw_floor(self):
        for brick in range (0,pyxel.width,15):
            pyxel.blt(brick, FLOOR+12, 1, 0, 8, 15, 9, 2)

    def draw_lives(self):
        x =int(self.lives_location.x)
        for heart in range (0,self.corgi.lives):
            pyxel.blt(x = x, y = self.lives_location.y, img = 0, u = 16, v = 0, w = 8, h = 8, colkey=0)
            x+=9

  

Game()