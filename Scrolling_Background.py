from pygame import *
import pygame.image
height = 600
class Background:
    def __init__(self, surface):
        self.surface = surface
        self.reset()
        self.scrolling = True

    def move(self, speed, image):
        if self.scrolling:
            self.y1 +=speed
            self.y2 +=speed

            if self.y1 ==height:
                self.y1 = -height
            if self.y2 ==height:
                self.y2 = -height
        self.surface.blit(image, (0, self.y1))
        self.surface.blit(image, (0, self.y2))
    def reset(self):
        self.y1 = 0
        self.y2 = -600
        

