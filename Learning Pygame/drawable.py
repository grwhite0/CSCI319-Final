"""
Author: Gaby White
Learning Pygame
""" 

import pygame
import os
from vector import *

class Drawable(object) :

    def __init__(self, image, position=vec(0,0), offset=None):
        
        self.image = image

        self.position=vec(*position)

    def draw(self, surface) :

        surface.blit(self.image, self.position)

    def getPosition(self) :
        return self.position
    
    def setPosition(self, position) :
        self.posiiton = position

    #FINISH
    def getSize(self) :
        return vec(*self.image.get_size())

    def getWidth(self) :
        return self.getSize()[0]
    
    def getHeight(self) :
        return self.getSize()[1]

    def handleEvent(self, event) :
        pass

    def update(self, seconds) :
        pass

    def getCollisionRect(self) :
        return rectAdd(self.getPosition(), self.image.get_rect())
