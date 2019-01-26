import pyxel
import os
import random

from collections import namedtuple


"""
CONSTANTS
"""
Point = namedtuple('location',['x','y'])
WIDTH = 255
HEIGHT = 255
FLOOR = HEIGHT-50
RIGHT = 255
LEFT = 0
BROCCOLI_HEIGHT = 150
DIRECTION_MAP = {RIGHT : 1, LEFT : -1}

#TODO: Implement score based number & different kinds of broccoli! (few heads)

class Broccoli:
    def __init__(self):
        self.location = Point((random.sample([LEFT,RIGHT],1)),BROCCOLI_HEIGHT)
        self.broccoli_direction = DIRECTION_MAP.get(self.location.x)
        self.max_broccoli = 1
        self.velocity = 0
        self.jump = False

    def display_broccoli(self):
        self.throw_broccoli()

    def update_broccolis(self):
        if self.location.x >= 0 and self.location.x <= 255:
            if not self.jump:
                self.velocity = -10
                self.jump = True

        if self.jump:
            self.velocity += 1
            location = self.location
            self.location = location._replace(y = location.y + self.velocity, x=location.x+1)

            if self.velocity > FLOOR:
                self.location = location._replace(y=FLOOR)
                self.velocity = -10




