import pyxel
from collections import namedtuple


Point = namedtuple("point",['x','y'])
WIDTH = 255
HEIGHT = 255
FLOOR = HEIGHT-50
START_LOCATION = Point((WIDTH/8),FLOOR)
LIVES_LOCATION = Point((5),HEIGHT-245)


class Corgi:
    def __init__(self):
        pyxel.init(WIDTH,HEIGHT,caption="Corgi",fps=40)
        pyxel.load("D:/pythonprojects/corgi/resources.pyxel")
        self.lives = 3
        self.velocity = 0
        self.jump = False
        self.walking = False
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

        self.walking = False
        if pyxel.btn(pyxel.KEY_RIGHT) and not pyxel.btn(pyxel.KEY_LEFT):
            self.walking = True
            if self.corgi_location.x < WIDTH -170:
                location = self.corgi_location
                self.corgi_location = location._replace(x=location.x + 1)

        if pyxel.btnp(pyxel.KEY_SPACE):
            if not self.jump:
                self.velocity = -10
                self.jump = True
            
        if not pyxel.btn(pyxel.KEY_RIGHT) and not pyxel.btn(pyxel.KEY_SPACE):
            self.draw_corgi_stand()

        if self.jump:
            self.velocity += 1
            location = self.corgi_location
            self.corgi_location = location._replace(y=location.y + self.velocity)

            if self.corgi_location.y > FLOOR:
                self.jump = False
                self.corgi_location = self.corgi_location._replace(y=FLOOR)
        
        
    def draw(self):
        pyxel.cls(0)
        self.draw_lives()
        self.display_corgi()

    def draw_lives(self):
        x =int(self.lives_location.x)
        for i in range (0,self.lives):
            pyxel.blt(x = x, y = self.lives_location.y, img = 0, u = 16, v = 0, w = 8, h = 8, colkey=0)
            x+=9

    def display_corgi(self):
        if self.walking:
            self.corgi_run_right()
        else:
            self.draw_corgi_stand()

    def draw_corgi_stand(self):
        pyxel.blt(x = self.corgi_location.x, y = self.corgi_location.y, img = 0, u = 0, v =0, w=11, h =12, colkey=1)

    def corgi_run_right(self):
        location = self.corgi_location

        if self.run_animation_right > 25: self.run_animation_right=0
        if self.run_animation_right<=25:
            pyxel.blt(x=location.x, y=location.y, img = 0, u = 0, v=16* (self.run_animation_right // 5), w=11, h=12, colkey=0)#+16h
            self.run_animation_right+=1

Corgi()
