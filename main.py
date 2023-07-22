import sys
import pygame.image
import pygame
from pygame import *
import random
pygame.font.init()
pygame.mixer.init()
from PySide6.QtWidgets import QApplication, QPushButton  
from SaveSystem import SaveandLoad
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
laser = pygame.mixer.Sound(resource_path("Player laser.wav"))
explosion = pygame.mixer.Sound(resource_path("explosion.wav"))
laser1 = pygame.mixer.Sound(resource_path("enemy laser.wav"))
hurt = pygame.mixer.Sound(resource_path("hurt.wav"))
red = pygame.image.load(resource_path(r"red.png"))

save = SaveandLoad(".level_data", "Space invaders stuff" )
class GameOver(Exception):
    pass
class Projectile:
    def __init__(self, screen,  y):

        self.color = (30, 30, 30)
        self.difference = 0
        self.num = 0
        self.four = 435
        self.y = y
        self.y1 = y
        self.y2 = y
        self.y3 = y
        self.y4 = y
        self.y5 = y
        self.y6 = y
        self.y7 = y
        self.y8 = y
        self.y9 = y
        self.ys = [self.y, self.y1, self.y2, self.y3, self.y4, self.y5, self.y6, self.y7, self.y8, self.y9]
        self.screen = screen
        self.laser_sideways = pygame.image.load(resource_path("laser.png"))
        self.laser = pygame.transform.rotate(self.laser_sideways, 90)
        self.laser1 = pygame.transform.rotate(self.laser_sideways, 90)
        self.laser2 = pygame.transform.rotate(self.laser_sideways, 90)
        self.laser3 = pygame.transform.rotate(self.laser_sideways, 90)
        self.laser4 = pygame.transform.rotate(self.laser_sideways, 90)
        self.laser5 = pygame.transform.rotate(self.laser_sideways, 90)
        self.laser6 = pygame.transform.rotate(self.laser_sideways, 90)
        self.laser7 = pygame.transform.rotate(self.laser_sideways, 90)
        self.laser8 = pygame.transform.rotate(self.laser_sideways, 90)
        self.laser9 = pygame.transform.rotate(self.laser_sideways, 90)
        self.laser_list = [self.laser, self.laser1, self.laser2, self.laser3, self.laser4, self.laser5, self.laser6, self.laser7, self.laser8, self.laser9]

    def draw_projectile(self):
        self.screen.blit(self.laser_list[self.num], (self.four + self.difference, self.ys[self.num]))



class Player:
    def __init__(self, x, y, screen):
        self.background =pygame.image.load(resource_path("Background.png"))
        self.health = 5
        self.screen = screen
        self.shooter = pygame.image.load(resource_path("Space-Invaders-Ship-PNG-Photo.png"))
        self.x = x
        self.y = y
    def draw_shooter(self):

        self.screen.fill((0, 0, 0))

        self.screen.blit(self.shooter, (self.x, self.y))
    def draw_health(self):

        font1 = pygame.font.SysFont("Typeface Mario World Pixel Filled", 400, bold=False, italic=False)
        if self.health <= 2:
            self.color = (50, 0, 0)
        else:
            self.color = (30, 30, 30)
        line = font1.render(str(self.health), False, self.color)
        self.screen.blit(line, (375, 200))


class Enemies:
    def __init__(self, screen):
        dimensions = [28, 45]
        self.shot = False
        self.down = False
        self.down1 = False
        self.down2 = False
        self.down3 = False
        self.down4 = False
        self.down5 = False
        self.down6 = False
        self.down7 = False
        self.down8 = False
        self.down9 = False
        self.down10 = False
        self.down11 = False
        self.down12 = False
        self.down13 = False
        self.down14 = False
        self.difference = 00
        self.direction = "right"
        if save.check_file("level"):
            self.level = save.load("level")
        else:
            self.level = 1

        self.screen = screen
        self.ship = pygame.image.load(resource_path("Alien.png"))
        self.ship1 = pygame.image.load(resource_path("Alien.png"))
        self.ship2 = pygame.image.load(resource_path("Alien.png"))
        self.ship3 = pygame.image.load(resource_path("Alien.png"))
        self.ship4 = pygame.image.load(resource_path("Alien.png"))
        self.ship5 = pygame.image.load(resource_path("Alien.png"))
        self.ship6 = pygame.image.load(resource_path("Alien.png"))
        self.ship7 = pygame.image.load(resource_path("Alien.png"))
        self.ship8 = pygame.image.load(resource_path("Alien.png"))
        self.ship9 = pygame.image.load(resource_path("Alien.png"))
        self.ship10 = pygame.image.load(resource_path("Alien.png"))
        self.ship11 = pygame.image.load(resource_path("Alien.png"))
        self.ship12 = pygame.image.load(resource_path("Alien.png"))
        self.ship13 = pygame.image.load(resource_path("Alien.png"))
        self.ship14 = pygame.image.load(resource_path("Alien.png"))
        self.horde = [self.ship, self.ship1, self.ship2, self.ship3, self.ship4, self.ship5, self.ship6, self.ship7, self.ship8, self.ship9, self.ship10, self.ship11, self.ship12, self.ship13, self.ship14]
        self.y = 20
        self.y1 = 20
        self.y2 = 20
        self.y3 = 20
        self.y4 = 20
        self.y5 = 20
        self.y6 = 50 + 30
        self.y7 = 20 + 110
        self.y8 = 20 + 110
        self.y9 = 20
        self.y10 = 50 + 30
        self.y11 = 80 + 50
        self.y12 = 80 + 50
        self.y13 = 20
        self.y14 = 20
        self.x = 200 + 50
        self.x1 = 255 + 50
        self.x2 = 310 + 50
        self.x3 = 365 + 50
        self.x4 = 420 + 50
        self.x5 = 475 + 50
        self.x6 = 50 + 200
        self.x7 = 50 + 310
        self.x8 = 50 + 365
        self.x9 = -400000000000000
        self.x10 = 475 + 50
        self.x11 = 250
        self.x12 = 525
        self.x13 = -400000000000
        self.x14 = 50
        self.laserx = 200 + 50 + 27.5
        self.laserx1 = 255 + 50 + 27.5
        self.laserx2 = 310 + 50 + 27.5
        self.laserx3 = 365 + 50 + 27.5
        self.laserx4 = 420 + 50 + 27.5
        self.laserx5 = 475 + 50 + 27.5
        self.laserx6 = 50 + 200 + 27.5
        self.laserx7 = 50 + 310 + 27.5
        self.laserx8 = 50 + 365 + 27.5
        self.laserx9 = - 400000000
        self.laserx10 = 475 + 50 + 27.5
        self.laserx11 = 250 + 27.5
        self.laserx12 = 525 + 27.5
        self.laserx13 = 50 + 27.5
        self.laserx14 = 50 + 27.5
        self.horde_y = [self.y, self.y1, self.y2, self.y3, self.y4 , self.y5, self.y6 , self.y7 ,self.y8, self.y9, self.y10,self.y11, self.y12, self.y13, self.y14]
        self.horde_x = [self.x, self.x1, self.x2, self.x3, self.x4, self.x5, self.x6, self.x7, self.x8, self.x9,self.x10, self.x11, self.x12, self.x13, self.x14]
        self.status = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        if self.level == 1:
            if self.horde_x[0] <= -3000:
                self.status[0] = False
            if self.horde_x[1] <= -3000:
                        self.status[1] = False
            if self.horde_x[2] <= -3000:
                        self.status[2] = False
            if self.horde_x[3] <= -3000:
                        self.status[3] = False
            if self.horde_x[4] <= -3000:
                        self.status[4] = False
            if self.horde_x[5] <= -3000:
                        self.status[5] = False
            if self.horde_x[6] <= -3000:
                        self.status[6] = False
            if self.horde_x[7] <= -3000:
                        self.status[7] = False
            if self.horde_x[8] <= -3000:
                        self.status[8] = False
            if self.horde_x[9] <= -3000:
                        self.status[9] = False
            if self.horde_x[10] <= -3000:
                        self.status[10] = False
            if self.horde_x[11] <= -3000:
                        self.status[11] = False
            if self.horde_x[12] <= -3000:
                        self.status[12] = False
            if self.horde_x[13] <= -3000:
                        self.status[13] = False



        if self.level == 2:  
            if 1 == 1:
                self.horde_x[0] = 150
                self.horde_x[1] = 150
                self.horde_x[2] = 150
                self.horde_x[3] = 205
                self.horde_x[4] = 205
                self.horde_x[5] = 260
                self.horde_x[6] = 260
                self.horde_x[7] = 260 + 535
                self.horde_x[8] = 260 + 535
                self.horde_x[9] = 260 + 535
                self.horde_x[10] = 205 + 535
                self.horde_x[11] = 205 + 535
                self.horde_x[12] = 150 + 535
                self.horde_x[13] = 150 + 535
                self.horde_y[0] = 20
                self.horde_y[1] = 80
                self.horde_y[2] = 130
                self.horde_y[3] = 20
                self.horde_y[4] = 80
                self.horde_y[5] = 20
                self.horde_y[6] = 80
                self.horde_y[7] = 20
                self.horde_y[8] = 80
                self.horde_y[9] = 130
                self.horde_y[10] = 20
                self.horde_y[11] = 80
                self.horde_y[12] = 20
                self.horde_y[13] = 80
                self.status = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]  
                self.shot = False
                self.laserx = self.horde_x[0] + 22.5
                self.laserx1 = self.horde_x[1] + 22.5
                self.laserx2 = self.horde_x[2] + 22.5
                self.laserx3 = self.horde_x[3] + 22.5
                self.laserx4 = self.horde_x[4] + 22.5
                self.laserx5 = self.horde_x[5] + 22.5
                self.laserx6 = self.horde_x[6] + 22.5
                self.laserx7 = self.horde_x[7] + 22.5
                self.laserx8 = self.horde_x[8] + 22.5
                self.laserx9 = self.horde_x[9] + 22.5
                self.laserx10 = self.horde_x[10] + 22.5
                self.laserx11 = self.horde_x[11] + 22.5
                self.laserx12 = self.horde_x[12] + 22.5
                self.laserx13 = self.horde_x[13] + 22.5
        if self.level ==3:

                self.horde_x[0] = 100
                self.horde_x[1] = 800
                self.horde_x[2] = 150
                self.horde_x[3] = 205
                self.horde_x[4] = 260
                self.horde_x[5] = 745
                self.horde_x[6] = 690
                self.horde_x[13] = 635
                self.horde_x[7] = 335
                self.horde_x[8] = 390
                self.horde_x[9] = 250
                self.horde_x[10] = 320
                self.horde_x[11] = 390
                self.horde_x[12] = 460

                self.horde_y[0] = 20
                self.horde_y[1] = 20
                self.horde_y[2] = 300
                self.horde_y[3] = 300
                self.horde_y[4] = 300
                self.horde_y[5] = 300
                self.horde_y[6] = 300
                self.horde_y[7] = 215 - 40
                self.horde_y[8] = 215 - 40
                self.horde_y[9] = 250 - 40
                self.horde_y[10] = 250 - 40
                self.horde_y[11] = 250 - 40
                self.horde_y[12] = 250 - 40
                self.horde_y[13] = 300 
                self.status = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]  
                self.shot = False
                self.laserx = self.horde_x[0] + 22.5
                self.laserx1 = self.horde_x[1] + 22.5
                self.laserx2 = self.horde_x[2] + 22.5
                self.laserx3 = self.horde_x[3] + 22.5
                self.laserx4 = self.horde_x[4] + 22.5
                self.laserx5 = self.horde_x[5] + 22.5
                self.laserx6 = self.horde_x[6] + 22.5
                self.laserx7 = self.horde_x[7] + 22.5
                self.laserx8 = self.horde_x[8] + 22.5
                self.laserx9 = self.horde_x[9] + 22.5
                self.laserx10 = self.horde_x[10] + 22.5
                self.laserx11 = self.horde_x[11] + 22.5
                self.laserx12 = self.horde_x[12] + 22.5
                self.laserx13 = self.horde_x[13] + 22.5
            




    def ship_placement(self, ship, x, y):
        self.screen.blit(ship, (x, y))


    def platform_placement(self, x1, y1, x_extension, y_extension):
        pygame.draw.rect(self.screen, (200, 200, 200), [x1, y1, x_extension, y_extension])
    def green_platform_placement(self, x1, y1, x_extension, y_extension):
        pygame.draw.rect(self.screen, (0, 150, 0), [x1, y1, x_extension, y_extension])
    def portal_placement(self, color, x1, y1, x_extension, y_extension):
        pygame.draw.rect(self.screen, color , [x1, y1, x_extension, y_extension])
    

    def level1(self):


        if self.level == 1:

            if self.horde_y[0] > -50:
                self.ship_placement(self.horde[0], self.horde_x[0], self.horde_y[0])
            if self.horde_y[1] > -50:
                self.ship_placement(self.horde[1], self.horde_x[1], self.horde_y[1])
            if self.horde_y[2] > -50:
                self.ship_placement(self.horde[2], self.horde_x[2], self.horde_y[2])
            if self.horde_y[3] > -50:
                self.ship_placement(self.horde[3], self.horde_x[3], self.horde_y[3])
            if self.horde_y[4] > -50:
                self.ship_placement(self.horde[4], self.horde_x[4], self.horde_y[4])
            if self.horde_y[5] > -50:
                self.ship_placement(self.horde[5], self.horde_x[5], self.horde_y[5])
            if self.horde_y[6] > -50:
                self.ship_placement(self.horde[6], self.horde_x[6], self.horde_y[6])
            if self.horde_y[7] > -50:
                self.ship_placement(self.horde[7], self.horde_x[7], self.horde_y[7])
            if self.horde_y[8] > -50:
                self.ship_placement(self.horde[8], self.horde_x[8], self.horde_y[8])
            if self.horde_y[10] > -50:
                self.ship_placement(self.horde[10], self.horde_x[10], self.horde_y[10])
            if self.horde_y[11] > -50:
                self.ship_placement(self.horde[11], self.horde_x[11], self.horde_y[11])
            if self.horde_y[12] > -50:
                self.ship_placement(self.horde[12], self.horde_x[12], self.horde_y[12])
            self.platform_placement(200, 300, 90, 5)
            self.platform_placement(650, 300, 90, 5)
            pygame.display.update()
        if self.level == 1.5:
            green = (0, 255, 0)
            self.screen.fill((0,0,0))
            font1 = pygame.font.SysFont("Typeface Mario World Pixel Filled", 100, bold=False, italic=False)
            line = font1.render("Success", False, (0, 255, 0))
            self.screen.blit(line, (300, 50))
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 310 <= mouse_x <= 610 and 235 <= mouse_y <= 315:
                green = (173,216, 230)
                if pygame.mouse.get_rel():
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        Game().reset()
                        self.level = 2
                        Game().reset()
                        

            font2 = pygame.font.SysFont("Typeface Mario World Pixel Filled", 75, bold=False, italic=False)
            line2 = font2.render("Continue?", False, (0, 255, 0))
            self.screen.blit(line2, (350 - 20, 50 + 200))
            pygame.draw.rect(self.screen, green, [330 - 20, 35 + 200, 300, 80], 1, 5)
        if self.level == 2.5:
            green = (0, 255, 0)
            self.screen.fill((0,0,0))
            font1 = pygame.font.SysFont("Typeface Mario World Pixel Filled", 100, bold=False, italic=False)
            line = font1.render("Success", False, (0, 255, 0))
            self.screen.blit(line, (300, 50))
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 310 <= mouse_x <= 610 and 235 <= mouse_y <= 315:
                green = (173,216, 230)
                if pygame.mouse.get_rel():
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        Game().reset()
                        self.level = 3
                        Game.reset()
            font2 = pygame.font.SysFont("Typeface Mario World Pixel Filled", 75, bold=False, italic=False)
            line2 = font2.render("Continue?", False, (0, 255, 0))
            self.screen.blit(line2, (350 - 20, 50 + 200))
            pygame.draw.rect(self.screen, green, [330 - 20, 35 + 200, 300, 80], 1, 5)

            pygame.display.update()
        
        if self.level == 2:
            
            if self.horde_y[0] > -50:
                self.ship_placement(red, self.horde_x[0], self.horde_y[0])
            if self.horde_y[1] > -50:
                self.ship_placement(red, self.horde_x[1], self.horde_y[1])
            if self.horde_y[2] > -50:
                self.ship_placement(self.horde[9], self.horde_x[2], self.horde_y[2])
            if self.horde_y[3] > -50:
                self.ship_placement(self.horde[3], self.horde_x[3], self.horde_y[3])
            if self.horde_y[4] > -50:
                self.ship_placement(self.horde[4], self.horde_x[4], self.horde_y[4])
            if self.horde_y[5] > -50:
                self.ship_placement(self.horde[5], self.horde_x[5], self.horde_y[5])
            if self.horde_y[6] > -50:
                self.ship_placement(self.horde[6], self.horde_x[6], self.horde_y[6])
            if self.horde_y[7] > -50:
                self.ship_placement(red, self.horde_x[7], self.horde_y[7])
            if self.horde_y[8] > -50:
                self.ship_placement(red, self.horde_x[8], self.horde_y[8])
            if self.horde_y[9] > -50:
                self.ship_placement(self.horde[9], self.horde_x[9], self.horde_y[9])
            if self.horde_y[10] > -50:
                self.ship_placement(self.horde[10], self.horde_x[10], self.horde_y[10])
            if self.horde_y[11] > -50:
                self.ship_placement(self.horde[11], self.horde_x[11], self.horde_y[11])
            if self.horde_y[12] > -50:
                self.ship_placement(self.horde[12], self.horde_x[12], self.horde_y[12])
            if self.horde_y[13] > -50:
                self.ship_placement(self.horde[13], self.horde_x[13], self.horde_y[13])
            self.green_platform_placement(100, 250, 150, 5)
            self.platform_placement(550, 250, 120, 5)
        if self.level ==3:

                if self.horde_y[0] > -50:
                    self.ship_placement(red, self.horde_x[0], self.horde_y[0])
                if self.horde_y[1] > -50:
                    self.ship_placement(red, self.horde_x[1], self.horde_y[1])
                if self.horde_y[2] > -50:
                    self.ship_placement(self.horde[9], self.horde_x[2], self.horde_y[2])
                if self.horde_y[3] > -50:
                    self.ship_placement(self.horde[3], self.horde_x[3], self.horde_y[3])
                if self.horde_y[4] > -50:
                    self.ship_placement(self.horde[4], self.horde_x[4], self.horde_y[4])
                if self.horde_y[5] > -50:
                    self.ship_placement(self.horde[5], self.horde_x[5], self.horde_y[5])
                if self.horde_y[6] > -50:
                    self.ship_placement(self.horde[6], self.horde_x[6], self.horde_y[6])
                if self.horde_y[7] > -50:
                    self.ship_placement(red, self.horde_x[7], self.horde_y[7])
                if self.horde_y[8] > -50:
                    self.ship_placement(red, self.horde_x[8], self.horde_y[8])
                if self.horde_y[9] > -50:
                    self.ship_placement(self.horde[9], self.horde_x[9], self.horde_y[9])
                if self.horde_y[10] > -50:
                    self.ship_placement(self.horde[10], self.horde_x[10], self.horde_y[10])
                if self.horde_y[11] > -50:
                    self.ship_placement(self.horde[11], self.horde_x[11], self.horde_y[11])
                if self.horde_y[12] > -50:
                    self.ship_placement(self.horde[12], self.horde_x[12], self.horde_y[12])
                if self.horde_y[13] > -50:
                    self.ship_placement(self.horde[13], self.horde_x[13], self.horde_y[13])
                self.green_platform_placement(0, 150, 200, 5)
                self.green_platform_placement(700, 150, 200, 5)
                self.portal_placement( (0,191,255),660, 280, 60, 5,)
                self.portal_placement( (0,191,255),770, 100, 60, 5,)
                self.portal_placement( (0,0,139),220, 280, 60, 5,)
                self.portal_placement( (0,0,139),110, 100, 60, 5,)
            


class Game:
    def __init__(self):
        self.h0 = 3
        self.h1 = 3
        self.h7 = 3
        self.h8 = 3
        self.count = 0
        self.state = "none"
        self.background = pygame.image.load(resource_path("Background.png"))
        pygame.mixer.music.load(resource_path("Music.mp3"))
        pygame.mixer.music.set_volume(0.35)
        pygame.mixer.music.play(-1)
        self.col = False
        self.direction = "right"
        self.direction1 = "right"
        self.direction2 = "right"
        self.direction3 = "right"
        self.blastssss = pygame.image.load(resource_path("red laser.png"))
        self.blast = pygame.transform.rotate(self.blastssss, 270)
        self.explosion = False
        self.backup = 0
        self.up = False
        self.screen_x = 900
        self.screen_y = 600
        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
        self.player = Player(self.screen_x/2 - 40, self.screen_y - 80, self.screen)
        self.projectile = Projectile(self.screen, self.player.y - 35)
        self.enemies = Enemies(self.screen)
        self.laser_y = self.enemies.horde_y[0] + 30
        self.laser_y1 = self.enemies.horde_y[1] + 30
        self.laser_y2 = self.enemies.horde_y[2] + 30
        self.laser_y3 = self.enemies.horde_y[3] + 30
        self.laser_y4 = self.enemies.horde_y[4] + 30
        self.laser_y5 = self.enemies.horde_y[5] + 30
        self.laser_y6 = self.enemies.horde_y[6] + 30
        self.laser_y7 = self.enemies.horde_y[7]+ 30
        self.laser_y8 = self.enemies.horde_y[8]+ 30
        self.laser_y9 = self.enemies.horde_y[9] + 30
        self.laser_y10 = self.enemies.horde_y[10]+ 30
        self.laser_y11 = self.enemies.horde_y[11]+ 30
        self.laser_y12 = self.enemies.horde_y[12]+ 30
        self.laser_y13 = self.enemies.horde_y[13]+ 30
    def alien_laser_collision(self, x1, y1, x2, y2):
            if x2 - 20 <= x1 <= x2 + 40:
                if y1 - 20 <= y2 <= y1 + 20:
                    return True
            return False




    def red_laser_collision(self, x1, y1, x2, y2):
            if x1 -5 <= x2 <= x1 + 70:
                if y1 - 5 <= y2 <= y1 + 28:
                    return True
            return False
    def red_white_collision(self, x1, y1, x2, y2, extension):
        if x1 - 25 <= x2 <=  x1 + extension:
            if y1  <= y2 <= y1 + 5:
                return True
        return False
    def blue_light_collision(self, x1, y1, x2, y2, extension):
        if x1 - 25 <= x2 <=  x1 + extension:
            if y1  <= y2 <= y1 + 5:
                return True
        return False


    def title(self):
        title = True
        while title:
 
             green = (0, 255, 0)
             color = (0, 255, 0)
             font1 = pygame.font.SysFont("Typeface Mario World Pixel Filled", 100, bold=False, italic=False)
             line = font1.render("Space Invaders", False, (0, 255, 0))
             line1 = font1.render("New Game", False, (green))
             line2 = font1.render("Continue", False, (green))
             red = pygame.image.load(resource_path("title1.jpg"))
             mouse_x, mouse_y = pygame.mouse.get_pos()

 
             if 250 <= mouse_x <= 250 + 400 and 280 <= mouse_y <= 430 - 50:
                 green = (173, 216, 230)
                 if pygame.mouse.get_pressed() != (0,0,0):
                    if save.check_file("level"):
                        save.del_save("level")
                        self.enemies.level = 1
                        self.reset()
                    title = False
             else:
                 green = (0, 255, 0)
            
             if save.check_file("level"):
                if 280 <= mouse_x <= 280 + 350 and 400 <= mouse_y <= 500:
                    color= (173, 216, 230)
                    if pygame.mouse.get_pressed() != (0,0,0):
                        title = False
                pygame.draw.rect(self.screen, color, [280, 400, 350, 100], 5, 10)
                self.screen.blit(line2, (300, 420))



             pygame.draw.rect(self.screen, green, [250, 280, 400, 100], 5, 10)

             self.screen.blit(line1, (270, 300))

             self.screen.blit(line, (200, 50))
             self.screen.blit(red, (350, 150))

             for event in pygame.event.get():
                 if event.type == QUIT:
                     if self.enemies.level != 1:
                        if self.enemies.level == 1.5 or self.enemies.level == 2.5:
                            self.enemies.level += 0.5
                        save.save_game(self.enemies.level, "level")
                     pygame.quit()
                     sys.exit()


             pygame.display.update()

    def reset(self):
        self.enemies.shot = False
        self.direction = "right"
        if self.enemies.level == 1:
            self.laser_y = 625
            self.laser_y1 = 625
            self.laser_y2 = 625
            self.laser_y3 = 625
            self.laser_y4 = 625
            self.laser_y5 = 625
            self.laser_y6 = 625
            self.laser_y7 = 625
            self.laser_y8 = 625
            self.laser_y10 = 625
            self.laser_y11 = 625
            self.laser_y12 = 625
            self.enemies.horde_y[0] = 20
            self.enemies.horde_y[1] = 20
            self.enemies.horde_y[2] = 20
            self.enemies.horde_y[3] = 20
            self.enemies.horde_y[4] = 20
            self.enemies.horde_y[5] = 20
            self.enemies.horde_y[6] = 50 + 30
            self.enemies.horde_y[7] = 20 + 110
            self.enemies.horde_y[8] = 20 + 110

            self.enemies.horde_y[10] = 50 + 30
            self.enemies.horde_y[11] = 80 + 50
            self.enemies.horde_y[12] = 80 + 50
            self.enemies.horde_y[13] = 20
            self.enemies.horde_y[14] = 20
            self.enemies.horde_x[0] = 200 + 50
            self.enemies.horde_x[1] = 255 + 50
            self.enemies.horde_x[2] = 310 + 50
            self.enemies.horde_x[3] = 365 + 50
            self.enemies.horde_x[4] = 420 + 50
            self.enemies.horde_x[5] = 475 + 50
            self.enemies.horde_x[6] = 50 + 200
            self.enemies.horde_x[7] = 50 + 310
            self.enemies.horde_x[8] = 50 + 365

            self.enemies.horde_x[10] = 475 + 50
            self.enemies.horde_x[11] = 250
            self.enemies.horde_x[12] = 525

            self.enemies.horde_x[14] = 50
            self.enemies.laserx = 200 + 50 + 27.5
            self.enemies.laserx1 = 255 + 50 + 27.5
            self.enemies.laserx2 = 310 + 50 + 27.5
            self.enemies.laserx3 = 365 + 50 + 27.5
            self.enemies.laserx4 = 420 + 50 + 27.5
            self.enemies.laserx5 = 475 + 50 + 27.5
            self.enemies.laserx6 = 50 + 200 + 27.5
            self.enemies.laserx7 = 50 + 310 + 27.5
            self.enemies.laserx8 = 50 + 365 + 27.5

            self.enemies.laserx10 = 475 + 50 + 27.5
            self.enemies.laserx11 = 250 + 27.5
            self.enemies.laserx12 = 525 + 27.5
            self.enemies.laserx13 = 50 + 27.5
            self.enemies.laserx14 = 50 + 27.5
            self.status = [True, True, True, True, True, True, True, True, True, False, True, True, True, False, True]  
        if 1.5 <= self.enemies.level <= 2:  
            self.status = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]  
            self.shot = False
            self.enemies.laserx = self.enemies.horde_x[0] + 22.5
            self.enemies.laserx1 = self.enemies.horde_x[1] + 22.5
            self.enemies.laserx2 = self.enemies.horde_x[2] + 22.5
            self.enemies.laserx3 = self.enemies.horde_x[3] + 22.5
            self.enemies.laserx4 = self.enemies.horde_x[4] + 22.5
            self.enemies.laserx5 = self.enemies.horde_x[5] + 22.5
            self.enemies.laserx6 = self.enemies.horde_x[6] + 22.5
            self.enemies.laserx7 = self.enemies.horde_x[7] + 22.5
            self.enemies.laserx8 = self.enemies.horde_x[8] + 22.5
            self.enemies.laserx9 = self.enemies.horde_x[9] + 22.5
            self.enemies.laserx10 = self.enemies.horde_x[10] + 22.5
            self.enemies.laserx11 = self.enemies.horde_x[11] + 22.5
            self.enemies.laserx12 = self.enemies.horde_x[12] + 22.5
            self.enemies.laserx13 = self.enemies.horde_x[13] + 22.5

            self.enemies.horde_x[0] = 150
            self.enemies.horde_x[1] = 150
            self.enemies.horde_x[2] = 150
            self.enemies.horde_x[3] = 205
            self.enemies.horde_x[4] = 205
            self.enemies.horde_x[5] = 260
            self.enemies.horde_x[6] = 260
            self.enemies.horde_x[7] = 260 + 535
            self.enemies.horde_x[8] = 260 + 535
            self.enemies.horde_x[9] = 260 + 535
            self.enemies.horde_x[10] = 205 + 535
            self.enemies.horde_x[11] = 205 + 535
            self.enemies.horde_x[12] = 150 + 535
            self.enemies.horde_x[13] = 150 + 535
            self.enemies.horde_y[0] = 20
            self.enemies.horde_y[1] = 80
            self.enemies.horde_y[2] = 130
            self.enemies.horde_y[3] = 20
            self.enemies.horde_y[4] = 80
            self.enemies.horde_y[5] = 20
            self.enemies.horde_y[6] = 80
            self.enemies.horde_y[7] = 20
            self.enemies.horde_y[8] = 80
            self.enemies.horde_y[9] = 130
            self.enemies.horde_y[10] = 20
            self.enemies.horde_y[11] = 80
            self.enemies.horde_y[12] = 20
            self.enemies.horde_y[13] = 80
            self.laser_y = 625
            self.laser_y1 = 625
            self.laser_y2 = 625
            self.laser_y3 = 625
            self.laser_y4 = 625
            self.laser_y5 = 625
            self.laser_y6 = 625
            self.laser_y7 = 625
            self.laser_y8 = 625
            self.laser_y9 = 625
            self.laser_y10 = 625
            self.laser_y11 = 625
            self.laser_y12 = 625
            self.laser_y13 = 625
            self.h0 = 3
            self.h1 = 3
            self.h7 = 3
            self.h8 = 3
        if 2.5  <= self.enemies.level <= 3:
                self.enemies.horde_x[0] = 100
                self.enemies.horde_x[1] = 800
                self.enemies.horde_x[2] = 150
                self.enemies.horde_x[3] = 205
                self.enemies.horde_x[4] = 260
                self.enemies.horde_x[5] = 745
                self.enemies.horde_x[6] = 690
                self.enemies.horde_x[13] = 635
                self.enemies.horde_x[7] = 335
                self.enemies.horde_x[8] = 390
                self.enemies.horde_x[9] = 250
                self.enemies.horde_x[10] = 320
                self.enemies.horde_x[11] = 390
                self.enemies.horde_x[12] = 460

                self.enemies.horde_y[0] = 20
                self.enemies.horde_y[1] = 20
                self.enemies.horde_y[2] = 300
                self.enemies.horde_y[3] = 300
                self.enemies.horde_y[4] = 300
                self.enemies.horde_y[5] = 300
                self.enemies.horde_y[6] = 300
                self.enemies.horde_y[7] = 215 - 40
                self.enemies.horde_y[8] = 215 - 40
                self.enemies.horde_y[9] = 250 - 40
                self.enemies.horde_y[10] = 250 - 40
                self.enemies.horde_y[11] = 250 - 40
                self.enemies.horde_y[12] = 250 - 40
                self.enemies.horde_y[13] = 300 
                self.status = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]  
                self.shot = False
                self.enemies.laserx = self.enemies.horde_x[0] + 22.5
                self.enemies.laserx1 = self.enemies.horde_x[1] + 22.5
                self.enemies.laserx2 = self.enemies.horde_x[2] + 22.5
                self.enemies.laserx3 = self.enemies.horde_x[3] + 22.5
                self.enemies.laserx4 = self.enemies.horde_x[4] + 22.5
                self.enemies.laserx5 = self.enemies.horde_x[5] + 22.5
                self.enemies.laserx6 = self.enemies.horde_x[6] + 22.5
                self.enemies.laserx7 = self.enemies.horde_x[7] + 22.5
                self.enemies.laserx8 = self.enemies.horde_x[8] + 22.5
                self.enemies.laserx9 = self.enemies.horde_x[9] + 22.5
                self.enemies.laserx10 = self.enemies.horde_x[10] + 22.5
                self.enemies.laserx11 = self.enemies.horde_x[11] + 22.5
                self.enemies.laserx12 = self.enemies.horde_x[12] + 22.5
                self.enemies.laserx13 = self.enemies.horde_x[13] + 22.5
                self.laser_y = 625
                self.laser_y1 = 625
                self.laser_y2 = 625
                self.laser_y3 = 625
                self.laser_y4 = 625
                self.laser_y5 = 625
                self.laser_y6 = 625
                self.laser_y7 = 625
                self.laser_y8 = 625
                self.laser_y9 = 625
                self.laser_y10 = 625
                self.laser_y11 = 625
                self.laser_y12 = 625
                self.laser_y13 = 625
            
            
        self.player.x = 435
        self.projectile.ys[self.projectile.num] = -25
        pygame.mixer.music.play(-1)

        self.enemies.status = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        self.count = 0


    def play(self):
        self.player.draw_shooter()
        self.player.draw_health()
        #Enemy shooting for all levels
        if self.enemies.shot:
            a = random.randint(1, 100)
            l = 100
            if a ==2:


                if self.enemies.laserx - l <= self.player.x <= self.enemies.laserx + l:
                    self.enemies.down = True

            if self.enemies.down:
                if self.laser_y == self.enemies.horde_y[0] + 30:
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y >= 625:

                    self.enemies.down = False

            if a ==1:
                if self.enemies.laserx1 - l <= self.player.x <= self.enemies.laserx1 + l:
                        self.enemies.down1 = True

            if self.enemies.down1:
                if self.laser_y1 == self.enemies.horde_y[1] + 30:
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y1 >= 625:

                    self.enemies.down1 = False
            if a ==3:

                if self.enemies.laserx2 - l <= self.player.x <= self.enemies.laserx2 + l:

                    self.enemies.down2 = True
            if self.enemies.down2:
                if self.laser_y2 == self.enemies.horde_y[2] + 30:
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y2 >= 625:

                    self.enemies.down2 = False
            if a ==4:

                if self.enemies.laserx3 - l <= self.player.x <= self.enemies.laserx3 + l:
                    self.enemies.down3 = True

            if self.enemies.down3:
                if self.laser_y3 == self.enemies.horde_y[3] + 30:

                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y3 >= 625:

                    self.enemies.down3 = False
            if a ==5:

                if self.enemies.laserx4 - l <= self.player.x <= self.enemies.laserx4 + l:
                        self.enemies.down4 = True

            if self.enemies.down4:
                if self.laser_y4 == self.enemies.horde_y[4] + 30:

                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y4 >= 625:

                    self.enemies.down4 = False
            if a ==6:

                if self.enemies.laserx5 - l <= self.player.x <= self.enemies.laserx5 + l:
                        self.enemies.down5 = True


            if self.enemies.down5:
                if self.laser_y5 == self.enemies.horde_y[5] + 30:

                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y5 >= 625:

                    self.enemies.down5 = False
            if a ==7:

                if self.enemies.laserx6 - l <= self.player.x <= self.enemies.laserx6 + l:
                        self.enemies.down6 = True


            if self.enemies.down6:
                if self.laser_y6 == self.enemies.horde_y[6] + 30:

                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y6 >= 625:

                    self.enemies.down6 = False
            if a ==8:

                if self.enemies.laserx7 - l <= self.player.x <= self.enemies.laserx7 + l:
                        self.enemies.down7 = True
            if self.enemies.down7:
                if self.laser_y7 == self.enemies.horde_y[7] + 30:

                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y7 >= 625:

                    self.enemies.down7 = False
            if a ==9:

                if self.enemies.laserx8 -l <= self.player.x <= self.enemies.laserx8 + l:
                        self.enemies.down8 = True

            if self.enemies.down8:
                if self.laser_y8 == self.enemies.horde_y[8] + 30:

                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y8 >= 625:
                    self.enemies.down8 = False
            if a ==10:

                if self.enemies.laserx10 - l <= self.player.x <= self.enemies.laserx10 + l:
                        self.enemies.down10 = True

            if self.enemies.down10:
                if self.laser_y10 == self.enemies.horde_y[10] + 30:

                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y10 >= 625:

                    self.enemies.down10 = False
            if a ==11:

                if self.enemies.laserx11 - l <= self.player.x <= self.enemies.laserx11 + l:
                        self.enemies.down11 = True

            if self.enemies.down11:
                if self.laser_y11 == self.enemies.horde_y[11] + 30:

                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y11 >= 625:

                    self.enemies.down11 = False
            if a ==12:

                if self.enemies.laserx12 - l <= self.player.x <= self.enemies.laserx12 + l:
                        self.enemies.down12 = True

            if self.enemies.down12:
                if self.laser_y12 == self.enemies.horde_y[12] + 30:

                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y12 >= 625:

                    self.enemies.down12 = False

            if a == 13:

                if self.enemies.laserx13 - l <= self.player.x <= self.enemies.laserx13 + l:
                    self.enemies.down13 = True

            if self.enemies.down13:
                if self.laser_y13 == self.enemies.horde_y[13] + 30:

                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y13 >= 625:
                    self.enemies.down13 = False

            if a == 14:

                if self.enemies.laserx9 - l <= self.player.x <= self.enemies.laserx9 + l:
                    self.enemies.down9 = True

            if self.enemies.down9:
                if self.laser_y9 == self.enemies.horde_y[9] + 30:

                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("enemy laser.wav")))
                if self.laser_y9 >= 625:
                    self.enemies.down9 = False


            if self.enemies.down:
                self.screen.blit(self.blast, (self.enemies.laserx, self.laser_y))
            if not self.enemies.down:
                self.laser_y = self.enemies.horde_y[0] + 30
                self.enemies.laserx = self.enemies.horde_x[0] + 22.5


            if self.enemies.down1:
                self.screen.blit(self.blast, (self.enemies.laserx1, self.laser_y1))
            if not self.enemies.down1:
                self.laser_y1 = self.enemies.horde_y[1] + 30
                self.enemies.laserx1 = self.enemies.horde_x[1] + 22.5


            if self.enemies.down2:
                self.screen.blit(self.blast, (self.enemies.laserx2, self.laser_y2))
            if not self.enemies.down2:
                self.laser_y2 = self.enemies.horde_y[2] + 30
                self.enemies.laserx2 = self.enemies.horde_x[2] + 22.5

            if self.enemies.down3:
                self.screen.blit(self.blast, (self.enemies.laserx3, self.laser_y3))
            if not self.enemies.down3:
                self.laser_y3 = self.enemies.horde_y[3] + 30
                self.enemies.laserx3 = self.enemies.horde_x[3] + 22.5


            if self.enemies.down4:
                self.screen.blit(self.blast, (self.enemies.laserx4, self.laser_y4))
            if not self.enemies.down4:
                self.laser_y4 = self.enemies.horde_y[4] + 30
                self.enemies.laserx4 = self.enemies.horde_x[4] + 22.5

            if self.enemies.down5:
                self.screen.blit(self.blast, (self.enemies.laserx5, self.laser_y5))
            if not self.enemies.down5:
                self.laser_y5 = self.enemies.horde_y[5] + 30
                self.enemies.laserx5 = self.enemies.horde_x[5] + 22.5

            if self.enemies.down6:
                self.screen.blit(self.blast, (self.enemies.laserx6, self.laser_y6))
            if not self.enemies.down6:
                self.laser_y6 = self.enemies.horde_y[6] + 30
                self.enemies.laserx6 = self.enemies.horde_x[6] + 22.5

            if self.enemies.down7:
                self.screen.blit(self.blast, (self.enemies.laserx7, self.laser_y7))
            if not self.enemies.down7:
                self.laser_y7 = self.enemies.horde_y[7] + 30
                self.enemies.laserx7 = self.enemies.horde_x[7] + 22.5

            if self.enemies.down8:
                self.screen.blit(self.blast, (self.enemies.laserx8, self.laser_y8))
            if not self.enemies.down8:
                self.laser_y8 = self.enemies.horde_y[8] + 30
                self.enemies.laserx8 = self.enemies.horde_x[8] + 22.5

            if self.enemies.down10:
                self.screen.blit(self.blast, (self.enemies.laserx10, self.laser_y10))
            if not self.enemies.down10:
                self.laser_y10 = self.enemies.horde_y[10] + 30
                self.enemies.laserx10 = self.enemies.horde_x[10] + 22.5

            if self.enemies.down11:
                self.screen.blit(self.blast, (self.enemies.laserx11, self.laser_y11))
            if not self.enemies.down11:
                self.laser_y11 = self.enemies.horde_y[11] + 30
                self.enemies.laserx11 = self.enemies.horde_x[11] + 22.5

            if self.enemies.down12:
                self.screen.blit(self.blast, (self.enemies.laserx12, self.laser_y12))
            if not self.enemies.down12:
                self.laser_y12 = self.enemies.horde_y[12] + 30
                self.enemies.laserx12 = self.enemies.horde_x[12] + 22.5
            if self.enemies.level != 1:

                if self.enemies.down13:
                    self.screen.blit(self.blast, (self.enemies.laserx13, self.laser_y13))
                if not self.enemies.down13:
                    self.laser_y13 = self.enemies.horde_y[13] + 30
                    self.enemies.laserx13 = self.enemies.horde_x[13] + 22.5
            if self.enemies.level != 1:
                if self.enemies.down9:
                    self.screen.blit(self.blast, (self.enemies.laserx9, self.laser_y9))
                if not self.enemies.down9:
                    self.laser_y9 = self.enemies.horde_y[9] + 30
                    self.enemies.laserx9 = self.enemies.horde_x[9] + 22.5


        if self.up:
            self.projectile.draw_projectile()


            if self.projectile.ys[self.projectile.num] > -25:
                self.projectile.ys[self.projectile.num] -= 2.2
        if self.projectile.num >= 9:
            self.projectile.num = 0
        self.enemies.level1()
        if self.projectile.ys[self.projectile.num] <= -25:
            self.up = False
            #self.projectile.four += self.backup
            if self.projectile.num < self.projectile.num + 1:
                self.projectile.num += 1
                self.projectile.ys[self.projectile.num - 1] = 520

        self.enemies.level1()
        if self.player.health == 0:
            raise GameOver
        #Level 1 enemy blast on player collision
        if 1 == 1:
                if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx, self.laser_y):
                    self.player.health -= 1
                    self.col = False
                    self.laser_y = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))

                if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx1, self.laser_y1):
                    self.player.health -= 1
                    self.col = False
                    self.laser_y1 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))

                if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx2, self.laser_y2):
                    self.player.health -= 1
                    self.col = False
                    self.laser_y2 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))

                if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx3, self.laser_y3):
                    self.player.health -= 1
                    self.col = False
                    self.laser_y3 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))

                if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx4, self.laser_y4):
                    self.player.health -= 1
                    self.col = False
                    self.laser_y4 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))

                if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx5, self.laser_y5):
                    self.player.health -= 1
                    self.col = False
                    self.laser_y5 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))

                if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx6, self.laser_y6):
                    self.player.health -= 1
                    self.col = False
                    self.laser_y6 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))

                if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx7, self.laser_y7):
                    self.player.health -= 1
                    self.col = False
                    self.laser_y7 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))

                if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx8, self.laser_y8):
                    self.player.health -= 1
                    self.col = False
                    self.laser_y8 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))

                if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx10, self.laser_y10):
                    self.player.health -= 1
                    self.col = False
                    self.laser_y10 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))

                if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx11, self.laser_y11):
                    self.player.health -= 1
                    self.col = False
                    self.laser_y11 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))

                if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx12, self.laser_y12):
                    self.player.health -= 1
                    self.col = False
                    self.laser_y12 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))


                

                pygame.display.update()


        if self.enemies.level == 1:

                #Enemy fire on barrier collision
                if self.red_white_collision(200, 300, self.enemies.laserx, self.laser_y, 90):
                    self.laser_y = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(200, 300, self.enemies.laserx1, self.laser_y1, 90):
                    self.laser_y1 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(200, 300, self.enemies.laserx2, self.laser_y2, 90):
                    self.laser_y2 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(200, 300, self.enemies.laserx3, self.laser_y3, 90):
                    self.laser_y3 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(200, 300, self.enemies.laserx4, self.laser_y4, 90):
                    self.laser_y4 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(200, 300, self.enemies.laserx5, self.laser_y5, 90):
                    self.laser_y5 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(200, 300, self.enemies.laserx6, self.laser_y6, 90):
                    self.laser_y6 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(200, 300, self.enemies.laserx7, self.laser_y7, 90):
                    self.laser_y7 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(200, 300, self.enemies.laserx8, self.laser_y8, 90):
                    self.laser_y8 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(200, 300, self.enemies.laserx10, self.laser_y10, 90):
                    self.laser_y10 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(200, 300, self.enemies.laserx11, self.laser_y11, 90):
                    self.laser_y11 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(200, 300, self.enemies.laserx12, self.laser_y12, 90):
                    self.laser_y12 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(650, 300, self.enemies.laserx, self.laser_y, 90):
                    self.laser_y = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound("Space invaders stuff/white barrier.wav"))
                if self.red_white_collision(650, 300, self.enemies.laserx1, self.laser_y1, 90):
                    self.laser_y1 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(650, 300, self.enemies.laserx2, self.laser_y2, 90):
                    self.laser_y2 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(650, 300, self.enemies.laserx3, self.laser_y3, 90):
                    self.laser_y3 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(650, 300, self.enemies.laserx4, self.laser_y4, 90):
                    self.laser_y4 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(650, 300, self.enemies.laserx5, self.laser_y5, 90):
                    self.laser_y5 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(650, 300, self.enemies.laserx6, self.laser_y6, 90):
                    self.laser_y6 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(650, 300, self.enemies.laserx7, self.laser_y7, 90):
                    self.laser_y7 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(650, 300, self.enemies.laserx8, self.laser_y8, 90):
                    self.laser_y8 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(650, 300, self.enemies.laserx10, self.laser_y10, 90):
                    self.laser_y10 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(650, 300, self.enemies.laserx11, self.laser_y11, 90):
                    self.laser_y11 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.red_white_collision(650, 300, self.enemies.laserx12, self.laser_y12, 90):
                    self.laser_y12 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))


                #Player fire on barrier collision
                if self.blue_light_collision(200, 300, 435 + self.projectile.difference, self.projectile.ys[self.projectile.num], 90):
                    self.projectile.ys[self.projectile.num] = -25
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.blue_light_collision(650, 300, 435 + self.projectile.difference, self.projectile.ys[self.projectile.num], 90):
                    self.projectile.ys[self.projectile.num] = -25
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))




        

                #Level 1 Player fire on enemy hitboxes
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num], self.enemies.horde_x[0], self.enemies.horde_y[0]):
                    self.enemies.horde_y[0] = -100
                    self.enemies.horde_x[0] = -3999
                    self.enemies.status[0] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num], self.enemies.horde_x[1], self.enemies.horde_y[1]):
                    self.enemies.horde_y[1] = -100
                    self.enemies.status[1] = False
                    self.enemies.horde_x[1] = -3999
                    pygame.mixer.Sound.play(explosion)
                    self.projectile.ys[self.projectile.num] = -26
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num], self.enemies.horde_x[2], self.enemies.horde_y[2]):
                    self.enemies.horde_y[2] = -100
                    self.enemies.status[2] = False
                    self.enemies.horde_x[2] = -3999
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num], self.enemies.horde_x[3], self.enemies.horde_y[3]):
                    self.enemies.horde_y[3] = -100
                    self.enemies.horde_x[3] = -4000
                    self.enemies.status[3] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num], self.enemies.horde_x[4], self.enemies.horde_y[4]):
                    self.enemies.horde_y[4] = -100
                    self.enemies.status[4] = False
                    self.enemies.horde_x[4] = -4000
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num], self.enemies.horde_x[5], self.enemies.horde_y[5]):
                    self.enemies.horde_y[5] = -100
                    self.enemies.horde_x[5] = -4000
                    self.enemies.status[5] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num], self.enemies.horde_x[6], self.enemies.horde_y[6]):
                    self.enemies.horde_y[6] = -100
                    self.enemies.horde_x[6] = -4000
                    self.enemies.status[6] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num], self.enemies.horde_x[7], self.enemies.horde_y[7]):
                    self.enemies.horde_x[7] = -4000
                    self.enemies.horde_y[7] = -100
                    self.enemies.status[7] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num], self.enemies.horde_x[8], self.enemies.horde_y[8]):
                    self.enemies.horde_x[8] = -4000
                    self.enemies.horde_y[8] = -100
                    self.enemies.status[8] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num], self.enemies.horde_x[10], self.enemies.horde_y[10]):
                    self.enemies.horde_x[10] = -4000
                    self.enemies.horde_y[10] = -100
                    self.enemies.status[10] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num], self.enemies.horde_x[11], self.enemies.horde_y[11]):
                    self.enemies.horde_x[11] = -4000
                    self.enemies.horde_y[11] = -100
                    self.enemies.status[11] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num], self.enemies.horde_x[12], self.enemies.horde_y[12]):
                    self.enemies.horde_x[12] = -4000
                    self.enemies.status[12] = False
                    self.projectile.ys[self.projectile.num] = -26
                    self.enemies.horde_y[12] = -100
                    pygame.mixer.Sound.play(explosion)
                value = False
                self.count = 0

                for f in [self.enemies.status[0], self.enemies.status[1], self.enemies.status[2], self.enemies.status[3], self.enemies.status[4], self.enemies.status[5], self.enemies.status[6], self.enemies.status[7], self.enemies.status[8], self.enemies.status[10], self.enemies.status[11], self.enemies.status[12]]:

                    if f == False:
                        self.count += 1



                if self.count == 12:
                    self.reset()
                    self.enemies.level += 0.5
                    self.reset()
                    self.count = 0
                    self.player.health = 5
        
        if self.enemies.level == 2:
            if self.red_white_collision(550, 250, self.enemies.laserx, self.laser_y, 120):
                    self.laser_y = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound("Space invaders stuff/white barrier.wav"))
            if self.red_white_collision(550, 250, self.enemies.laserx1, self.laser_y1, 120):
                    self.laser_y1 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

            if self.red_white_collision(550, 250, self.enemies.laserx2, self.laser_y2, 120):
                    self.laser_y2 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

            if self.red_white_collision(550, 250, self.enemies.laserx3, self.laser_y3, 120):
                    self.laser_y3 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

            if self.red_white_collision(550, 250, self.enemies.laserx4, self.laser_y4, 120):
                    self.laser_y4 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

            if self.red_white_collision(550, 250, self.enemies.laserx5, self.laser_y5, 120):
                    self.laser_y5 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

            if self.red_white_collision(550, 250, self.enemies.laserx6, self.laser_y6, 120):
                    self.laser_y6 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

            if self.red_white_collision(550, 250, self.enemies.laserx7, self.laser_y7, 120):
                    self.laser_y7 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))
                
            if self.red_white_collision(550, 250, self.enemies.laserx8, self.laser_y8, 120):
                    self.laser_y8 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))


            if self.red_white_collision(550, 250, self.enemies.laserx9, self.laser_y9, 120):
                    self.laser_y9 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

            if self.red_white_collision(550, 250, self.enemies.laserx10, self.laser_y10, 120):
                    self.laser_y10 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

            if self.red_white_collision(550, 250, self.enemies.laserx11, self.laser_y11, 120):
                    self.laser_y11 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

            if self.red_white_collision(550, 250, self.enemies.laserx12, self.laser_y12, 120):
                    self.laser_y12 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

            if self.red_white_collision(550, 250, self.enemies.laserx13, self.laser_y13, 120):
                    self.laser_y13 = 625
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))


            if self.blue_light_collision(100, 250, 435 + self.projectile.difference,self.projectile.ys[self.projectile.num], 150 ):
                self.projectile.ys[self.projectile.num] = -25
            if self.blue_light_collision(550, 250, 435 + self.projectile.difference,self.projectile.ys[self.projectile.num], 120): 
                self.projectile.ys[self.projectile.num] = -25
            if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx9, self.laser_y9):
                self.player.health -= 1
                self.col = False
                self.laser_y9 = 625
                pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))
            if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx13, self.laser_y13):
                self.player.health -= 1
                self.col = False
                self.laser_y13 = 625
                pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[0], self.enemies.horde_y[0]):
                if self.h0 == 1:
                    self.h0 -= 1
                    self.enemies.horde_y[0] = -100
                    self.enemies.horde_x[0] = -399900
                    self.enemies.status[0] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.h0 > 1:
                    self.h0 -= 1
                    self.projectile.ys[self.projectile.num] = -26

                    pygame.mixer.Sound.play(hurt)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[1], self.enemies.horde_y[1]):

                if self.h1 == 1:
                    self.h1 -= 1
                    self.enemies.horde_y[1] = -100
                    self.enemies.horde_x[1] = -399900
                    self.enemies.status[1] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.h1 > 1:
                    self.h1 -= 1
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(hurt)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[2], self.enemies.horde_y[2]):
                self.enemies.horde_y[2] = -100
                self.enemies.status[2] = False
                self.enemies.horde_x[2] = -399900
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[3], self.enemies.horde_y[3]):
                self.enemies.horde_y[3] = -100
                self.enemies.horde_x[3] = -400000
                self.enemies.status[3] = False
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[4], self.enemies.horde_y[4]):
                self.enemies.horde_y[4] = -100
                self.enemies.status[4] = False
                self.enemies.horde_x[4] = -400000
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[5], self.enemies.horde_y[5]):
                self.enemies.horde_y[5] = -100
                self.enemies.horde_x[5] = -400000
                self.enemies.status[5] = False
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[6], self.enemies.horde_y[6]):
                self.enemies.horde_y[6] = -100
                self.enemies.horde_x[6] = -400000
                self.enemies.status[6] = False
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[7], self.enemies.horde_y[7]):
                
                if self.h7 == 1:
                    self.h7 -= 1
                    self.enemies.horde_y[7] = -100
                    self.enemies.horde_x[7] = -399900
                    self.enemies.status[7] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.h7 > 1:
                    self.h7-= 1
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(hurt)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[8], self.enemies.horde_y[8]):
              
                if self.h8 == 1:
                    self.h8 -= 1
                    self.enemies.horde_y[8] = -100
                    self.enemies.horde_x[8] = -399900
                    self.enemies.status[8] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.h8 > 1:
                    self.h8 -= 1
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(hurt)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[9], self.enemies.horde_y[9]):
                self.enemies.horde_y[9] = -100
                self.enemies.horde_x[9] = -400000
                self.enemies.status[9] = False
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[10], self.enemies.horde_y[10]):
                self.enemies.horde_x[10] = -400000
                self.enemies.horde_y[10] = -100
                self.enemies.status[10] = False
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[11], self.enemies.horde_y[11]):
                self.enemies.horde_x[11] = -400000
                self.enemies.horde_y[11] = -100
                self.enemies.status[11] = False
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[12], self.enemies.horde_y[12]):
                self.enemies.horde_x[12] = -400000
                self.enemies.status[12] = False
                self.projectile.ys[self.projectile.num] = -26
                self.enemies.horde_y[12] = -100
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[13], self.enemies.horde_y[13]):
                self.enemies.horde_x[13] = -400000
                self.enemies.status[13] = False
                self.projectile.ys[self.projectile.num] = -26
                self.enemies.horde_y[13] = -100
                pygame.mixer.Sound.play(explosion)
            

            pygame.display.update()


            value = False
            self.count = 0

            for f in [self.enemies.status[0], self.enemies.status[1], self.enemies.status[2], self.enemies.status[3],
                      self.enemies.status[4], self.enemies.status[5], self.enemies.status[6], self.enemies.status[7],
                      self.enemies.status[8],self.enemies.status[9], self.enemies.status[10], self.enemies.status[11],
                      self.enemies.status[12],  self.enemies.status[13]]:

                if f == False:
                    self.count += 1
                if self.count == 14:
                    self.reset()
                    self.enemies.level += 0.5
                    self.reset()
                    self.count = 0
                    self.player.health = 5
        if self.enemies.level == 3:
            if self.blue_light_collision(0, 150, 435 + self.projectile.difference, self.projectile.ys[self.projectile.num], 200):
                    self.projectile.ys[self.projectile.num] = -25
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

            if self.blue_light_collision(700, 150, 435 + self.projectile.difference, self.projectile.ys[self.projectile.num], 200):
                    self.projectile.ys[self.projectile.num] = -25
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))


            if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx9, self.laser_y9):
                self.player.health -= 1
                self.col = False
                self.laser_y9 = 625
                pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))
            if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserx13, self.laser_y13):
                self.player.health -= 1
                self.col = False
                self.laser_y13 = 625
                pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("hit.wav")))
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[0], self.enemies.horde_y[0]):
                if self.h0 == 1:
                    self.h0 -= 1
                    self.enemies.horde_y[0] = -100
                    self.enemies.horde_x[0] = -399900
                    self.enemies.status[0] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.h0 > 1:
                    self.h0 -= 1
                    self.projectile.ys[self.projectile.num] = -26

                    pygame.mixer.Sound.play(hurt)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[1], self.enemies.horde_y[1]):

                if self.h1 == 1:
                    self.h1 -= 1
                    self.enemies.horde_y[1] = -100
                    self.enemies.horde_x[1] = -399900
                    self.enemies.status[1] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.h1 > 1:
                    self.h1 -= 1
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(hurt)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[2], self.enemies.horde_y[2]):
                self.enemies.horde_y[2] = -100
                self.enemies.status[2] = False
                self.enemies.horde_x[2] = -399900
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[3], self.enemies.horde_y[3]):
                self.enemies.horde_y[3] = -100
                self.enemies.horde_x[3] = -400000
                self.enemies.status[3] = False
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[4], self.enemies.horde_y[4]):
                self.enemies.horde_y[4] = -100
                self.enemies.status[4] = False
                self.enemies.horde_x[4] = -400000
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[5], self.enemies.horde_y[5]):
                self.enemies.horde_y[5] = -100
                self.enemies.horde_x[5] = -400000
                self.enemies.status[5] = False
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[6], self.enemies.horde_y[6]):
                self.enemies.horde_y[6] = -100
                self.enemies.horde_x[6] = -400000
                self.enemies.status[6] = False
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[7], self.enemies.horde_y[7]):
                
                if self.h7 == 1:
                    self.h7 -= 1
                    self.enemies.horde_y[7] = -100
                    self.enemies.horde_x[7] = -399900
                    self.enemies.status[7] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.h7 > 1:
                    self.h7-= 1
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(hurt)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[8], self.enemies.horde_y[8]):
              
                if self.h8 == 1:
                    self.h8 -= 1
                    self.enemies.horde_y[8] = -100
                    self.enemies.horde_x[8] = -399900
                    self.enemies.status[8] = False
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
                if self.h8 > 1:
                    self.h8 -= 1
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(hurt)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[9], self.enemies.horde_y[9]):
                self.enemies.horde_y[9] = -100
                self.enemies.horde_x[9] = -400000
                self.enemies.status[9] = False
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[10], self.enemies.horde_y[10]):
                self.enemies.horde_x[10] = -400000
                self.enemies.horde_y[10] = -100
                self.enemies.status[10] = False
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[11], self.enemies.horde_y[11]):
                self.enemies.horde_x[11] = -400000
                self.enemies.horde_y[11] = -100
                self.enemies.status[11] = False
                self.projectile.ys[self.projectile.num] = -26
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[12], self.enemies.horde_y[12]):
                self.enemies.horde_x[12] = -400000
                self.enemies.status[12] = False
                self.projectile.ys[self.projectile.num] = -26
                self.enemies.horde_y[12] = -100
                pygame.mixer.Sound.play(explosion)
            if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[13], self.enemies.horde_y[13]):
                self.enemies.horde_x[13] = -400000
                self.enemies.status[13] = False
                self.projectile.ys[self.projectile.num] = -26
                self.enemies.horde_y[13] = -100
                pygame.mixer.Sound.play(explosion)
            if self.blue_light_collision(660, 280, 435 + self.projectile.difference,self.projectile.ys[self.projectile.num], 60 ):
                self.projectile.ys[self.projectile.num] = 100
                self.projectile.difference = 800 - 435
                
                
            if self.blue_light_collision(220, 280, 435 + self.projectile.difference,self.projectile.ys[self.projectile.num], 60 ):
                self.projectile.ys[self.projectile.num] = 100
                self.projectile.difference = 100 - 435
            

            pygame.display.update()


            value = False
            self.count = 0

            for f in [self.enemies.status[0], self.enemies.status[1], self.enemies.status[2], self.enemies.status[3],
                      self.enemies.status[4], self.enemies.status[5], self.enemies.status[6], self.enemies.status[7],
                      self.enemies.status[8],self.enemies.status[9], self.enemies.status[10], self.enemies.status[11],
                      self.enemies.status[12],  self.enemies.status[13]]:

                if f == False:
                    self.count += 1
                if self.count == 14:
                    self.reset()
                    self.enemies.level += 0.5
                    self.reset()
                    self.count = 0
                    self.player.health = 5












    def game_over(self):
        over = True
        while over:
            self.screen.fill((0,0,0))
            self.screen.blit(self.background, (0, 0))
            font1 = pygame.font.SysFont("Typeface Mario World Pixel Filled", 150, bold=False, italic=False)
            font2 = pygame.font.SysFont("Typeface Mario World Pixel Filled", 75, bold=False, italic=False)
            line = font1.render("Game Over", False, (200, 0, 0))
            line1 = font2.render("Restart?", False, (200, 0, 0))
            color = (200, 0, 0)

            self.screen.blit(line, (165, 80))
            self.screen.blit(line1, (350, 280))
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 330 <= mouse_x <= 580 and 260 <= mouse_y <= 350:
                color = (173, 216, 230)
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    over = False
            pygame.draw.rect(self.screen, color, [330, 260, 250, 90], 5, 10 )

            pygame.display.update()
            pygame.mixer.music.stop()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()


    def run(self):
        run = True
        pause = False
        while run:

            r = random.randint(3, 9)
            if self.enemies.level == 3:
                f = 1.2
            else:
                f = 1.4
            if self.enemies.down:
                        if self.laser_y < 625:

                                self.laser_y +=  f
                                self.enemies.laserx = self.enemies.laserx
            if self.enemies.down1:
                        if self.laser_y1 < 625:

                                self.laser_y1 +=  f
                                self.enemies.laserx1 = self.enemies.laserx1
            if self.enemies.down2:
                        if self.laser_y2 < 625:

                                self.laser_y2 +=  f
                                self.enemies.laserx2 = self.enemies.laserx2
            if self.enemies.down3:
                        if self.laser_y3 < 625:

                                self.laser_y3 +=  f
                                self.enemies.laserx3 = self.enemies.laserx3
            if self.enemies.down4:
                        if self.laser_y4 < 625:

                                self.laser_y4 +=  f
                                self.enemies.laserx4 = self.enemies.laserx4
            if self.enemies.down5:
                        if self.laser_y5 < 625:

                                self.laser_y5 +=  f
                                self.enemies.laserx5 = self.enemies.laserx5
            if self.enemies.down6:
                        if self.laser_y6 < 625:

                                self.laser_y6 +=  f
                                self.enemies.laserx6 = self.enemies.laserx6
            if self.enemies.down7:
                        if self.laser_y7 < 625:

                                self.laser_y7 +=  f
                                self.enemies.laserx7 = self.enemies.laserx7
            if self.enemies.down8:
                        if self.laser_y8 < 625:

                                self.laser_y8 +=  f
                                self.enemies.laserx8 = self.enemies.laserx8
            if self.enemies.down9:
                        if self.laser_y9 < 625:

                                self.laser_y9 +=  f
                                self.enemies.laserx9 = self.enemies.laserx9
            if self.enemies.down10:
                        if self.laser_y10 < 625:

                                self.laser_y10 +=  f
                                self.enemies.laserx10 = self.enemies.laserx10
            if self.enemies.down11:
                        if self.laser_y11 < 625:

                                self.laser_y11 +=  f
                                self.enemies.laserx11 = self.enemies.laserx11
            if self.enemies.down12:
                        if self.laser_y12 < 625:

                                self.laser_y12 +=  f
                                self.enemies.laserx12 = self.enemies.laserx12
            if self.enemies.down13:
                        if self.laser_y13 < 625:

                                self.laser_y13 +=  f
                                self.enemies.laserx13 = self.enemies.laserx13





            if self.enemies.level ==1:

                #Movement  in level 1 (to the right)
                if self.direction == "right":
                    if self.enemies.status[0]:
                        if self.enemies.horde_x[0] < 525:
                            if self.enemies.down:
                                self.enemies.horde_x[0] += 0.5
                            if not self.enemies.down:
                                self.enemies.horde_x[0] += 0.5
                                self.enemies.laserx += 0.5
                if self.direction == "right":
                    if self.enemies.status[1]:
                        if self.enemies.horde_x[1]  < 580:
                            if self.enemies.down1:
                                self.enemies.horde_x[1] += 0.5
                            if not self.enemies.down1:
                                self.enemies.horde_x[1] += 0.5
                                self.enemies.laserx1 += 0.5
                if self.direction == "right":
                    if self.enemies.status[2]:
                        if self.enemies.horde_x[2]  < 635:
                            if self.enemies.down2:
                                self.enemies.horde_x[2] += 0.5
                            if not self.enemies.down2:
                                self.enemies.horde_x[2] += 0.5
                                self.enemies.laserx2 += 0.5
                if self.direction == "right":
                    if self.enemies.status[3]:
                        if self.enemies.horde_x[3]  < 690:
                            if self.enemies.down3:
                                self.enemies.horde_x[3] += 0.5
                            if not self.enemies.down3:
                                self.enemies.horde_x[3] += 0.5
                                self.enemies.laserx3 += 0.5
                if self.direction == "right":
                    if self.enemies.status[4]:
                        if self.enemies.horde_x[4]  < 745:
                            if self.enemies.down4:
                                self.enemies.horde_x[4] += 0.5
                            if not self.enemies.down4:
                                self.enemies.horde_x[4] += 0.5
                                self.enemies.laserx4 += 0.5
                if self.direction == "right":
                    if self.enemies.status[5]:
                        if self.enemies.horde_x[5]  < 800:
                            if self.enemies.down5:
                                self.enemies.horde_x[5] += 0.5
                            if not self.enemies.down5:
                                self.enemies.horde_x[5] += 0.5
                                self.enemies.laserx5 += 0.5
                if self.direction == "right":
                    if self.enemies.status[6]:
                        if self.enemies.horde_x[6]  < 525:
                            if self.enemies.down6:
                                self.enemies.horde_x[6] += 0.5
                            if not self.enemies.down6:
                                self.enemies.horde_x[6] += 0.5
                                self.enemies.laserx6 += 0.5
                if self.direction == "right":
                    if self.enemies.status[7]:
                        if self.enemies.horde_x[7]  < 635:
                            if self.enemies.down7:
                                self.enemies.horde_x[7] += 0.5
                            if not self.enemies.down7:
                                self.enemies.horde_x[7] += 0.5
                                self.enemies.laserx7 += 0.5
                if self.direction == "right":
                    if self.enemies.status[8]:
                        if self.enemies.horde_x[8]  < 690:
                            if self.enemies.down8:
                                self.enemies.horde_x[8] += 0.5
                            if not self.enemies.down8:
                                self.enemies.horde_x[8] += 0.5
                                self.enemies.laserx8 += 0.5
                if self.direction == "right":
                    if self.enemies.status[10]:
                        if self.enemies.horde_x[10]  < 800:
                            if self.enemies.down10:
                                self.enemies.horde_x[10] += 0.5
                            if not self.enemies.down10:
                                self.enemies.horde_x[10] += 0.5
                                self.enemies.laserx10 += 0.5
                if self.direction == "right":
                    if self.enemies.status[11]:
                        if self.enemies.horde_x[11]  < 525:
                            if self.enemies.down11:
                                self.enemies.horde_x[11] += 0.5
                            if not self.enemies.down11:
                                self.enemies.horde_x[11] += 0.5
                                self.enemies.laserx11 += 0.5
                if self.direction == "right":
                    if self.enemies.status[12]:
                        if self.enemies.horde_x[12]  < 800:
                            if self.enemies.down12:
                                self.enemies.horde_x[12] += 0.5
                            if not self.enemies.down12:
                                self.enemies.horde_x[12] += 0.5
                                self.enemies.laserx12 += 0.5

                #Switching Direction1= level 1 (from right to left)
                if self.direction == "right":
                    if self.enemies.status[0]:
                        if self.enemies.horde_x[0]  == 525:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[1]:
                        if self.enemies.horde_x[1]  == 580:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[2]:
                        if self.enemies.horde_x[2]  == 635:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[3]:
                        if self.enemies.horde_x[3]  ==690:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[4]:
                        if self.enemies.horde_x[4]  ==745:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[5]:
                        if self.enemies.horde_x[5]  ==800:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[6]:
                        if self.enemies.horde_x[6]  ==525:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[7]:
                        if self.enemies.horde_x[7]  ==635:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[8]:
                        if self.enemies.horde_x[8]  ==690:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[10]:
                        if self.enemies.horde_x[10]  == 800:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[11]:
                        if self.enemies.horde_x[11]  ==525:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[12]:
                        if self.enemies.horde_x[12]  ==800:
                            self.direction = "left"

                #Movement  in level 1 (to the left)
                if self.direction == "left":
                    if self.enemies.horde_x[0] > 70:
                        if self.enemies.down:
                            self.enemies.horde_x[0] -= 0.5
                        if not self.enemies.down:
                            self.enemies.horde_x[0] -= 0.5
                            self.enemies.laserx -= 0.5
                    if self.enemies.horde_x[1] > 125:
                        if self.enemies.down1:
                            self.enemies.horde_x[1] -= 0.5
                        if not self.enemies.down1:
                            self.enemies.horde_x[1] -= 0.5
                            self.enemies.laserx1 -= 0.5
                    if self.enemies.horde_x[2] > 180:
                        if self.enemies.down2:
                            self.enemies.horde_x[2] -= 0.5
                        if not self.enemies.down2:
                            self.enemies.horde_x[2] -= 0.5
                            self.enemies.laserx2 -= 0.5
                    if self.enemies.horde_x[3] > 235:
                        if self.enemies.down3:
                            self.enemies.horde_x[3] -= 0.5
                        if not self.enemies.down3:
                            self.enemies.horde_x[3] -= 0.5
                            self.enemies.laserx3 -= 0.5
                    if self.enemies.horde_x[4] > 290:
                        if self.enemies.down4:
                            self.enemies.horde_x[4] -= 0.5
                        if not self.enemies.down4:
                            self.enemies.horde_x[4] -= 0.5
                            self.enemies.laserx4 -= 0.5
                    if self.enemies.horde_x[5] > 345:
                        if self.enemies.down5:
                            self.enemies.horde_x[5] -= 0.5
                        if not self.enemies.down5:
                            self.enemies.horde_x[5] -= 0.5
                            self.enemies.laserx5 -= 0.5
                    if self.enemies.horde_x[6] > 70:
                        if self.enemies.down6:
                            self.enemies.horde_x[6] -= 0.5
                        if not self.enemies.down6:
                            self.enemies.horde_x[6] -= 0.5
                            self.enemies.laserx6 -= 0.5
                    if self.enemies.horde_x[7] > 180:
                        if self.enemies.down7:
                            self.enemies.horde_x[7] -= 0.5
                        if not self.enemies.down7:
                            self.enemies.horde_x[7] -= 0.5
                            self.enemies.laserx7 -= 0.5
                    if self.enemies.horde_x[8] > 235:
                        if self.enemies.down8:
                            self.enemies.horde_x[8] -= 0.5
                        if not self.enemies.down8:
                            self.enemies.horde_x[8] -= 0.5
                            self.enemies.laserx8 -= 0.5
                    if self.enemies.horde_x[10] > 345:
                        if self.enemies.down10:
                            self.enemies.horde_x[10] -= 0.5
                        if not self.enemies.down10:
                            self.enemies.horde_x[10] -= 0.5
                            self.enemies.laserx10 -= 0.5
                    if self.enemies.horde_x[11] > 70:
                        if self.enemies.down11:
                            self.enemies.horde_x[11] -= 0.5
                        if not self.enemies.down11:
                            self.enemies.horde_x[11] -= 0.5
                            self.enemies.laserx11 -= 0.5
                    if self.enemies.horde_x[12] > 345:
                        if self.enemies.down12:
                            self.enemies.horde_x[12] -= 0.5
                        if not self.enemies.down12:
                            self.enemies.horde_x[12] -= 0.5
                            self.enemies.laserx12 -= 0.5
                #Switching directions in level 1 (from left to right)
                if self.direction == "left":
                    if self.enemies.horde_x[0] == 70:
                        self.direction = "right"
                    if self.enemies.horde_x[1] == 125:
                        self.direction = "right"
                    if self.enemies.horde_x[2] == 180:
                        self.direction = "right"
                    if self.enemies.horde_x[3] == 235:
                        self.direction = "right"
                    if self.enemies.horde_x[4] == 290:
                        self.direction = "right"
                    if self.enemies.horde_x[5] == 345:
                        self.direction = "right"
                    if self.enemies.horde_x[6] ==70:
                        self.direction = "right"
                    if self.enemies.horde_x[7] ==180:
                        self.direction = "right"
                    if self.enemies.horde_x[8] ==235:
                        self.direction = "right"
                    if self.enemies.horde_x[10] == 345:
                        self.direction = "right"
                    if self.enemies.horde_x[11] ==70:
                        self.direction = "right"
                    if self.enemies.horde_x[12] ==345:
                        self.direction = "right"
            if self.enemies.level == 2:
                 #Movement  in level 2 (to the right)
                if self.direction == "right":
                    if self.enemies.status[0]:
                        if self.enemies.horde_x[0] < 740:
                            if self.enemies.down:
                                self.enemies.horde_x[0] += 0.5
                            if not self.enemies.down:
                                self.enemies.horde_x[0] += 0.5
                                self.enemies.laserx += 0.5

                    if self.enemies.status[1]:
                        if self.enemies.horde_x[1]  < 740:
                            if self.enemies.down1:
                                self.enemies.horde_x[1] += 0.5
                            if not self.enemies.down1:
                                self.enemies.horde_x[1] += 0.5
                                self.enemies.laserx1 += 0.5

                    if self.enemies.status[2]:
                        if self.enemies.horde_x[2]  < 740:
                            if self.enemies.down2:
                                self.enemies.horde_x[2] += 0.5
                            if not self.enemies.down2:
                                self.enemies.horde_x[2] += 0.5
                                self.enemies.laserx2 += 0.5

                    if self.enemies.status[3]:
                        if self.enemies.horde_x[3]  < 795:
                            if self.enemies.down3:
                                self.enemies.horde_x[3] += 0.5
                            if not self.enemies.down3:
                                self.enemies.horde_x[3] += 0.5
                                self.enemies.laserx3 += 0.5

                    if self.enemies.status[4]:
                        if self.enemies.horde_x[4]  < 795:
                            if self.enemies.down4:
                                self.enemies.horde_x[4] += 0.5
                            if not self.enemies.down4:
                                self.enemies.horde_x[4] += 0.5
                                self.enemies.laserx4 += 0.5

                    if self.enemies.status[5]:
                        if self.enemies.horde_x[5]  < 850:
                            if self.enemies.down5:
                                self.enemies.horde_x[5] += 0.5
                            if not self.enemies.down5:
                                self.enemies.horde_x[5] += 0.5
                                self.enemies.laserx5 += 0.5

                    if self.enemies.status[6]:
                        if self.enemies.horde_x[6]  < 850:
                            if self.enemies.down6:
                                self.enemies.horde_x[6] += 0.5
                            if not self.enemies.down6:
                                self.enemies.horde_x[6] += 0.5
                                self.enemies.laserx6 += 0.5

                    if self.enemies.status[7]:
                        if self.enemies.horde_x[7]  > 205:
                            if self.enemies.down7:
                                self.enemies.horde_x[7] -= 0.5
                            if not self.enemies.down7:
                                self.enemies.horde_x[7] -= 0.5
                                self.enemies.laserx7 -= 0.5

                    if self.enemies.status[8]:
                        if self.enemies.horde_x[8]  > 205:
                            if self.enemies.down8:
                                self.enemies.horde_x[8] -= 0.5
                            if not self.enemies.down8:
                                self.enemies.horde_x[8] -= 0.5
                                self.enemies.laserx8 -= 0.5
                    if self.enemies.status[9]:
                        if self.enemies.horde_x[9]  > 205:
                            if self.enemies.down8:
                                self.enemies.horde_x[9] -= 0.5
                            if not self.enemies.down8:
                                self.enemies.horde_x[9] -= 0.5
                                self.enemies.laserx8 -= 0.5

                    if self.enemies.status[10]:
                        if self.enemies.horde_x[10]  > 150:
                            if self.enemies.down10:
                                self.enemies.horde_x[10] -= 0.5
                            if not self.enemies.down10:
                                self.enemies.horde_x[10] -= 0.5
                                self.enemies.laserx10 -= 0.5

                    if self.enemies.status[11]:
                        if self.enemies.horde_x[11]  > 150:
                            if self.enemies.down11:
                                self.enemies.horde_x[11] -= 0.5
                            if not self.enemies.down11:
                                self.enemies.horde_x[11] -= 0.5
                                self.enemies.laserx11 -= 0.5

                    if self.enemies.status[12]:
                        if self.enemies.horde_x[12]  > 95:
                            if self.enemies.down12:
                                self.enemies.horde_x[12] -= 0.5
                            if not self.enemies.down12:
                                self.enemies.horde_x[12] -= 0.5
                                self.enemies.laserx12 -= 0.5
                    if self.enemies.status[13]:
                        if self.enemies.horde_x[13]  > 95:
                            if self.enemies.down12:
                                self.enemies.horde_x[13] -= 0.5
                            if not self.enemies.down12:
                                self.enemies.horde_x[13] -= 0.5
                                self.enemies.laserx12 -= 0.5


                #Switching Direction1= level 2 (from right to left)
                if self.direction == "right":
                    if self.enemies.status[0]:
                        if self.enemies.horde_x[0]  == 740:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[1]:
                        if self.enemies.horde_x[1]  == 740:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[2]:
                        if self.enemies.horde_x[2]  == 740:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[3]:
                        if self.enemies.horde_x[3]  ==795:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[4]:
                        if self.enemies.horde_x[4]  ==795:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[5]:
                        if self.enemies.horde_x[5]  ==850:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[6]:
                        if self.enemies.horde_x[6]  ==850:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[7]:
                        if self.enemies.horde_x[7]  ==205:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[8]:
                        if self.enemies.horde_x[8]  ==205:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[9]:
                        if self.enemies.horde_x[9]  ==205:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[10]:
                        if self.enemies.horde_x[10]  == 150:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[11]:
                        if self.enemies.horde_x[11]  ==150:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[12]:
                        if self.enemies.horde_x[12]  ==95:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[13]:
                        if self.enemies.horde_x[13]  ==95:
                            self.direction = "left"

                #Movement  in level 2 (to the left)
                if self.direction == "left":
                    if self.enemies.horde_x[0] > 150:
                        if self.enemies.down:
                            self.enemies.horde_x[0] -= 0.5
                        if not self.enemies.down:
                            self.enemies.horde_x[0] -= 0.5
                            self.enemies.laserx -= 0.5
                    if self.enemies.horde_x[1] > 150:
                        if self.enemies.down1:
                            self.enemies.horde_x[1] -= 0.5
                        if not self.enemies.down1:
                            self.enemies.horde_x[1] -= 0.5
                            self.enemies.laserx1 -= 0.5
                    if self.enemies.horde_x[2] > 150:
                        if self.enemies.down2:
                            self.enemies.horde_x[2] -= 0.5
                        if not self.enemies.down2:
                            self.enemies.horde_x[2] -= 0.5
                            self.enemies.laserx2 -= 0.5
                    if self.enemies.horde_x[3] > 205:
                        if self.enemies.down3:
                            self.enemies.horde_x[3] -= 0.5
                        if not self.enemies.down3:
                            self.enemies.horde_x[3] -= 0.5
                            self.enemies.laserx3 -= 0.5
                    if self.enemies.horde_x[4] > 205:
                        if self.enemies.down4:
                            self.enemies.horde_x[4] -= 0.5
                        if not self.enemies.down4:
                            self.enemies.horde_x[4] -= 0.5
                            self.enemies.laserx4 -= 0.5
                    if self.enemies.horde_x[5] > 260:
                        if self.enemies.down5:
                            self.enemies.horde_x[5] -= 0.5
                        if not self.enemies.down5:
                            self.enemies.horde_x[5] -= 0.5
                            self.enemies.laserx5 -= 0.5
                    if self.enemies.horde_x[6] > 260:
                        if self.enemies.down6:
                            self.enemies.horde_x[6] -= 0.5
                        if not self.enemies.down6:
                            self.enemies.horde_x[6] -= 0.5
                            self.enemies.laserx6 -= 0.5
                    if self.enemies.horde_x[7] < 795:
                        if self.enemies.down7:
                            self.enemies.horde_x[7] += 0.5
                        if not self.enemies.down7:
                            self.enemies.horde_x[7] += 0.5
                            self.enemies.laserx7 += 0.5
                    if self.enemies.horde_x[8] < 795:
                        if self.enemies.down8:
                            self.enemies.horde_x[8] += 0.5
                        if not self.enemies.down8:
                            self.enemies.horde_x[8] += 0.5
                            self.enemies.laserx8 += 0.5
                    if self.enemies.horde_x[9] < 795:
                        if self.enemies.down8:
                            self.enemies.horde_x[9] += 0.5
                        if not self.enemies.down8:
                            self.enemies.horde_x[9] += 0.5
                            self.enemies.laserx8 += 0.5
                    if self.enemies.horde_x[10] < 205 + 535:
                        if self.enemies.down10:
                            self.enemies.horde_x[10] += 0.5
                        if not self.enemies.down10:
                            self.enemies.horde_x[10] += 0.5
                            self.enemies.laserx10 += 0.5
                    if self.enemies.horde_x[11] < 205 + 535:
                        if self.enemies.down11:
                            self.enemies.horde_x[11] += 0.5
                        if not self.enemies.down11:
                            self.enemies.horde_x[11] += 0.5
                            self.enemies.laserx11 += 0.5
                    if self.enemies.horde_x[12] < 150 + 535:
                        if self.enemies.down12:
                            self.enemies.horde_x[12] += 0.5
                        if not self.enemies.down12:
                            self.enemies.horde_x[12] += 0.5
                            self.enemies.laserx12 += 0.5
                    if self.enemies.horde_x[13] < 150 + 535:
                        if self.enemies.down12:
                            self.enemies.horde_x[13] += 0.5
                        if not self.enemies.down12:
                            self.enemies.horde_x[13] += 0.5
                            self.enemies.laserx12 += 0.5
                #Switching directions in level 2 (from left to right)
                if self.direction == "left":
                    if self.enemies.horde_x[0] == 150:
                        self.direction = "right"
                    if self.enemies.horde_x[1] == 150:
                        self.direction = "right"
                    if self.enemies.horde_x[2] == 150:
                        self.direction = "right"
                    if self.enemies.horde_x[3] == 205:
                        self.direction = "right"
                    if self.enemies.horde_x[4] == 205:
                        self.direction = "right"
                    if self.enemies.horde_x[5] == 260:
                        self.direction = "right"
                    if self.enemies.horde_x[6] ==260:
                        self.direction = "right"
                    if self.enemies.horde_x[7] ==795:
                        self.direction = "right"
                    if self.enemies.horde_x[8] ==795:
                        self.direction = "right"
                    if self.enemies.horde_x[9] ==795:
                        self.direction = "right"
                    if self.enemies.horde_x[10] == 740:
                        self.direction = "right"
                    if self.enemies.horde_x[11] == 740:
                        self.direction = "right"
                    if self.enemies.horde_x[12] ==695:
                        self.direction = "right"
                    if self.enemies.horde_x[13] ==695:
                        self.direction = "right"
            if self.enemies.level == 3:
                 #Movement  in level 2 (to the right)
                if self.direction == "right":
                    if self.enemies.status[0]:
                        if self.enemies.horde_x[0] < 200:
                            if self.enemies.down:
                                self.enemies.horde_x[0] += 0.5
                            if not self.enemies.down:
                                self.enemies.horde_x[0] += 0.5
                                self.enemies.laserx += 0.5

                    if self.enemies.status[1]:
                        if self.enemies.horde_x[1]  > 700:
                            if self.enemies.down1:
                                self.enemies.horde_x[1] -= 0.5
                            if not self.enemies.down1:
                                self.enemies.horde_x[1] -= 0.5
                                self.enemies.laserx1 -= 0.5
                if self.direction2 == "right":
                    if self.enemies.status[2]:
                        if self.enemies.horde_x[2]  < 590:
                            if self.enemies.down2:
                                self.enemies.horde_x[2] += 0.5
                            if not self.enemies.down2:
                                self.enemies.horde_x[2] += 0.5
                                self.enemies.laserx2 += 0.5

                    if self.enemies.status[3]:
                        if self.enemies.horde_x[3]  < 645:
                            if self.enemies.down3:
                                self.enemies.horde_x[3] += 0.5
                            if not self.enemies.down3:
                                self.enemies.horde_x[3] += 0.5
                                self.enemies.laserx3 += 0.5

                    if self.enemies.status[4]:
                        if self.enemies.horde_x[4]  < 700:
                            if self.enemies.down4:
                                self.enemies.horde_x[4] += 0.5
                            if not self.enemies.down4:
                                self.enemies.horde_x[4] += 0.5
                                self.enemies.laserx4 += 0.5
                if self.direction3 == "right":

                    if self.enemies.status[5]:
                        if self.enemies.horde_x[5]  > 310:
                            if self.enemies.down5:
                                self.enemies.horde_x[5] -= 0.5
                            if not self.enemies.down5:
                                self.enemies.horde_x[5] -= 0.5
                                self.enemies.laserx5 -= 0.5

                    if self.enemies.status[6]:
                        if self.enemies.horde_x[6]  > 255:
                            if self.enemies.down6:
                                self.enemies.horde_x[6] -= 0.5
                            if not self.enemies.down6:
                                self.enemies.horde_x[6] -= 0.5
                                self.enemies.laserx6 -= 0.5
                    if self.enemies.status[13]:
                        if self.enemies.horde_x[13]  > 200:
                            if self.enemies.down12:
                                self.enemies.horde_x[13] -= 0.5
                            if not self.enemies.down12:
                                self.enemies.horde_x[13] -= 0.5
                                self.enemies.laserx12 -= 0.5
                if self.direction1 == "right":

                    if self.enemies.status[7]:
                        if self.enemies.horde_x[7]  < 575:
                            if self.enemies.down7:
                                self.enemies.horde_x[7] += 0.5
                            if not self.enemies.down7:
                                self.enemies.horde_x[7] += 0.5
                                self.enemies.laserx7 += 0.5

                    if self.enemies.status[8]:
                        if self.enemies.horde_x[8]  < 630:
                            if self.enemies.down8:
                                self.enemies.horde_x[8] += 0.5
                            if not self.enemies.down8:
                                self.enemies.horde_x[8] += 0.5
                                self.enemies.laserx8 += 0.5
                    if self.enemies.status[9]:
                        if self.enemies.horde_x[9]  < 490:
                            if self.enemies.down8:
                                self.enemies.horde_x[9] += 0.5
                            if not self.enemies.down8:
                                self.enemies.horde_x[9] += 0.5
                                self.enemies.laserx8 += 0.5

                    if self.enemies.status[10]:
                        if self.enemies.horde_x[10]  < 560:
                            if self.enemies.down10:
                                self.enemies.horde_x[10] += 0.5
                            if not self.enemies.down10:
                                self.enemies.horde_x[10] += 0.5
                                self.enemies.laserx10 += 0.5

                    if self.enemies.status[11]:
                        if self.enemies.horde_x[11]  < 630:
                            if self.enemies.down11:
                                self.enemies.horde_x[11] += 0.5
                            if not self.enemies.down11:
                                self.enemies.horde_x[11] += 0.5
                                self.enemies.laserx11 += 0.5

                    if self.enemies.status[12]:
                        if self.enemies.horde_x[12]  < 700:
                            if self.enemies.down12:
                                self.enemies.horde_x[12] += 0.5
                            if not self.enemies.down12:
                                self.enemies.horde_x[12] += 0.5
                                self.enemies.laserx12 += 0.5
                    


                #Switching Direction1= level 2 (from right to left)
                if self.direction == "right":
                    if self.enemies.status[0]:
                        if self.enemies.horde_x[0]  == 200:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[1]:
                        if self.enemies.horde_x[1]  == 700:
                            self.direction = "left"
                if self.direction2 == "right":
                    if self.enemies.status[2]:
                        if self.enemies.horde_x[2]  == 590:
                            self.direction2 = "left"
                if self.direction2 == "right":
                    if self.enemies.status[3]:
                        if self.enemies.horde_x[3]  ==645:
                            self.direction2 = "left"
                if self.direction2 == "right":
                    if self.enemies.status[4]:
                        if self.enemies.horde_x[4]  ==700:
                            self.direction2 = "left"
                if self.direction3 == "right":
                    if self.enemies.status[5]:
                        if self.enemies.horde_x[5]  ==310:
                            self.direction3 = "left"
                if self.direction3 == "right":
                    if self.enemies.status[6]:
                        if self.enemies.horde_x[6]  ==255:
                            self.direction3 = "left"
                if self.direction1 == "right":
                    if self.enemies.status[7]:
                        if self.enemies.horde_x[7]  ==575:
                            self.direction1 = "left"
                if self.direction1 == "right":
                    if self.enemies.status[8]:
                        if self.enemies.horde_x[8]  ==630:
                            self.direction1 = "left"
                if self.direction1 == "right":
                    if self.enemies.status[9]:
                        if self.enemies.horde_x[9]  ==490:
                            self.direction1 = "left"
                if self.direction1 == "right":
                    if self.enemies.status[10]:
                        if self.enemies.horde_x[10]  == 560:
                            self.direction1 = "left"
                if self.direction1 == "right":
                    if self.enemies.status[11]:
                        if self.enemies.horde_x[11]  ==630:
                            self.direction1 = "left"
                if self.direction1 == "right":
                    if self.enemies.status[12]:
                        if self.enemies.horde_x[12]  ==700:
                            self.direction1 = "left"
                if self.direction3 == "right":
                    if self.enemies.status[13]:
                        if self.enemies.horde_x[13]  == 200:
                            self.direction3 = "left"

                #Movement  in level 2 (to the left)
                if self.direction == "left":
                    if self.enemies.horde_x[0] > 40:
                        if self.enemies.down:
                            self.enemies.horde_x[0] -= 0.5
                        if not self.enemies.down:
                            self.enemies.horde_x[0] -= 0.5
                            self.enemies.laserx -= 0.5
                    if self.enemies.horde_x[1] < 860:
                        if self.enemies.down1:
                            self.enemies.horde_x[1] += 0.5
                        if not self.enemies.down1:
                            self.enemies.horde_x[1] += 0.5
                            self.enemies.laserx1 += 0.5
                if self.direction2 == "left":
                    if self.enemies.horde_x[2] > 150:
                        if self.enemies.down2:
                            self.enemies.horde_x[2] -= 0.5
                        if not self.enemies.down2:
                            self.enemies.horde_x[2] -= 0.5
                            self.enemies.laserx2 -= 0.5
                    if self.enemies.horde_x[3] > 205:
                        if self.enemies.down3:
                            self.enemies.horde_x[3] -= 0.5
                        if not self.enemies.down3:
                            self.enemies.horde_x[3] -= 0.5
                            self.enemies.laserx3 -= 0.5
                    if self.enemies.horde_x[4] > 260:
                        if self.enemies.down4:
                            self.enemies.horde_x[4] -= 0.5
                        if not self.enemies.down4:
                            self.enemies.horde_x[4] -= 0.5
                            self.enemies.laserx4 -= 0.5
                if self.direction3 == "left":
                    if self.enemies.horde_x[5] < 745:
                        if self.enemies.down5:
                            self.enemies.horde_x[5] += 0.5
                        if not self.enemies.down5:
                            self.enemies.horde_x[5] += 0.5
                            self.enemies.laserx5 += 0.5
                    if self.enemies.horde_x[6] < 690:
                        if self.enemies.down6:
                            self.enemies.horde_x[6] += 0.5
                        if not self.enemies.down6:
                            self.enemies.horde_x[6] += 0.5
                            self.enemies.laserx6 += 0.5
                    if self.enemies.horde_x[13] < 635:
                        if self.enemies.down7:
                            self.enemies.horde_x[13] += 0.5
                        if not self.enemies.down7:
                            self.enemies.horde_x[13] += 0.5
                            self.enemies.laserx7 += 0.5
                if self.direction1 == "left":
                    if self.enemies.horde_x[7] > 335:
                        if self.enemies.down7:
                            self.enemies.horde_x[7] -= 0.5
                        if not self.enemies.down7:
                            self.enemies.horde_x[7] -= 0.5
                            self.enemies.laserx7 -= 0.5
                    if self.enemies.horde_x[8] > 390:
                        if self.enemies.down8:
                            self.enemies.horde_x[8] -= 0.5
                        if not self.enemies.down8:
                            self.enemies.horde_x[8] -= 0.5
                            self.enemies.laserx8 -= 0.5
                    if self.enemies.horde_x[9] > 250:
                        if self.enemies.down8:
                            self.enemies.horde_x[9] -= 0.5
                        if not self.enemies.down8:
                            self.enemies.horde_x[9] -= 0.5
                            self.enemies.laserx8 -= 0.5
                    if self.enemies.horde_x[10]  >320:
                        if self.enemies.down10:
                            self.enemies.horde_x[10] -= 0.5
                        if not self.enemies.down10:
                            self.enemies.horde_x[10] -= 0.5
                            self.enemies.laserx10 -= 0.5
                    if self.enemies.horde_x[11] > 390:
                        if self.enemies.down11:
                            self.enemies.horde_x[11] -= 0.5
                        if not self.enemies.down11:
                            self.enemies.horde_x[11] -= 0.5
                            self.enemies.laserx11 -= 0.5
                    if self.enemies.horde_x[12] > 460:
                        if self.enemies.down12:
                            self.enemies.horde_x[12] -= 0.5
                        if not self.enemies.down12:
                            self.enemies.horde_x[12] -= 0.5
                            self.enemies.laserx12 -= 0.5

                #Switching directions in level 2 (from left to right)
                if self.direction == "left":
                    if self.enemies.horde_x[0] == 40:
                        self.direction = "right"
                    if self.enemies.horde_x[1] == 860:
                        self.direction = "right"
                if self.direction2 == "left":
                    if self.enemies.horde_x[2] == 150:
                        self.direction2 = "right"
                    if self.enemies.horde_x[3] == 205:
                        self.direction2 = "right"
                    if self.enemies.horde_x[4] == 260:
                        self.direction2 = "right"
                    
                if self.direction3 == "left":
                    if self.enemies.horde_x[5] == 745:
                        self.direction3 = "right"
                    if self.enemies.horde_x[6] == 690:
                        self.direction3 = "right"
                    if self.enemies.horde_x[13] ==635:
                        self.direction3 = "right"
                if self.direction1 == "left":
                    if self.enemies.horde_x[7] == 335:
                        self.direction1 = "right"
                    if self.enemies.horde_x[8] ==390:
                        self.direction1 = "right"
                    if self.enemies.horde_x[9] ==250 :
                        self.direction1 = "right"
                    if self.enemies.horde_x[10] == 320:
                        self.direction1 = "right"
                    if self.enemies.horde_x[11] == 390:
                        self.direction1 = "right"
                    if self.enemies.horde_x[12] == 460:
                        self.direction1 = "right"
                    
            
            
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
                    if self.enemies.level == 1.5 or self.enemies.level == 2.5:
                            self.enemies.level += 0.5
                    save.save_game(self.enemies.level, "level")
                pygame.key.set_repeat(1, 1)
                if event.type == KEYDOWN:
                    if  self.enemies.level == 1  or self.enemies.level == 2  or self.enemies.level == 3:   

                        if event.key == K_a or event.key == K_LEFT or event.key == CONTROLLER_BUTTON_DPAD_LEFT:

                            if 1 <= self.player.x <= 830:
                                self.enemies.shot = True
                                if not self.up:
                                    self.projectile.difference -= 1

                                    self.player.x -= 1
                                if self.up:
                                    self.player.x -= 1
                                    self.backup -= 1
                        if event.key == K_d or event.key == K_RIGHT or event.key == CONTROLLER_BUTTON_DPAD_RIGHT:
                            if 0 <= self.player.x <= 829:
                                self.enemies.shot= True
                                if not self.up:
                                    self.projectile.difference += 1

                                    self.player.x += 1
                                if self.up:
                                    self.player.x += 1
                                    self.backup += 1

                        if event.key == K_SPACE or CONTROLLER_BUTTON_A:
                            pygame.key.set_repeat(1, 10)
                            self.enemies.shot = True
                            if not self.up:
                                pygame.mixer.Sound.play(laser)
                                self.projectile.difference = self.player.x - self.projectile.four + 25
                            self.up = True
                if event.type == KEYUP:

                        if event.key == K_ESCAPE:
                            pygame.key.set_repeat(1, 1)
                            pause = True
            while pause:
                font1 = pygame.font.SysFont("Typeface Mario World Pixel Filled", 70, bold=False, italic=False)
                line = font1.render("Paused", False, (255, 255, 255))
                self.screen.blit(line, (700, 10))
                pygame.display.update()
                for event in pygame.event.get():
                        pygame.key.set_repeat(1, 1)
                        if event.type == KEYUP:
                            if event.key == K_ESCAPE:
                                pause = False
                        if event.type == QUIT:
                            if self.enemies.level == 1.5 or self.enemies.level == 2.5:
                                self.enemies.level += 0.5
                            save.save_game(self.enemies.level, "level")
                            pygame.quit()
                            sys.exit()







                    #if keys[K_d] and keys[K_a]:
                     #   pygame.key.set_repeat(1, 1000000)
                      #  if 0 <= self.player.x <= 829:
                       #     self.player.x -= 1







            try:
                    self.play()

            except Exception as e:
               if self.player.health <= 0: 

                    self.game_over()
                    self.reset()
                    self.player.health = 5








if __name__ == '__main__':
    game = Game()
    game.title()
    game.run()

