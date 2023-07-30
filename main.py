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
from Sin_Wave import sine
clock = pygame.time.Clock()
#Function to get the app to compile to an exe properly
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
#Sounds and images I use later
laser = pygame.mixer.Sound(resource_path("Player laser.wav"))
explosion = pygame.mixer.Sound(resource_path("explosion.wav"))
laser1 = pygame.mixer.Sound(resource_path("enemy laser.wav"))
hurt = pygame.mixer.Sound(resource_path("hurt.wav"))
red = pygame.image.load(resource_path(r"red.png"))
hit = pygame.mixer.Sound(resource_path("hit.wav"))
white_barrier = pygame.mixer.Sound(resource_path("white barrier.wav"))
#Instances of the savesystem I built using a guide
save = SaveandLoad(".level_data", "Space invaders stuff" )
save_highscore = SaveandLoad(".high_score", "Space invaders stuff")
#Game over class to call game over when the player's health hits 0
class GameOver(Exception):
    pass
class Projectile:
    def __init__(self, screen,  y):
        #Color of the health
        self.color = (30, 30, 30)
        self.difference = 0
        self.num = 0
        self.four = 435
        #Y values for the projectiles of the player
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
        #Y values in a list so I can iterate through them
        self.ys = [self.y, self.y1, self.y2, self.y3, self.y4, self.y5, self.y6, self.y7, self.y8, self.y9]
        self.screen = screen
        #Player projectile model
        self.laser_sideways = pygame.image.load(resource_path("laser.png"))
        self.laser = pygame.transform.rotate(self.laser_sideways, 90)
    def draw_projectile(self):
        self.screen.blit(self.laser, (self.four + self.difference, self.ys[self.num]))
class Player:
    def __init__(self, x, y, screen):
        #player health
        self.health = 5
        self.screen = screen
        #Player model
        self.shooter = pygame.image.load(resource_path("Space-Invaders-Ship-PNG-Photo.png"))
        self.x = x
        self.y = y
    def draw_shooter(self):
        #Blits the player to the screen. The screen fill also serves to delete all previous instances of all images used in the game
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.shooter, (self.x, self.y))
    def draw_health(self):
        #Draw health and change color when it gets low
        font1 = pygame.font.SysFont("Comic Sans", 250, bold=False, italic=False)
        if self.health <= 2:
            self.color = (50, 0, 0)
        else:
            self.color = (50, 50, 50)
        line = font1.render(str(self.health), True, self.color)
        self.screen.blit(line, (375, sine(100, 1280, 0, 100)))
class Enemies:
    def __init__(self, screen):
        dimensions = [28, 45]
        self.score = 0
        #Variable that allows player to shoot
        self.shot = False
        #State of enemy lasers. If true, they cause the lasers to go downward
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
        self.down15 = False
        self.down16 = False
        self.down17= False
        self.down18= False
        self.down19 = False
        self.down20= False
        self.down21= False
        self.down22 = False
        self.down23 = False
        self.down24 = False
        self.down25 = False
        self.difference = 00
        self.direction = "right"
        #Loading the level(chceking if a save exists)
        if save.check_file("level"):
            self.level = save.load("level")
        else:
            self.level = 1
        #This inteneded fps is used to make the speeds of everything in the game constant, regardless of framerate
        if self.level >0:
            self.intended_fps = 180
        else:
            self.intended_fps = 163
        self.screen = screen
        self.ship = pygame.image.load(resource_path("Alien.png"))
        #ys of the enemies
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
        self.y13 = 80
        self.y14 = 80
        self.y15 = 80
        self.y16 = 80
        self.y17 = 80
        self.y18 = 80
        self.y19 = 80
        self.y20 = 80
        self.y21 = 80
        self.y22 = 80
        self.y23 = 80
        self.y24 = 80
        self.y25 = 80
        #xs of the enemies
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
        self.x14 =  -400000000000000
        self.x15 =  -400000000000000
        self.x16 =  -400000000000000
        self.x17 =  -400000000000000
        self.x18 =  -400000000000000
        self.x19 =  -400000000000000
        self.x20 =  -400000000000000
        self.x21 =  -400000000000000
        self.x22 =  -400000000000000
        self.x23 =  -400000000000000
        self.x24 =  -400000000000000
        self.x25 =  -400000000000000
        #the xs of enemy projectiles
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
        self.laserx13 = -40000000
        self.laserx14 = -40000000
        self.laserx15 = -40000000
        self.laserx16 = -40000000
        self.laserx17 = -40000000
        self.laserx18 = -40000000
        self.laserx19 = -40000000
        self.laserx20 = -40000000
        self.laserx21 = -40000000
        self.laserx22 = -40000000
        self.laserx23 = -40000000
        self.laserx24 = -40000000
        self.laserx25 = -40000000
        #Putting everything in the game so I can iterate through them late
        self.horde_y = [self.y, self.y1, self.y2, self.y3, self.y4 , self.y5, self.y6 , self.y7 ,self.y8, self.y9, self.y10,self.y11, self.y12, self.y13, self.y14, self.y15, self.y16, self.y17, self.y18,self.y19,self.y20,self.y21, self.y22, self.y23, self.y24, self.y25]
        self.horde_x = [self.x, self.x1, self.x2, self.x3, self.x4, self.x5, self.x6, self.x7, self.x8, self.x9,self.x10, self.x11, self.x12, self.x13, self.x14, self.x15, self.x16, self.x17, self.x18,self.x19,self.x20,self.x21, self.x22, self.x23, self.x24, self.x25]
        self.laserxs= [self.laserx, self.laserx1, self.laserx2, self.laserx3, self.laserx4, self.laserx5, self.laserx5, self.laserx6, self.laserx7, self.laserx8, self.laserx9, self.laserx10, self.laserx11, self.laserx12, self.laserx13, self.laserx14, self.laserx15, self.laserx16, self.laserx17, self.laserx18, self.laserx19, self.laserx20, self.laserx21, self.laserx22, self.laserx23, self.laserx24, self.laserx25]
        self.downs = [self.down, self.down1, self.down2, self.down3, self.down4, self.down5, self.down6, self.down7, self.down8, self.down9, self.down10, self.down11, self.down12, self.down13, self.down14, self.down15, self.down16, self.down17, self.down18, self.down19, self.down20, self.down21, self.down22, self.down22, self.down23, self.down24, self.down25]
        self.status = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        #These dictionaries are used specifically in the endless mode to get the enemies to respawn after their whole group is defeated.They aren't working at the moment.
        self.line= {self.horde_y[0]: True, self.horde_y[1]: True, self.horde_y[2]:True, self.horde_y[3]:True, self.horde_y[4]:True, self.horde_y[5]:True, self.horde_y[6]:True, self.horde_y[7]:True, self.horde_y[8]:True, self.horde_y[9]:True, self.horde_y[10]:True, self.horde_y[11]:True, self.horde_y[12]:True}
        self.line2={self.horde_y[13]:True, self.horde_y[14]:True, self.horde_y[15]:True, self.horde_y[16]:True, self.horde_y[17]:True, self.horde_y[18]:True, self.horde_y[19]:True, self.horde_y[20]:True, self.horde_y[21]: True, self.horde_y[22]: True, self.horde_y[23]: True, self.horde_y[24]:True, self.horde_y[25]:True}
        self.list_line1 = []
        self.list_line2 = []
        if self.level == 2:
            for i in range(14, 26):
                self.horde_x[i] = -400000000000
            for i in range(0, 4):
                self.horde_y[i] = 20
                self.horde_x[i] = 350 + (60*i)
            for i in range(4, 8):
                self.horde_y[i] = 80
                self.horde_x[i] = 350 + (60*(i-4))
            for i in range(8, 11):
                self.horde_y[i] =140
                self.horde_x[i] = 150 + 50 + (60*(i-8))
            for i in range(11, 14):
                self.horde_y[i] =140
                self.horde_x[i] = 450 +(60*(i-11))
            for i in range(0, 14):
                self.laserxs[i] = self.horde_x[i] + 22.5 
        #Loading enemy positions for level 2
        if self.level == 3:  
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
                for i in range(14, 26):
                    self.horde_x[i] = -4000000000000
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
                #Resetting enemy status and making it so they can't shoot the moment the level starts
                self.status = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]  
                self.shot = False
                #setting enemy laser xs
                for i in range(0, 26):
                    self.laserxs[i] = self.horde_x[i] + 22.5
        #Doing the same for level 3
        if self.level ==4:
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
                for i in range(14, 26):
                    self.horde_x[i] = -400000000000
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
                for i in range(0, 26):
                    self.laserxs[i] = self.horde_x[i] + 22.5
        #Doing the same for endless mode, which the game recognizes as level 0
        if self.level == 0:
            standard = 80
            self.shot = False
            for i in range(0, 13):
                self.horde_y[i] =  70
                self.list_line1.append(self.horde_y[i])
            for i in range(13, 26):
                self.horde_y[i] = 120
                self.list_line2.append(self.horde_y[i])
            for i in range(0, 13):
                self.horde_x[i] = standard
                standard += 60
            for i in range(13, 26):
                self.horde_x[i] = self.horde_x[i - 13]
            for i in range(0, 26):
                self.laserxs[i] = self.horde_x[i] +22.5
    #functions for drawing all the objects and enemies
    def ship_placement(self, ship, x, y):
        self.screen.blit(ship, (x, y))
    def platform_placement(self, x1, y1, x_extension, y_extension):
        pygame.draw.rect(self.screen, (200, 200, 200), [x1, y1, x_extension, y_extension])
    def green_platform_placement(self, x1, y1, x_extension, y_extension):
        pygame.draw.rect(self.screen, (0, 150, 0), [x1, y1, x_extension, y_extension])
    def portal_placement(self, color, x1, y1, x_extension, y_extension):
        pygame.draw.rect(self.screen, color , [x1, y1, x_extension, y_extension])
    def level1(self):
        #Drawing level 1 to the screen
        if self.level == 1:
            for i in range(0, 13):
                if i ==9:
                    continue
                if self.horde_y[i] < 900:
                    self.ship_placement(self.ship, self.horde_x[i], self.horde_y[i])
            self.platform_placement(200, 300, 90, 5)
            self.platform_placement(650, 300, 90, 5)
            pygame.display.update()
        #Intermission screen 
        if (self.level/0.5) % 2 == 1:
            green = (0, 255, 0)
            self.screen.fill((0,0,0))
            y= sine(100, 1280, 10, 50)
            y1 = sine(100, 1280, 10, 220)
            font1 = pygame.font.SysFont("Comic Sans", 100, bold=False, italic=False)
            line = font1.render("Success", True, (0, 255, 0))
            self.screen.blit(line, (300 - 30, y))
            #Button color changes if you mouse over it. You eneter the next level if you click on it
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 280 <= mouse_x <= 610 + 30 -20 and 235 <= mouse_y <= 315:
                green = (173,216, 230)
                if pygame.mouse.get_pressed() != (0,0,0):
                    Game().reset()
                    self.level +=0.5
                    Game().reset()
            font2 = pygame.font.SysFont("Comic Sans", 75, bold=False, italic=False)
            line2 = font2.render("Continue?", True, (green))
            self.screen.blit(line2, (350 - 20 - 50 -10, y1))
            pygame.display.update()
        if self.level == 2:
            for i in range(0, 14):
                if self.horde_y[i] <900:
                    self.ship_placement(self.ship, self.horde_x[i], self.horde_y[i])
        if self.level == 3:
            #Drawing level 2 to the screen
            for i in range(0, 14):
                #The statement below checks if the enemy is on screen(aka still in play)
                if self.horde_y[i] < 900:
                    if i ==7 or i ==8 or i ==0 or i== 1:
                        self.ship_placement(red, self.horde_x[i], self.horde_y[i])
                    else:
                        self.ship_placement(self.ship, self.horde_x[i], self.horde_y[i])
            self.green_platform_placement(100, 250, 150, 5)
            self.platform_placement(550, 250, 120, 5)
        #Drawing level 3 to the screen
        if self.level ==4:
            for i in range(0, 14):
                if self.horde_y[i] < 900:
                 #The statement above checks if the enemy is on screen(aka still in play)
                    if i ==7 or i ==8 or i ==0 or i== 1:
                        self.ship_placement(red, self.horde_x[i], self.horde_y[i])
                    else:
                        self.ship_placement(self.ship, self.horde_x[i], self.horde_y[i])
                self.green_platform_placement(0, 150, 200, 5)
                self.green_platform_placement(700, 150, 200, 5)
                self.portal_placement( (0,191,255),660, 280, 60, 5,)
                self.portal_placement( (0,191,255),770, 100, 60, 5,)
                self.portal_placement( (0,0,139),220, 280, 60, 5,)
                self.portal_placement( (0,0,139),110, 100, 60, 5,)
        #Drawing endless mode to the screen
        if self.level == 0:
            for i in range(0, 26):
                #The statement below checks if the enemy is on screen(aka still in play)
                if self.horde_y[i] < 900:
                    if i ==7 or i ==8 or i ==0 or i== 1:
                        self.ship_placement(red, self.horde_x[i], self.horde_y[i])
                    else:
                        self.ship_placement(self.ship, self.horde_x[i], self.horde_y[i])
            font7 = pygame.font.SysFont("Comic Sans", 25, bold=False, italic=False)
            score = font7.render(f"Score: {str(self.score)} ", True, (255, 255, 255))
            y = sine(100, 1280, 5, 15)
            self.screen.blit(score, (420, y))
            pygame.display.update()
class Game:
    def __init__(self):
        self.lst = []
        self.lst1 = []
        #Health for enemies which take multiple hits to kill
        self.h0 = 3
        self.h1 = 3
        self.h7 = 3
        self.h8 = 3
        #Variables used to check the amount of enemies defeated. When they reach the required number the level ends
        self.count = 0
        self.count2 = 0
        #Game music
        pygame.mixer.music.load(resource_path("Music.mp3"))
        pygame.mixer.music.set_volume(0.35)
        pygame.mixer.music.play(-1)
        self.col = False
        #The direction variables. Usually only the first is used but occassionally the others are used
        self.direction = "right"
        self.direction1 = "right"
        self.direction2 = "right"
        self.direction3 = "right"
        #Enemy projectile model
        self.blastssss = pygame.image.load(resource_path("red laser.png"))
        self.blast = pygame.transform.rotate(self.blastssss, 270)
        self.backup = 0
        #Variable which causes player projectile to move upwards so long as it is true
        self.up = False
        #Window size
        self.screen_x = 900
        self.screen_y = 600
        #Game window formatting
        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
        icon = pygame.image.load(resource_path("title.png"))
        pygame.display.set_caption("Space Invaders")
        pygame.display.set_icon(icon)
        #Instances of the above classes
        self.player = Player(self.screen_x/2 - 40, self.screen_y - 80, self.screen)
        self.projectile = Projectile(self.screen, self.player.y - 35)
        self.enemies = Enemies(self.screen)
        #ys of the enemy projectiles
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
        self.laser_y14 = self.enemies.horde_y[14]+ 30
        self.laser_y15 = self.enemies.horde_y[15]+ 30
        self.laser_y16 = self.enemies.horde_y[16]+ 30
        self.laser_y17 = self.enemies.horde_y[17]+ 30
        self.laser_y18 = self.enemies.horde_y[18]+ 30
        self.laser_y19 = self.enemies.horde_y[19]+ 30
        self.laser_y20 = self.enemies.horde_y[20]+ 30
        self.laser_y21 = self.enemies.horde_y[21]+ 30
        self.laser_y22 = self.enemies.horde_y[22]+ 30
        self.laser_y23 = self.enemies.horde_y[23]+ 30
        self.laser_y24 = self.enemies.horde_y[24]+ 30
        self.laser_y25 = self.enemies.horde_y[25]+ 30
        #list of said ys
        self.laser_ys = [self.laser_y, self.laser_y1, self.laser_y2, self.laser_y3, self.laser_y4, self.laser_y5, self.laser_y6, self.laser_y7, self.laser_y8, self.laser_y9, self.laser_y10, self.laser_y11, self.laser_y12, self.laser_y13, self.laser_y14, self.laser_y15, self.laser_y16, self.laser_y17, self.laser_y18, self.laser_y19, self.laser_y20, self.laser_y21, self.laser_y22, self.laser_y23, self.laser_y24, self.laser_y25]
        #Player projectile speed
        if self.enemies.level > 0:
            self.projectile_speed = 4
        else:
            self.projectile_speed = 4.5
    #All the collision functions of the game
    def alien_laser_collision(self, x1, y1, x2, y2):
            if x2 - 20 <= x1 <= x2 + 40:
                if y1 - 20 <= y2 <= y1 + 20:
                    return True
            return False
    def red_laser_collision(self, x1, y1, x2, y2):
            if x1 -25 <= x2 <= x1 + 70:
                if y1 - 5 <= y2 <= y1 + 70:
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
        #Title screen
        while title:
             y = 10
             y1 = 150
             y2 = sine(100, 1280, 10, 270)
             y3 = sine(100, 1280, 10, 380)
             if save.check_file("level"):
                y4 = sine(100, 1280, 10, 490)
             else:
                y4 = sine(100, 1280, 10, 380)
             green = (0, 255, 0)
             color = (0, 255, 0)
             color1 = (0,255,0)
             font1 = pygame.font.SysFont("Comic Sans", 100, bold=False, italic=False)
             font2 = pygame.font.SysFont("Comic Sans", 75, bold=False, italic=False)
             red = pygame.image.load(resource_path("title1.jpg"))
             #These buttons function the same as the ones from before
             mouse_x, mouse_y = pygame.mouse.get_pos()
             #Button collision
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
            #The continue butto is only drawn if a save file exists
             line = font1.render("Space Invaders", True, (0, 255, 0))
             line1 = font2.render("New Game", True, (green))
             self.screen.fill((0,0,0))
             if save.check_file("level"):
                if 280 <= mouse_x <= 280 + 350 and 400 <= mouse_y <= 500:
                    color= (173, 216, 230)
                    if pygame.mouse.get_pressed() != (0,0,0):
                        self.reset()
                        self.enemies.level = save.load("level")
                        self.reset()
                        title = False
                line2 = font2.render("Continue", True, (color))
                self.screen.blit(line2, (300, y3))
                if 320 <= mouse_x <= 320 + 300 and 490 + 10 <= mouse_y <= 590:
                    color1= (173, 216, 230)
                    if pygame.mouse.get_pressed() != (0,0,0):
                        self.enemies.level = 0
                        title = False
                        self.reset()

             else:
                if 320 <= mouse_x <= 320 + 300 and 380 + 10 <= mouse_y <= 590:
                    color1= (173, 216, 230)
                    if pygame.mouse.get_pressed() != (0,0,0):
                        if self.enemies.level != 0:
                            self.enemies.level = 0
                            self.reset()
                        title = False             
             line3 = font2.render("Endless",True, (color1))
             self.screen.blit(line1, (270, y2))
             self.screen.blit(line, (100, y))
             self.screen.blit(red, (350, y1))
             self.screen.blit(line3, (320, y4))
             for event in pygame.event.get():
                 if event.type == QUIT:
                     if self.enemies.level != 1 and self.enemies.level != 0:
                        if (self.enemies.level/0.5)%2 == 1:
                            self.enemies.level += 0.5
                        #saves the level number when the player quits the game
                        save.save_game(self.enemies.level, "level")
                     pygame.quit()
                     sys.exit()
             pygame.display.update()
             clock.tick_busy_loop(60)
    def reset(self):
        #Resets the positions and states of everything. Said positions depend on the level number
        self.enemies.shot = False
        self.direction = "right"
        if self.enemies.level == 1:
            for i in range(1, 15):
                self.laser_ys[i] = 625
            for i in range(0, 6):
                self.enemies.horde_y[i] = 20
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
            for i in range(0, 15):
                self.enemies.laserxs[i] = self.enemies.horde_x[i] + 22.5
        if 1.5 <= self.enemies.level <=2:
            self.shot = False            
            self.status = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]  
            for i in range(14, 26):
                self.enemies.horde_x[i] = -400000000000
            for i in range(0, 4):
                self.enemies.horde_y[i] = 20
                self.enemies.horde_x[i] = 350 + (60*i)
            for i in range(4, 8):
                self.enemies.horde_y[i] = 80
                self.enemies.horde_x[i] = 350 + (60*(i-4))
            for i in range(8, 11):
                self.enemies.horde_y[i] =140
                self.enemies.horde_x[i] = 150 + 50 + (60*(i-8))
            for i in range(11, 14):
                self.enemies.horde_y[i] =140
                self.enemies.horde_x[i] = 450 + 50 + 60 + (60*(i-11))
            for i in range(0, 14):
                self.enemies.laserxs[i] = self.enemies.horde_x[i] + 22.5 
        if 2.5 <= self.enemies.level <= 3:  
            self.status = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]  
            self.shot = False
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
            for i in range(0, 14):
                self.enemies.laserxs[i] = self.enemies.horde_x[i] + 22.5
            for i in range(0, 14):
                self.laser_ys[i] = 625
            self.h0 = 3
            self.h1 = 3
            self.h7 = 3
            self.h8 = 3
        if 3.5  <= self.enemies.level <= 4:
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
                for i in range(0, 14):
                    self.enemies.laserxs[i] = self.enemies.horde_x[i] + 22.5
                for i in range(0, 14):
                    self.laser_ys[i] = 625
        if self.enemies.level == 0:
            standard = 80
            self.enemies.score = 0
            self.h0 =3
            self.h1 =3
            self.h7 =3
            self.h8 =3
            self.shot = False
            for i in range(0, 13):
                self.enemies.horde_y[i] =  70
                self.enemies.list_line1.append(self.enemies.horde_y[i])
            for i in range(13, 26):
                self.enemies.horde_y[i] = 120
                self.enemies.list_line2.append(self.enemies.horde_y[i])
            for i in range(0, 13):
                self.enemies.horde_x[i] = standard
                standard += 60
            for i in range(13, 26):
                self.enemies.horde_x[i] = self.enemies.horde_x[i - 13]
            for i in range(0, 26):
                self.enemies.laserxs[i] = self.enemies.horde_x[i] +22.5
        self.player.x = 435
        self.projectile.ys[self.projectile.num] = -25
        pygame.mixer.music.play(-1)
        self.enemies.status = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        self.count = 0
        self.player.health = 5 
    #This method is where almost everything is called for the game to actually happen. It itself is called at the end of the main while loop
    def play(self):
        self.player.draw_shooter()
        self.player.draw_health()
        #Enemy shooting for all levels other than endless mode
        if self.enemies.shot:
            a = random.randint(1, 100)
            l = 100
            for i in range(0, 14):
                if i == 9:
                    if self.enemies.level == 1:
                        continue
                    else:
                        pass
                if i == 13:
                    if self.enemies.level == 1:
                        continue
                    else:
                        pass
                if a == i + 1:
                    if self.enemies.laserxs[i] - l <= self.player.x <= self.enemies.laserxs[i] + l:
                        self.enemies.downs[i] = True
                if self.enemies.downs[i] :
                    if self.laser_ys[i] == self.enemies.horde_y[i] + 30:
                        pygame.mixer.Sound.play(laser1)
                    if self.laser_ys[i] >= 625:
                        self.enemies.downs[i] = False

            if self.enemies.level == 0:
                for i in range(0, 13):
                    if a == i + 1:
                        if self.enemies.laserxs[i] - l <= self.player.x <= self.enemies.laserxs[i] + l:
                            self.enemies.downs[i] = True
                    if self.enemies.downs[i]:
                        if self.laser_ys[i] == self.enemies.horde_y[i] + 30:
                            pygame.mixer.Sound.play(laser1)
                        if self.laser_ys[i] >= 625:
                            self.enemies.downs[i] = False
                for i in range(13, 26):
                    if a == i + 1:
                        if self.enemies.laserxs[i] - l <= self.player.x <= self.enemies.laserxs[i] + l:
                            self.enemies.downs[i] = True
                    if self.enemies.downs[i]:
                        if self.laser_ys[i] == self.enemies.horde_y[i] + 30:
                            pygame.mixer.Sound.play(laser1)
                        if self.laser_ys[i] >= 625:
                            self.enemies.downs[i] = False
            #Drawing enemy projectiles on the screen if their moving
            for i in range(0, 26):
                if self.enemies.downs[i]:
                    self.screen.blit(self.blast, (self.enemies.laserxs[i], self.laser_ys[i]))
                if not self.enemies.downs[i] :
                    self.laser_ys[i] = self.enemies.horde_y[i] + 30
                    self.enemies.laserxs[i] = self.enemies.horde_x[i] + 22.5
        #Drawing player projectile if it is moving
        if self.up:
            self.projectile.draw_projectile()
            if self.projectile.ys[self.projectile.num] > -25:
                self.projectile.ys[self.projectile.num] -= self.projectile_speed
        if self.projectile.num >= 9:
            self.projectile.num = 0
        #Contrary to what the name suggests, this method is how the posisitons of all things are decided in each level
        self.enemies.level1()
        if self.projectile.ys[self.projectile.num] <= -25:
            self.up = False
            #self.projectile.four += self.backup
            if self.projectile.num < self.projectile.num + 1:
                self.projectile.num += 1
                self.projectile.ys[self.projectile.num - 1] = 520
        self.enemies.level1()
        if self.player.health == 0:
            if self.enemies.level == 0:
                if not save_highscore.check_file("highscore"):
                    save_highscore.save_game(self.enemies.score, "highscore")
                if save_highscore.check_file("highscore"):
                    r= int(save_highscore.load("highscore"))
                    if self.enemies.score > r:
                        save_highscore.save_game(self.enemies.score, "highscore")
        if self.player.health == 0:
            raise GameOver
        #Level 1 enemy blast on player collision
        if 1 == 1:
                for i in range(0, 13):
                    if i == 9:
                        continue
                    if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserxs[i], self.laser_ys[i]):
                        self.player.health -= 1
                        self.laser_ys[i] = 625
                pygame.display.update()
        if self.enemies.level == 1:
                #Enemy fire on barrier collision
                for i in range(0,13):
                    if i ==9:
                        continue
                    if self.red_white_collision(200, 300, self.enemies.laserxs[i], self.laser_ys[i], 90):
                        self.laser_ys[i] = 625
                        pygame.mixer.Sound.play(white_barrier)
                for i in range(0,13):
                    if i ==9:
                        continue
                    if self.red_white_collision(650, 300, self.enemies.laserxs[i], self.laser_ys[i], 90):
                        self.laser_ys[i] = 625
                        pygame.mixer.Sound.play(white_barrier)
                #Player fire on barrier collision
                if self.blue_light_collision(200, 300, 435 + self.projectile.difference, self.projectile.ys[self.projectile.num], 90):
                    self.projectile.ys[self.projectile.num] = -25
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))

                if self.blue_light_collision(650, 300, 435 + self.projectile.difference, self.projectile.ys[self.projectile.num], 90):
                    self.projectile.ys[self.projectile.num] = -25
                    pygame.mixer.Sound.play(pygame.mixer.Sound(resource_path("white barrier.wav")))
                #Level 1 Player fire on enemy hitboxes
                for i in range(0, 13):
                    if i ==9:
                        continue
                    if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num], self.enemies.horde_x[i], self.enemies.horde_y[i]):
                        self.enemies.horde_y[i] = 1000
                        self.enemies.horde_x[i] = -3999
                        self.enemies.status[i] = False
                        self.projectile.ys[self.projectile.num] = -26
                        pygame.mixer.Sound.play(explosion)
                #Promotion from level one to intermission screen
                value = False
                self.count = 0
                for f in [self.enemies.status[0], self.enemies.status[1], self.enemies.status[2], self.enemies.status[3], self.enemies.status[4], self.enemies.status[5], self.enemies.status[6], self.enemies.status[7], self.enemies.status[8], self.enemies.status[10], self.enemies.status[11], self.enemies.status[12]]:

                    if not f:
                        self.count += 1
                if self.count == 12:
                    self.reset()
                    self.enemies.level += 0.5
                    self.reset()
                    self.count = 0
                    self.player.health = 5
        if self.enemies.level == 2:
            for i in range(0, 14):
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],self.enemies.horde_x[i], self.enemies.horde_y[i]):
                    self.enemies.horde_y[i] = 1000
                    self.enemies.status[i] = False
                    self.enemies.horde_x[i] = -399900
                    self.projectile.ys[self.projectile.num] = -26
                    pygame.mixer.Sound.play(explosion)
            if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserxs[9], self.laser_ys[9]):
                self.player.health -= 1
                self.col = False
                self.laser_ys[9] = 625
                pygame.mixer.Sound.play(hit)
            if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserxs[13], self.laser_ys[13]):
                self.player.health -= 1
                self.col = False
                self.laser_ys[13] = 625
            
            self.count = 0
            for f in [self.enemies.status[0], self.enemies.status[1], self.enemies.status[2], self.enemies.status[3],
                      self.enemies.status[4], self.enemies.status[5], self.enemies.status[6], self.enemies.status[7],
                      self.enemies.status[8],self.enemies.status[9], self.enemies.status[10], self.enemies.status[11],
                      self.enemies.status[12],  self.enemies.status[13]]:
                if not f:
                    self.count += 1
                if self.count == 14:
                    self.reset()
                    self.enemies.level += 0.5
                    self.reset()
                    self.count = 0
                    self.player.health = 5
        if self.enemies.level == 3:
            #Collision for the enemy fire and the white barrier
            for i in range(0,14):
                if self.red_white_collision(550, 250, self.enemies.laserxs[i], self.laser_ys[i], 120):
                        self.laser_ys[i] = 625
                        pygame.mixer.Sound.play(white_barrier)
            #Collision for enemies tand the white barrier
            if self.blue_light_collision(100, 250, 435 + self.projectile.difference,self.projectile.ys[self.projectile.num], 150 ):
                self.projectile.ys[self.projectile.num] = -25
            #Collision for enemies and the green barrier (which enenmy fire intentionally does not collide with)
            if self.blue_light_collision(550, 250, 435 + self.projectile.difference,self.projectile.ys[self.projectile.num], 120): 
                self.projectile.ys[self.projectile.num] = -25
            #Collision for enemy projectiles that did not exist in the previous level
            if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserxs[9], self.laser_ys[9]):
                self.player.health -= 1
                self.col = False
                self.laser_ys[9] = 625
                pygame.mixer.Sound.play(hit)
            if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserxs[13], self.laser_ys[13]):
                self.player.health -= 1
                self.col = False
                self.laser_ys[13] = 625
                pygame.mixer.Sound.play(hit)
            pygame.display.update()
            self.count = 0
            for f in [self.enemies.status[0], self.enemies.status[1], self.enemies.status[2], self.enemies.status[3],
                      self.enemies.status[4], self.enemies.status[5], self.enemies.status[6], self.enemies.status[7],
                      self.enemies.status[8],self.enemies.status[9], self.enemies.status[10], self.enemies.status[11],
                      self.enemies.status[12],  self.enemies.status[13]]:
                if not f:
                    self.count += 1
                if self.count == 14:
                    self.reset()
                    self.enemies.level += 0.5
                    self.reset()
                    self.count = 0
                    self.player.health = 5
            #Player fire on enemy collision
            for i in range(0, 14):
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[i], self.enemies.horde_y[i]):
                    if i ==0:
                        #Subtracting from enenmy health upon collison. For enemies that have health that is. This is repeated a couple of times with different coordinates
                        if self.h0 == 1:
                            self.h0 -= 1
                            self.enemies.horde_y[i] = 1000
                            self.enemies.horde_x[i] = -399900
                            self.enemies.status[i] = False
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(explosion)
                        if self.h0 > 1:
                            self.h0 -= 1
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(hurt)
                    elif i ==1:
                        if self.h1 == 1:
                            self.h1 -= 1
                            self.enemies.horde_y[i] = 1000
                            self.enemies.horde_x[i] = -399900
                            self.enemies.status[i] = False
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(explosion)
                        if self.h1 > 1:
                            self.h1 -= 1
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(hurt)
                    elif i ==7:
                        if self.h7 == 1:
                            self.h7 -= 1
                            self.enemies.horde_y[i] = 1000
                            self.enemies.horde_x[i] = -399900
                            self.enemies.status[i] = False
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(explosion)
                        if self.h7 > 1:
                            self.h7 -= 1
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(hurt)
                    elif i ==8:
                        if self.h8 == 1:
                            self.h8 -= 1
                            self.enemies.horde_y[i] = 1000
                            self.enemies.horde_x[i] = -399900
                            self.enemies.status[i] = False
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(explosion)
                        if self.h8 > 1:
                            self.h8 -= 1
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(hurt)
                    else:
                        self.enemies.horde_y[i] = 1000
                        self.enemies.status[i] = False
                        self.enemies.horde_x[i] = -399900
                        self.projectile.ys[self.projectile.num] = -26
                        pygame.mixer.Sound.play(explosion)
            pygame.display.update()
            #level promotion once more
            value = False
            self.count = 0
            for f in [self.enemies.status[0], self.enemies.status[1], self.enemies.status[2], self.enemies.status[3],
                      self.enemies.status[4], self.enemies.status[5], self.enemies.status[6], self.enemies.status[7],
                      self.enemies.status[8],self.enemies.status[9], self.enemies.status[10], self.enemies.status[11],
                      self.enemies.status[12],  self.enemies.status[13]]:
                if not f:
                    self.count += 1
                if self.count == 14:
                    self.reset()
                    self.enemies.level += 0.5
                    self.reset()
                    self.count = 0
                    self.player.health = 5

        if self.enemies.level == 4:
            #Collision with barriers and enemies that did not exist in level 1
            if self.blue_light_collision(0, 150, 435 + self.projectile.difference, self.projectile.ys[self.projectile.num], 200):
                    self.projectile.ys[self.projectile.num] = -25
                    pygame.mixer.Sound.play(white_barrier)
            if self.blue_light_collision(700, 150, 435 + self.projectile.difference, self.projectile.ys[self.projectile.num], 200):
                    self.projectile.ys[self.projectile.num] = -25
                    pygame.mixer.Sound.play(white_barrier)
            if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserxs[9], self.laser_ys[9]):
                self.player.health -= 1
                self.col = False
                self.laser_ys[9] = 625
                pygame.mixer.Sound.play(hit)
            if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserxs[13], self.laser_ys[13]):
                self.player.health -= 1
                self.col = False
                self.laser_ys[13] = 625
                pygame.mixer.Sound.play(hit)
            for i in range(0, 14):
                #Player fire on enemies collision. They include the health thing from before
                if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],
                                          self.enemies.horde_x[i], self.enemies.horde_y[i]):
                    if i ==0:
                        if self.h0 == 1:
                            self.h0 -= 1
                            self.enemies.horde_y[i] = 1000
                            self.enemies.horde_x[i] = -399900
                            self.enemies.status[i] = False
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(explosion)
                        if self.h0 > 1:
                            self.h0 -= 1
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(hurt)
                    elif i ==1:
                        if self.h1 == 1:
                            self.h1 -= 1
                            self.enemies.horde_y[i] = 1000
                            self.enemies.horde_x[i] = -399900
                            self.enemies.status[i] = False
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(explosion)
                        if self.h1 > 1:
                            self.h1 -= 1
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(hurt)
                    elif i ==7:
                        if self.h7 == 1:
                            self.h7 -= 1
                            self.enemies.horde_y[i] = 1000
                            self.enemies.horde_x[i] = -399900
                            self.enemies.status[i] = False
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(explosion)
                        if self.h7 > 1:
                            self.h7 -= 1
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(hurt)
                    elif i ==8:
                        if self.h8 == 1:
                            self.h8 -= 1
                            self.enemies.horde_y[i] = 1000
                            self.enemies.horde_x[i] = -399900
                            self.enemies.status[i] = False
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(explosion)
                        if self.h8 > 1:
                            self.h8 -= 1
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(hurt)
                    else:
                        self.enemies.horde_y[i] = 1000
                        self.enemies.status[i] = False
                        self.enemies.horde_x[i] = -399900
                        self.projectile.ys[self.projectile.num] = -26
                        pygame.mixer.Sound.play(explosion)
            #Player on portal (blue barrier) collison
            if self.blue_light_collision(660, 280, 435 + self.projectile.difference,self.projectile.ys[self.projectile.num], 60 ):
                self.projectile.ys[self.projectile.num] = 100
                self.projectile.difference = 800 - 435
            if self.blue_light_collision(220, 280, 435 + self.projectile.difference,self.projectile.ys[self.projectile.num], 60 ):
                self.projectile.ys[self.projectile.num] = 100
                self.projectile.difference = 100 - 435
            pygame.display.update()
            #Promotion from level 3. No more levels exist at the time of commenting
            value = False
            self.count = 0
            for f in [self.enemies.status[0], self.enemies.status[1], self.enemies.status[2], self.enemies.status[3],
                      self.enemies.status[4], self.enemies.status[5], self.enemies.status[6], self.enemies.status[7],
                      self.enemies.status[8],self.enemies.status[9], self.enemies.status[10], self.enemies.status[11],
                      self.enemies.status[12],  self.enemies.status[13]]:
                if not f :
                    self.count += 1
                if self.count == 14:
                    self.reset()
                    self.enemies.level += 0.5
                    self.reset()
                    self.count = 0
                    self.player.health = 5

        if self.enemies.level == 0:

                #Collisions in endless mode
                for i in range(13, 26):
                    if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserxs[i], self.laser_ys[i]):
                        self.player.health -= 1
                        self.col = False
                        self.laser_ys[i] = 625
                        pygame.mixer.Sound.play(hit)
                    if self.red_laser_collision(self.player.x, self.player.y, self.enemies.laserxs[9], self.laser_ys[9]):
                        self.player.health -= 1
                        self.col = False
                        self.laser_ys[9] = 625
                        pygame.mixer.Sound.play(hit)
                    
                for i in range(0, 26):
                    if self.alien_laser_collision(435 + self.projectile.difference, self.projectile.ys[self.projectile.num],self.enemies.horde_x[i], self.enemies.horde_y[i]):
                        if i ==0:
                            if self.h0 == 1:
                                self.h0 -= 1
                                self.enemies.horde_y[i] = 1000
                                self.enemies.horde_x[i] = -399900
                                self.enemies.line[self.enemies.horde_y[i]] = False
                                self.projectile.ys[self.projectile.num] = -26
                                pygame.mixer.Sound.play(explosion)
                                self.lst.append((self.enemies.horde_y[i]))
                                self.enemies.score +=3
                            if self.h0 > 1:
                                self.h0 -= 1
                                self.projectile.ys[self.projectile.num] = -26
                                pygame.mixer.Sound.play(hurt)
                        elif i ==1:
                            if self.h1 == 1:
                                self.h1 -= 1
                                self.enemies.horde_y[i] = 1000
                                self.enemies.horde_x[i] = -399900
                                self.enemies.line[self.enemies.horde_y[i]] = False
                                self.projectile.ys[self.projectile.num] = -26
                                pygame.mixer.Sound.play(explosion)
                                self.lst.append((self.enemies.horde_y[i]))
                                self.enemies.score +=3
                            if self.h1 > 1:
                                self.h1 -= 1
                                self.projectile.ys[self.projectile.num] = -26
                                pygame.mixer.Sound.play(hurt)
                        elif i ==7:

                            if self.h7 == 1:
                                self.h7 -= 1
                                self.enemies.horde_y[i] = 1000
                                self.enemies.horde_x[i] = -399900
                                self.enemies.score +=3
                                self.projectile.ys[self.projectile.num] = -26
                                pygame.mixer.Sound.play(explosion)
                                self.lst.append((self.enemies.horde_y[i]))
                            if self.h7 > 1:
                                self.h7 -= 1
                                self.projectile.ys[self.projectile.num] = -26
                                pygame.mixer.Sound.play(hurt)
                        elif i ==8:
                            if self.h8 == 1:
                                self.h8 -= 1
                                self.enemies.horde_y[i] = 1000
                                self.lst.append((self.enemies.horde_y[i]))
                                self.enemies.horde_x[i] = -399900
                                self.enemies.score +=3
                                self.projectile.ys[self.projectile.num] = -26
                                pygame.mixer.Sound.play(explosion)
                            if self.h8 > 1:
                                self.h8 -= 1
                                self.projectile.ys[self.projectile.num] = -26
                                pygame.mixer.Sound.play(hurt)
                        elif i <= 12:
                            self.enemies.horde_y[i] = 1000
                            self.enemies.score +=1
                            self.enemies.horde_x[i] = -399900
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(explosion)
                            self.lst.append((self.enemies.horde_y[i]))
                        else:
                            self.enemies.horde_y[i] = 1000
                            self.enemies.horde_x[i] = -399900
                            self.projectile.ys[self.projectile.num] = -26
                            pygame.mixer.Sound.play(explosion)
                            self.lst1.append((self.enemies.horde_y[i]))
                            self.enemies.score += 1
                for item in self.lst:
                    if item in self.enemies.list_line1:
                        self.enemies.list_line1.remove(item)
                for item in self.lst1:
                    if item in self.enemies.list_line2:
                        self.enemies.list_line2.remove(item)
                pygame.display.update()
                self.count = 0
                self.count2 = 0
                #Resetting system for endless mode. Its the bit that doesn't work right now



                for i in range(0,13):
                    if self.enemies.horde_y[i] in self.lst:
                        self.count += 1

                for i in range(13, 26):
                    if self.enemies.horde_y[i] in self.lst1:
                        self.count2 += 1



                if self.count == 13:
                    standard = 80
                    l = 0
                    #for i in range(13, 26):
                     #   if self.enemies.horde_y[i] in self.enemies.list_line2:
                      #      if self.enemies.horde_y[i] == 70 or self.enemies.horde_y[i] == 120:
                       #         l= self.enemies.horde_y
                        #        break
                    for i in range(0, 13):
                        self.enemies.horde_x[i] = 80 + (60 *i)
                
                    for i in range(0, 13):
                        self.enemies.horde_y[i] = 70
                        self.lst = []
                    for i in range(13, 26):
                        if self.enemies.horde_y[i]  not in self.lst1:
                                self.enemies.horde_y[i] = 120
                        else:
                            continue
                    self.h0 = 3
                    self.h1 = 3
                    self.h7 = 3
                    self.h8 = 3
                    self.count = 0

                if self.count2 == 13:
                    l = 0
                    standard1 = 80
                    for i in range(13, 26):
                        self.enemies.horde_x[i] = standard1
                        standard1 += 60
                    for i in range(13, 26):
                        self.enemies.horde_y[i] = 70
                        self.lst1 = []
                    for i in range(0, 13):
                        if self.enemies.horde_y[i]  not in self.lst:
                                self.enemies.horde_y[i] = 120
                        else:
                            continue
                    self.count2 = 0
                    

                pygame.display.update()                          
    def game_over(self):
        #Game over screen. Buttons follow the same logic as before
        over = True
        while over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #Maintaining most common framerate in gameplay to avoid any weird jolting(same is done for the pause screen)
            clock.tick_busy_loop(165)
            color = (200, 0, 0)
            color1 = (200, 0, 0)
            self.screen.fill((0,0,0))
            if self.enemies.level != 0: 
                x = 155 + 10
            else:
                x= 135
            font1 = pygame.font.SysFont("Comic Sans", 110, bold=False, italic=False)
            font2 = pygame.font.SysFont("Comic Sans", 75, bold=False, italic=False)
            if self.enemies.level != 0:
                line = font1.render("Game Over", True,(200, 0, 0))
                            

            else:
                line = font1.render(f"Highscore: {str(save_highscore.load('highscore'))}", True, (200, 0, 0))
            self.screen.blit(line, (x, sine(100, 1280, 10,60)))


            if 280 <=mouse_x <= 650 and 350 <= mouse_y <= 450:
                    color1 = (173, 216, 230)
                    if pygame.mouse.get_pressed() != (0, 0, 0):
                                pygame.mouse.set_pos(700, 450)
                                if self.enemies.level > 0:
                                    save.save_game(self.enemies.level, "level")
                                self.title()
                                over = False



            line3 = font2.render("Main Menu", True, color1)
            self.screen.blit(line3, (280, sine(100, 1280, 10, 350)))


            if 320 - 10 <= mouse_x <= 580 + 40 and 260 <= mouse_y <= 350:
                color = (173, 216, 230)
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    over = False
            line1 = font2.render("Restart?", True, (color))
            self.screen.blit(line1, (330 - 20, sine(100, 1280, 10,250)))
            pygame.display.update()
            pygame.mixer.music.stop()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
    #Methods that will be filled later for the movement of enemies
    def switch_left1(self, target, num,):
                    if self.enemies.horde_y[num] < 900:
                        if self.enemies.horde_x[num]  >= target:
                            self.direction = "left"
    def switch_right1(self, target, num):
        if self.enemies.horde_y[num] < 900:
                if self.enemies.horde_x[num] <= target:
                    self.direction = "right"
    def switch_left2(self, target, num):
            if self.enemies.horde_y[num] < 900:
                if num <7:
                    if self.enemies.horde_x[num] >= target:
                        self.direction = "left"
                if num >=7:
                    if self.enemies.horde_x[num] <= target:
                        self.direction = "left"
    def switch_right2(self, target, num):
            if self.enemies.horde_y[num] < 900:
                if num <7:
                    if self.enemies.horde_x[num] <= target:
                        self.direction = "right"
                if num >=7:
                    if self.enemies.horde_x[num] >= target:
                        self.direction = "right"
    def run(self):
        run = True
        pause = False
        while run:
            #Calculating current fps
            clock.tick_busy_loop(200)
            fps = clock.get_fps()
            #Adjusting the speeds of everything depending on current fps
            if self.up:
                if fps >0:
                    
                    self.projectile.ys[self.projectile.num] += self.projectile_speed
                    #This is an example of the aforementioned adjustment calculations. The division by current fps and multiplication by intended fps keeps the speeds of everthing constant regardless of the currnet fps
                    self.projectile.ys[self.projectile.num] -= self.projectile_speed * self.enemies.intended_fps/fps
            else:
                pass
            if fps > 0:
                #Speed of enemy movement
                speed = 1 * self.enemies.intended_fps/fps
            else:
                speed = 1
            if fps > 0:
                if self.enemies.level == 3:
                    f = (2.1 * self.enemies.intended_fps/fps)
                elif self.enemies.level == 0:
                    f = 2.9 * self.enemies.intended_fps/fps
                else:
                    f = 1.9  * self.enemies.intended_fps/fps
            else:
                #Speed of enemy projectiles
                if self.enemies.level == 3:
                    f = 2.1 
                elif self.enemies.level == 0:
                    f = 2.9 
                else:
                    f = 1.9
            for i in range(0,26):
                if self.enemies.downs[i]:
                    if self.laser_ys[i] < 625:
                                self.laser_ys[i] +=  f
                                self.enemies.laserxs[i] = self.enemies.laserxs[i]
            if self.enemies.level ==1:
                #Movement  in level 1 (to the right)
                if self.direction == "right":
                    for i in range(0, 13):
                        if i ==9:
                            continue
                        if self.enemies.status:
                            if self.enemies.downs[i]:
                                self.enemies.horde_x[i] += speed
                            if not self.enemies.downs[i]:
                                self.enemies.horde_x[i] += speed
                                self.enemies.laserxs[i] += speed
                #Switching Direction level 1 (from right to left)
                if self.direction == "right":
                    self.switch_left1(525, 0)
                    self.switch_left1(580, 1)
                    self.switch_left1(635, 2)
                    self.switch_left1(690, 3)
                    self.switch_left1(745, 4)
                    self.switch_left1(800, 5)
                    self.switch_left1(525, 6)
                    self.switch_left1(635, 7)
                    self.switch_left1(690, 8)
                    self.switch_left1(800, 10)
                    self.switch_left1(525, 11)
                    self.switch_left1(800, 12)
                #Movement  in level 1 (to the left)
                if self.direction == "left":
                    for i in range(0, 13):
                        if i ==9:
                            continue
                        if self.enemies.status:
                            if self.enemies.downs[i]:
                                self.enemies.horde_x[i] -= speed
                            if not self.enemies.downs[i]:
                                self.enemies.horde_x[i] -= speed
                                self.enemies.laserxs[i] -= speed
                #Switching directions in level 1 (from left to right)
                if self.direction == "left":
                    self.switch_right1(70, 0)
                    self.switch_right1(125, 1)
                    self.switch_right1(180, 2)
                    self.switch_right1(235, 3)
                    self.switch_right1(290, 4)
                    self.switch_right1(345, 5)
                    self.switch_right1(70, 6)
                    self.switch_right1(180, 7)
                    self.switch_right1(235, 8)
                    self.switch_right1(345, 10)
                    self.switch_right1(70, 11)
                    self.switch_right1(345, 12)
            if self.enemies.level ==2:
                for i in range(0, 4):
                    if self.enemies.horde_y[i] < 900:
                        self.enemies.horde_x[i] -= speed
                        if self.enemies.horde_x[i] <= -40:
                            self.enemies.horde_x[i] = 900
                for i in range(4, 8):
                    if self.enemies.horde_y[i] < 900:
                        self.enemies.horde_x[i] += speed
                        if self.enemies.horde_x[i] >= 900:
                            self.enemies.horde_x[i] = -40
                if self.direction == "right":
                    for i in range(8, 14):
                        if self.enemies.horde_y[i] < 900:
                            self.enemies.horde_x[i] += speed
                            #300 more
                            if i <11:
                                if self.enemies.horde_x[i] >= 450 + (60*(i-8)):
                                    self.direction = "left"
                            if i >=11:
                                if self.enemies.horde_x[i] >=750 + (60* (i - 11)):
                                    self.direction = "left"
                if self.direction == "left":
                    for i in range(8, 14):
                        if self.enemies.horde_y[i] < 900:
                            self.enemies.horde_x[i] -= speed
                            #300 more
                            if i <11:
                                if self.enemies.horde_x[i] <= 0 + (60*(i-8)):
                                    self.direction = "right"
                            if i >=11:
                                if self.enemies.horde_x[i] <=300 + (60* (i - 11)):
                                    self.direction = "right"

                            




            if self.enemies.level == 3:
                 #Movement  in level 2 (to the right)
                if self.direction == "right":
                    for i in range(0, 7):
                        if self.enemies.horde_x[i] > -5:
                            if self.enemies.downs[i]:
                                self.enemies.horde_x[i] += speed
                            if not self.enemies.downs[i]:
                                self.enemies.horde_x[i] += speed
                                self.enemies.laserxs[i] += speed
                    for i in range(7, 14):
                        if self.enemies.horde_x[i] > -5:
                            if self.enemies.downs[i]:
                                self.enemies.horde_x[i] -= speed
                            if not self.enemies.downs[i]:
                                self.enemies.horde_x[i] -= speed
                                self.enemies.laserxs[i] -= speed
                #Switching Direction1= level 2 (from right to left)
                if self.direction == "right":
                    self.switch_left2(740, 0)
                    self.switch_left2(740, 1)
                    self.switch_left2(740, 2)
                    self.switch_left2(795, 3)
                    self.switch_left2(795, 4)
                    self.switch_left2(850, 5)
                    self.switch_left2(850, 6)
                    self.switch_left2(205, 7)
                    self.switch_left2(205, 8)
                    self.switch_left2(205, 9)
                    self.switch_left2(150, 10)
                    self.switch_left2(150, 11)
                    self.switch_left2(95, 12)
                    self.switch_left2(95, 13)
                #Movement  in level 2 (to the left)
                if self.direction == "left":
                    for i in range(0, 7):
                        if self.enemies.status:
                            if self.enemies.downs[i]:
                                self.enemies.horde_x[i] -= speed
                            if not self.enemies.downs[i]:
                                self.enemies.horde_x[i] -= speed
                                self.enemies.laserxs[i] -= speed
                    for i in range(7, 14):
                        if self.enemies.status:
                            if self.enemies.downs[i]:
                                self.enemies.horde_x[i] += speed
                            if not self.enemies.downs[i]:
                                self.enemies.horde_x[i] += speed
                                self.enemies.laserxs[i] += speed
                #Switching directions in level 2 (from left to right)
                if self.direction == "left":
                    self.switch_right2(150, 0)
                    self.switch_right2(150, 1)
                    self.switch_right2(150, 2)
                    self.switch_right2(205, 3)
                    self.switch_right2(205, 4)
                    self.switch_right2(260, 5)
                    self.switch_right2(260, 6)
                    self.switch_right2(795, 7)
                    self.switch_right2(795, 8)
                    self.switch_right2(795, 9)
                    self.switch_right2(740, 10)
                    self.switch_right2(740, 11)
                    self.switch_right2(695, 12)
                    self.switch_right2(695, 13)
            if self.enemies.level == 4:
                 #Movement  in level 3 (to the right). 
                if self.direction == "right":
                    if self.enemies.horde_y[0] < 900:
                            if self.enemies.downs[0]:
                                self.enemies.horde_x[0] += speed
                            if not self.enemies.downs[0]:
                                self.enemies.horde_x[0] += speed
                                self.enemies.laserxs[0] += speed
                    if self.enemies.horde_y[1] < 900:
                        if self.enemies.horde_x[1]  > 700:
                            if self.enemies.downs[1]:
                                self.enemies.horde_x[1] -= speed
                            if not self.enemies.downs[1]:
                                self.enemies.horde_x[1] -= speed
                                self.enemies.laserxs[1] -= speed
                if self.direction2 == "right":
                    for i in range(2, 5):
                        if self.enemies.status[i]:
                                if self.enemies.downs[i]:
                                    self.enemies.horde_x[i] += speed
                                if not self.enemies.downs[i]:
                                    self.enemies.horde_x[i] += speed
                                    self.enemies.laserxs[i] += speed
                if self.direction3 == "right":
                    for i in range(5, 14):
                        if 7 <= i <= 12:
                            continue
                        if self.enemies.status[i]:
                                if self.enemies.downs[i]:
                                    self.enemies.horde_x[i] -= speed
                                if not self.enemies.downs[i]:
                                    self.enemies.horde_x[i] -= speed
                                    self.enemies.laserxs[i] -= speed
                if self.direction1 == "right":
                    for i in range(7, 13):
                        if self.enemies.status[i]:
                                if self.enemies.downs[i]:
                                    self.enemies.horde_x[i] += speed
                                if not self.enemies.downs[i]:
                                    self.enemies.horde_x[i] += speed
                                    self.enemies.laserxs[i] += speed
                #Switching Direction1= level 3 (from right to left) Due to the different direction variables, this is quite a bit more complicated than the previous ones, and could not be done with a method
                if self.direction == "right":
                    if self.enemies.status[0]:
                        if self.enemies.horde_x[0]  >= 200:
                            self.direction = "left"
                if self.direction == "right":
                    if self.enemies.status[1]:
                        if self.enemies.horde_x[1]  <= 700:
                            self.direction = "left"
                if self.direction2 == "right":
                    standard = 590
                    for i in range(2, 5):
                        if self.enemies.horde_y[i] < 900:
                            if self.enemies.horde_x[i]  >= standard:
                                self.direction2 = "left"
                        standard += 55
                if self.direction3 == "right":
                    standard = 310
                    for i in range(5, 14):
                        if 7<= i <= 12:
                            continue
                        if self.enemies.horde_y[i] < 900:
                            if self.enemies.horde_x[i] <= standard:
                                self.direction3 ="left"
                        standard -= 55
                if self.direction1 == "right":
                    if self.enemies.status[7]:
                        if self.enemies.horde_x[7]  >=575:
                            self.direction1 = "left"
                if self.direction1 == "right":
                    if self.enemies.status[8]:
                        if self.enemies.horde_x[8]  >=630:
                            self.direction1 = "left"
                if self.direction1 == "right":                    
                    standard = 490
                    for i in range(9, 13):
                        if self.enemies.horde_y[i] <900:
                            if self.enemies.horde_x[i]  >= standard:
                                self.direction1 = "left"
                        standard += 70
                #Movement  in level 3 (to the left).
                if self.direction == "left":
                    if self.enemies.status[0]:
                            if self.enemies.downs[0]:
                                self.enemies.horde_x[0] -= speed
                            if not self.enemies.downs[0]:
                                self.enemies.horde_x[0] -= speed
                                self.enemies.laserxs[0] -= speed
                    if self.enemies.status[1]:
                            if self.enemies.downs[1]:
                                self.enemies.horde_x[1] += speed
                            if not self.enemies.downs[1]:
                                self.enemies.horde_x[1] += speed
                                self.enemies.laserxs[1] += speed
                if self.direction2 == "left":
                    for i in range(2, 5):
                        if self.enemies.status[i]:
                                if self.enemies.downs[i]:
                                    self.enemies.horde_x[i] -= speed
                                if not self.enemies.downs[i]:
                                    self.enemies.horde_x[i] -= speed
                                    self.enemies.laserxs[i] -= speed
                if self.direction3 == "left":
                    for i in range(5, 14):
                        if 7 <= i <= 12:
                            continue
                        if self.enemies.status[i]:
                                if self.enemies.downs[i]:
                                    self.enemies.horde_x[i] += speed
                                if not self.enemies.downs[i]:
                                    self.enemies.horde_x[i] += speed
                                    self.enemies.laserxs[i] += speed
                if self.direction1 == "left":
                    for i in range(7, 13):
                        if self.enemies.status[i]:
                                if self.enemies.downs[i]:
                                    self.enemies.horde_x[i] -= speed
                                if not self.enemies.downs[i]:
                                    self.enemies.horde_x[i] -= speed
                                    self.enemies.laserxs[i] -= speed
                #Switching directions in level 3 (from left to right) Also complicated because of the direction variables
                if self.direction == "left":
                    if self.enemies.horde_y[0] <900:
                        if self.enemies.horde_x[0] <= 40:
                            self.direction = "right"
                    if self.enemies.horde_y[1]:
                        if self.enemies.horde_x[1] >= 860:
                            self.direction = "right"
                if self.direction2 == "left":
                    standard_left = 150
                    for i in range(2, 5):
                        if self.enemies.horde_y[i] <900:
                            if self.enemies.horde_x[i] <= standard_left:
                                self.direction2 = "right"
                        standard_left += 55
                if self.direction3 == "left":
                    standard_left = 745
                    for i in range(5, 14):
                        if 7 <= i <= 12:
                            continue
                        if self.enemies.horde_y[i] < 900:
                            if self.enemies.horde_x[i] >= standard_left:
                                self.direction3 = "right"
                        standard_left -= 55
                if self.direction1 == "left":
                    standard_left = 250
                    for i in range(9, 13):
                        if self.enemies.horde_y[i] < 900:
                            if self.enemies.horde_x[i] <= standard_left:
                                self.direction1 = "right"
                        standard_left += 70
                    if self.enemies.horde_x[7] <= 335:
                        if self.enemies.horde_y[7] <900:
                            self.direction1 = "right"
                    if self.enemies.horde_x[8] <=390:
                        if self.enemies.horde_y[8] <900:
                            self.direction1 = "right"
            
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT:
                    #Saving level when the game quits
                    run = False
                    if (self.enemies.level/0.5)%2:
                            self.enemies.level += 0.5
                            save.save_game(self.enemies.level, "level")
                    if self.enemies.level != 0:
                        save.save_game(self.enemies.level, "level")
                    if self.enemies.level == 0:
                        if not save_highscore.check_file("highscore"):
                            save_highscore.save_game(self.enemies.score, "highscore")
                        if save_highscore.check_file("highscore"):
                            r= int(save_highscore.load("highscore"))
                            if self.enemies.score > r:
                                save_highscore.save_game(self.enemies.score, "highscore")
                pygame.key.set_repeat(1, 1)
                #Controls of the game
                if event.type == KEYDOWN:
                    if  (self.enemies.level/0.5)% 2 == 0:   
                        if event.key == K_a or event.key == K_LEFT or event.key == CONTROLLER_BUTTON_DPAD_LEFT:
                            if not keys[K_SPACE]:
                                self.enemies.shot = True
                                if self.player.x <= 0:
                                    if not self.up:
                                        self.projectile.difference = 850 - 435
                                        self.player.x = 850
                                    if self.up:
                                        self.player.x = 850
                                else:
                                    if not self.up:
                                        self.projectile.difference -= 1

                                        self.player.x -= 1
                                    if self.up:
                                        self.player.x -= 1
                                        self.backup -= 1
                        if event.key == K_d or event.key == K_RIGHT or event.key == CONTROLLER_BUTTON_DPAD_RIGHT:
                            if not keys[K_SPACE]:
                                self.enemies.shot= True
                                if self.player.x >= 830:
                                    if not self.up:
                                        self.projectile.difference = 0 - 435
                                        self.player.x = 0
                                    if self.up:
                                        self.player.x = 0
                                else:
                                    if not self.up:
                                        self.projectile.difference += 1
                                        self.player.x += 1
                                    if self.up:
                                        self.player.x += 1
                                        self.backup += 1
                        if event.key == K_SPACE or CONTROLLER_BUTTON_A:
                            self.enemies.shot = True
                            if not self.up:
                                pygame.mixer.Sound.play(laser)
                                self.projectile.difference = self.player.x - self.projectile.four + 25
                            self.up = True
                        if keys[K_d] and keys[K_SPACE] or keys[K_RIGHT] and keys[K_SPACE]:
                                self.enemies.shot= True
                                if self.player.x >= 830:
                                    if not self.up:
                                        self.projectile.difference = 0 - 435
                                        self.player.x = 0
                                        pygame.mixer.Sound.play(laser)
                                        self.projectile.difference = self.player.x - self.projectile.four + 25
                                        self.up = True
                                    if self.up:
                                        self.player.x = 0
                                else:
                                    if not self.up:
                                        self.projectile.difference += 1
                                        self.player.x += 1
                                        pygame.mixer.Sound.play(laser)
                                        self.projectile.difference = self.player.x - self.projectile.four + 25
                                        self.up = True
                                    if self.up:
                                        self.player.x += 1
                                        self.backup += 1
                        if keys[K_SPACE] and keys[K_a] or keys[K_SPACE] and keys[K_LEFT]:
                                self.enemies.shot = True
                                if self.player.x <= 0:
                                    if not self.up:
                                        self.projectile.difference = 850 - 435
                                        self.player.x = 850
                                        pygame.mixer.Sound.play(laser)
                                        self.projectile.difference = self.player.x - self.projectile.four + 25
                                        self.up = True
                                    if self.up:
                                        self.player.x = 850
                                else: 
                                    if not self.up:
                                        self.projectile.difference -= 1
                                        pygame.mixer.Sound.play(laser)
                                        self.projectile.difference = self.player.x - self.projectile.four + 25
                                        self.up = True
                                        self.player.x -= 1
                                    if self.up:
                                        self.player.x -= 1
                                        self.backup -= 1
                if event.type == KEYUP:
                        if event.key == K_ESCAPE:
                            pygame.key.set_repeat(1, 1)
                            pause = True
            
            while pause:
                clock.tick_busy_loop(165)
                #Pause screen while loop
                y = sine(100, 1280, 0,10)
                font1 = pygame.font.SysFont("Comic Sans", 50, bold=False, italic=False)
                line = font1.render("Paused", True, (255, 255, 255))
                self.screen.blit(line, (700 - 65, y))
                color = 255, 255, 255
                font8 = pygame.font.SysFont("Comic Sans", 50, bold=False, italic=False)
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 630 <= mouse_x <= 900 and 80 <= mouse_y <= 180:
                    color = (173, 216, 230)
                    if pygame.mouse.get_pressed() != (0,0,0):

                        if self.enemies.level != 0:
                            save.save_game(self.enemies.level, "level")
                        else:
                            save_highscore.save_game(self.enemies.score, "highscore")
                        self.reset()
                        pause = False
                        self.title()

                line0 = font8.render("Main Menu", True, color)
                self.screen.blit(line0, (630, 80))
                pygame.display.update()
                for event in pygame.event.get():
                        pygame.key.set_repeat(1, 1)
                        if event.type == KEYUP:
                            if event.key == K_ESCAPE:
                                pause = False
                        if event.type == QUIT:
                            if (self.enemies.level/0.5)%2 == 1:
                                self.enemies.level += 0.5
                            if self.enemies.level != 0:
                                save.save_game(self.enemies.level, "level")
                            pygame.quit()
                            sys.exit()
            # The previously mentioned Try/ except statement at the end of the while loop. The exception is meant to catch the game over and nothing else
            try:
                    self.play()
                    pygame.display.update()
            except Exception as e:
               if self.player.health <= 0: 
                    self.game_over()
                    self.reset()
                    self.player.health = 5
if __name__ == '__main__':
    game = Game()
    #Calling the loop for the title screen
    game.title()
    #Calling the main loop of the game
    game.run()