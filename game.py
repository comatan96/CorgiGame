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
HEIGHT = 180
FLOOR = HEIGHT-50
FPS = 50
START_LOCATION = Point((WIDTH/2),FLOOR)
LIVES_LOCATION = Point(5,HEIGHT//90)
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
    update all objects inside the game window each frame
    """
    def update(self):
        # as long as the corgi have lives
        if self.corgi.lives != -1:
            self.corgi.update_corgi_location()
            self.ghost.update_ghosts()
            self.update_life_count()
            self.eat()
            self.background.update_clouds()

        #handle quit buttons
        if pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
    """
    On draw
    Handle the drawing of those:
    Corgi, Bacons, Clouds, Sky, Floor, Lives and ghosts!
    """
    def draw(self):
        pyxel.cls(0)
        self.background.disaply_background()
        self.draw_lives()
        self.draw_floor()
        self.corgi.display_corgi()
        self.bacon.disaply_bacon()
        self.ghost.activate_ghost()

        # Draw score
        pyxel.text(x= WIDTH/1.275, y= HEIGHT//90, s="score: " + str(self.bacon.SCORE), col = 7)

        # if out of lives
        if self.corgi.lives == -1:
            pyxel.cls(0)
            pyxel.text(x = WIDTH/2, y= HEIGHT/2, s= "GAME OVER", col= 1)

    """
    handle floor drawing
    """
    def draw_floor(self):
        pyxel.bltm(x= 0,y= FLOOR+12,tm= 0,u= 0,v= 0,w= 35,h= 5)

    """
    handle lives drawing
    """
    def draw_lives(self):
        x =int(self.lives_location.x)
        for heart in range (0,self.corgi.lives):
            pyxel.blt(x = x, y = self.lives_location.y, img = 0, u = 16, v = 0, w = 8, h = 8, colkey=0)
            x+=9

    """
    handle the eating mechanism
    """
    def eat(self):
        if not self.corgi.jump:
            if abs(self.corgi.location.x - self.bacon.location.x) <= 8:
                self.bacon.eaten = True
                self.bacon.SCORE +=20

    """
    handle the life count with ineraction with ghosts
    """    
    def update_life_count(self):
        if abs(self.corgi.location.x - self.ghost.location.x) <= 8:
            if self.corgi.location.y > HEIGHT - 60: 
                self.corgi.hit = True
                self.ghost.appear = False
                self.bacon.SCORE -= 10
        pyxel.text(x = 200, y= 30, s = "-10", col = 8)

Game()
