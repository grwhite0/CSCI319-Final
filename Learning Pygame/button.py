"""
Author: Gaby White
Learning Pygame
""" 

import pygame
import os
from drawable import Drawable
from vector import *
from constants import *

class Button(Drawable) :

    def __init__(self, position, fileName="", energy=2, id=0, playType=False, scrollType=False, offset=None):
        self.fileName = fileName
        path = os.path.join("images", self.fileName)
        self.image = pygame.image.load(path)
        super().__init__(self.image, position, offset)
        self.energy = energy
        self.playType = playType
        self.scrollType = scrollType
        self.id = id

        self.clicked = False
    
    def update(self, seconds):
        if not self.clicked and not self.playType :
            path = os.path.join("images", self.fileName)
            self.image = pygame.image.load(path)
        super().update(seconds)

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse_position = event.pos
            if self.getCollisionRect().collidepoint(event.pos) :
                if self.clicked and not self.playType :
                    path = os.path.join("images", "invert" + self.fileName)
                    self.image = pygame.image.load(path)
                elif not self.clicked and not self.playType :
                    path = os.path.join("images", self.fileName)
                    self.image = pygame.image.load(path)   

            if self.getCollisionRect().collidepoint(event.pos) and self.id == -100 :
                    self.CLICK += 1
                    if self.CLICK > 3 :
                        self.CLICK = 3
                    if self.CLICK == 0 :
                        if 1 <= self.id <= 4 :
                            self.position = vec(x, 104)
                            x += 195
                        x = 5
                        if 5 <= self.id <= 8 :
                            self.position = vec(x, 204)
                            x += 195
                        x = 5
                        if 9 <= self.id <= 12 :
                            self.position = vec(x, 304)
                            x += 195
                        else :
                            self.position = vec(-100, -100)

                    elif self.CLICK == 1 :                        
                        x = 5
                        if 5 <= self.id <= 8 :
                            self.position = vec(x, 104)
                            x += 195
                        x = 5
                        if 9 <= self.id <= 12 :
                            self.position = vec(x, 204)
                            x += 195
                        x = 5
                        if 13 <= self.id <= 16 :
                            self.position = vec(x, 304)
                            x += 195
                        else :
                            self.position = vec(-100, -100)
                    
                    elif self.CLICK == 2 :
                        x = 5
                        if 9 <= self.id <= 12 :
                            self.position = vec(x, 104)
                            x += 195
                        x = 5
                        if 13 <= self.id <= 16 :
                            self.position = vec(x, 204)
                            x += 195
                        x = 5
                        if 17 <= self.id <= 20 :
                            self.position = vec(x, 304)
                            x += 195
                        else :
                            self.position = vec(-100, -100)

                    elif self.CLICK == 3 :
                        x = 5
                        if 13 <= self.id <= 16 :
                            self.position = vec(x, 104)
                            x += 195
                        x = 5
                        if 17 <= self.id <= 20 :
                            self.position = vec(x, 204)
                            x += 195
                        x = 5
                        if 21 <= self.id <= 24 :
                            self.position = vec(x, 304)
                            x += 195
                        else :
                            self.position = vec(-100, -100)
                
            elif self.getCollisionRect().collidepoint(event.pos) :
                    self.CLICK -= 1
                    if self.CLICK < 0 :
                        self.CLICK = 0

                    if self.CLICK == 0 :
                        SCROLLBAR.position = vec(0,0)
                        x = 5
                        if 1 <= self.id <= 4 :
                            self.position = vec(x, 104)
                            x += 195
                        x = 5
                        if 5 <= self.id <= 8 :
                            self.position = vec(x, 204)
                            x += 195
                        x = 5
                        if 9 <= self.id <= 12 :
                            self.position = vec(x, 304)
                            x += 195
                        else :
                            self.position = vec(-100, -100)

                    elif self.CLICK == 1 :
                        SCROLLBAR.position = vec(0,100)
                        x = 5
                        if 5 <= self.id <= 8 :
                            self.position = vec(x, 104)
                            x += 195
                        x = 5
                        if 9 <= self.id <= 12 :
                            self.position = vec(x, 204)
                            x += 195
                        x = 5
                        if 13 <= self.id <= 16 :
                            self.position = vec(x, 304)
                            x += 195
                        else :
                            self.position = vec(-100, -100)
                    
                    elif self.CLICK == 2 :
                        SCROLLBAR.position = vec(0,200)
                        x = 5
                        if 9 <= self.id <= 12 :
                            self.position = vec(x, 104)
                            x += 195
                        x = 5
                        if 13 <= self.id <= 16 :
                            self.position = vec(x, 204)
                            x += 195
                        x = 5
                        if 17 <= self.id <= 20 :
                            self.position = vec(x, 304)
                            x += 195
                        else :
                            self.position = vec(-100, -100)

                    elif self.CLICK == 3 :
                        SCROLLBAR.position = vec(0,300)
                        x = 5
                        if 13 <= self.id <= 16 :
                            self.position = vec(x, 104)
                            x += 195
                        x = 5
                        if 17 <= self.id <= 20 :
                            self.position = vec(x, 204)
                            x += 195
                        x = 5
                        if 21 <= self.id <= 24 :
                            self.position = vec(x, 304)
                            x += 195
                        else :
                            self.position = vec(-100, -100)

        pass
        
    
