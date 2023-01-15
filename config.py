import pygame
import time
import math
from pygame import mixer

pygame.init()
height = 800
width = 800
player1x = 368
player2x = 368
player1y = 768
player2y = 58
score1m = 0
score1g = 0
dead1 = 0
dead2 = 0
score1 = 0
score2 = 0
score2m = 0
score2g = 0
scoreg = [5, 5, 10, 5, 10, 10]
player1xchange = 0
player1ychange = 0
player2xchange = 0
player2ychange = 0
invert = 0
roundx = 2
rnd = 0
mercedesx = [0, 653, 376, 188, 440, 564, 288]
mercedesy = [109, 209, 309, 409, 509, 609, 709]
mercedesc1 = 0.35
mercedesc2 = 0.35
gasx = [528, 13, 241, 56, 344, 524, 350, 677, 251]
gasy = [159, 259, 359, 359, 459, 559, 559, 659, 659]
mercedeschange = [0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35]
blue = [0, 170, 250]
tm1 = 0
tm2 = 0
tm = 0
font = pygame.font.Font('freesansbold.ttf', 32)
black = [0, 0, 0]
green = [0, 255, 100]
beige = [245, 245, 220]
brown = [177, 34, 34]
white = [255, 255, 255]
tesla = pygame.image.load("./media/tesla.png")
teslax = pygame.image.load("./media/teslax.png")
mercedes = pygame.image.load("./media/mercedes.png")
gas = pygame.image.load("./media/gas.png")
size = (width, height)
gameoverx = font.render("gameover bois!\n", True, white, black)
gameoverrect = gameoverx.get_rect()
gameoverrect.center = (width // 2, height // 2)