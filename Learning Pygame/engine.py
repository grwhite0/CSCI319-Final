"""
Author: Gaby White
Learning Pygame
""" 

import pygame
from drawable import Drawable
from os.path import join
from constants import *
from button import Button

class GameEngine(object):

    def __init__(self):
        
        bg = pygame.image.load("background.png").convert()        
        self.background = Drawable(bg, (0,0))

        self.mouseOffset = vec(0,0)
    
    def draw(self, drawSurface):
        drawSurface.fill((255,255,255))
        
        self.background.draw(drawSurface)

        #color = self.star.get_at((0,0))

        #self.star.set_colorkey(color)

        #self.star.draw(drawSurface)
            
    def handleEvent(self, event): 
        pass
       
        #self.star.handleEvent(event)        
    
    def update(self, seconds):
        pass

    
        

