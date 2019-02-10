import pyxel
import random

from collections import namedtuple

"""
CONSTANTS
"""
Point = namedtuple ('location', ['x','y'])
WIDTH = 255
HEIGHT = 180
FLOOR = HEIGHT - 50
RIGHT = 0
LEFT = 255
DIRECTION_MAP = {RIGHT: 1 , LEFT: -1}
SMALL_GHOST = {'u':0, 'v':32, 'w':10, 'h':9}
MID_GHOST = {'u':0, 'v':48, 'w':16, 'h':12}
BIG_GHOST = {'u':0, 'v':48, 'w':16, 'h':15}
GHOST_TYPES = [SMALL_GHOST,MID_GHOST]

class Ghost:

    """
    Initial ghost
    """
    def __init__(self, ghost_type = MID_GHOST):
        self.ghost_type = ghost_type
        self.x = random.sample([RIGHT,LEFT],1)
        self.x = self.x[0]
        self.location = Point(self.x,FLOOR)
        self.ghost_direction = DIRECTION_MAP.get(self.x)
        self.ghost_animation = 0
        self.max_ghosts = 1
        self.appear = True

    """
    handle the ghost view
    """
    def display_ghost(self):
        if self.appear:
            self.activate_ghost()
        
    """
    update ghost state
    """
    def update_ghosts(self):
        if self.location.x >= -30 and self.location.x <= 270:
            location = self.location
            self.location = location._replace( x = location.x + (.75*self.ghost_direction))
        else:
            self.appear = False
            self.activate_ghost()

    """
    activate the ghosts to move on the map
    """
    def activate_ghost(self):
        if self.appear:
            location = self.location
            direction = self.ghost_direction

            #pairs of (u,v) and (w,h)
            u, v= self.ghost_type.get("u"), self.ghost_type.get("v")
            w, h= self.ghost_type.get("w"), self.ghost_type.get("h")
            if self.ghost_animation > 1:
                self.ghost_animation = 0
            if self.ghost_animation <= 1:
                pyxel.blt(x = location.x, y = location.y, img = 1, u = u, v = v, w = w*direction, h = h, colkey = 0)
                self.ghost_animation -=1
        else:
            ghost = random.choice(GHOST_TYPES)
            self.__init__(ghost_type= ghost)
