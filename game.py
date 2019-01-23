import pyxel
from collections import namedtuple


Point = namedtuple("point",['x','y'])
WIDTH = 255
HEIGHT = 255
START_LOCATION = Point((WIDTH/8),HEIGHT-50)
LIVES_LOCATION = Point((5),HEIGHT-245)

class Corgi:
    def __init__(self):
        pyxel.init(WIDTH,HEIGHT,caption="Corgi",fps=40)
        self.assetes = pyxel.load("D:/pythonProjects/corgi/resources.pyxel")
        self.lives = 3
        self.velocity = 10
        self.jump = False
        self.corgi_location = START_LOCATION
        self.lives_location = LIVES_LOCATION
        self.run_animation_right = 0
        pyxel.run(self.update, self.draw)
        

    def update(self):
        if self.lives != -1:
            self.update_corgi_location()
        
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

    def update_corgi_location(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and not pyxel.btn(pyxel.KEY_LEFT):
            if self.corgi_location.x < WIDTH -170:
                old_location = self.corgi_location
                new_location = Point(old_location.x + 1, old_location.y )
                self.corgi_run_right(new_location)
            else:
                self.corgi_run_right(self.corgi_location) 
        if pyxel.btn(pyxel.KEY_SPACE):
            old_location = self.corgi_location
            self.jump = True

            if self.velocity >= -10:
                neg = 1
                if self.velocity < 0:
                    neg = -1
                new_location = Point (old_location.x,old_location.y-((self.velocity**2)*0.1*neg))
                self.velocity -=1
                self.corgi_run_right(new_location)
            else :                 
                self.velocity =10
                self.jump = False
                self.corgi_run_right (self.corgi_location)
            
        if not pyxel.btn(pyxel.KEY_RIGHT) and not pyxel.btn(pyxel.KEY_SPACE):
            self.draw_corgi_stand()
        
    def draw(self):
        pyxel.cls(0)
        self.draw_lives()
        self.update_corgi_location()

    def draw_lives(self):
        x =int(self.lives_location.x)
        for i in range (0,self.lives):
            pyxel.blt(x = x, y = self.lives_location.y, img = 0, u = 16, v = 0, w = 8, h = 8, colkey=0)
            x+=9

    def draw_corgi_stand(self):
        pyxel.blt(x = self.corgi_location.x, y = self.corgi_location.y, img = 0, u = 0, v =0, w=11, h =12, colkey=1)

    def corgi_run_right(self, new_location):
        if self.run_animation_right > 5: self.run_animation_right=0
        if self.run_animation_right<=5:
            pyxel.blt(x=new_location.x, y= self.corgi_location.y, img = 0, u = 0, v=16*self.run_animation_right, w=11, h=12, colkey=0)#+16h
            self.run_animation_right+=1
        self.corgi_location = new_location

Corgi()
