import math
import pygame
from pygame.locals import *
def sine(speed: float, frequency: int, max_amplitude: float, base_line: int) -> int:
    #time since the program started fivided by the remainde of 2 and frequency
    t = pygame.time.get_ticks() / 2 % frequency
    #calculation of current y position
    y = math.sin(t / speed) * max_amplitude + base_line
    return int(y)