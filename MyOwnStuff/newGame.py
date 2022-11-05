import pygame
import sys
import time
import random
import math

from pygame.locals import *

size = (800, 608)
backgroundColor = (0, 0, 0)

def draw_box(surf, color, pos, size):
    r = pygame.Rect((pos[0], pos[1]), (size[0], size[1]))
    pygame.draw.rect(surf, color, r)

pygame.init()

screen = pygame.display.set_mode(size)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill(backgroundColor)
pygame.display.set_caption("Free")


screen.blit(surface, (0,0))


pygame.display.flip()

movingLeft = False
movingRight = False
movingUp = False
movingDown = False

def direction(ax, ay, bx, by):
    return math.degrees(math.atan2(ay-by, bx-ax))

def rainbowColor():
    colorValues = [255, 0, random.randint(0, 255)]
    random.shuffle(colorValues)
    return tuple(colorValues)

class Player:

    playerSpeed = 0.5
    
    def __init__(self):
        self.color = (255, 255, 255)
        self.origin = (400, 304)
        self.playerSize = (16, 16)

    def lose(self):
        self.origin = (400, 304)

    def moveDown(self):
        self.origin = (self.origin[0], self.origin[1] + self.playerSpeed)

    def moveUp(self):
        self.origin = (self.origin[0], self.origin[1] - self.playerSpeed)

    def moveRight(self):
        self.origin = (self.origin[0] + self.playerSpeed, self.origin[1])

    def moveLeft(self):
        self.origin = (self.origin[0] - self.playerSpeed, self.origin[1])

    def draw(self, surf):
        draw_box(surf, self.color, self.origin, self.playerSize)

class Bullet:

    def __init__(self, dir, spd, color, pos, size):
        self.dir = dir
        self.spd = spd
        self.color = color
        self.pos = pos
        self.size = size

    def outsideScreen(self):
        if self.pos[0] > 800 + self.size[0] or self.pos[0] < 0 - self.size[0] or self.pos[1] > 608 + self.size[1] or self.pos[1] < 0 - self.size[1]:
            return True
        return False

    def move(self):
        self.pos = (self.pos[0] + self.spd * math.cos(math.radians(self.dir)), self.pos[1] + self.spd * -math.sin(math.radians(self.dir)))

    def draw(self, surf):
        draw_box(surf, self.color, self.pos, self.size)

player = Player()

class Boss1():

    def __init__(self):
        self.bulletList = []
        self.timer = 0
        self.dt = 0

    def boss(self):
        # main
        if self.timer == 0:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            if not pygame.mixer.music.get_busy():    
                pygame.mixer.music.load(r"C:\Users\gabri\Desktop\ThirdQuarter\MyOwnStuff\btba.mp3")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play()
        elif self.timer > 0 and self.timer <= 6000 and self.timer % 120 == 0:
            speed = 0.9
            bullet1 = Bullet(random.randint(1, 89), speed, rainbowColor(), (2,606), (3,3))
            bullet2 = Bullet(random.randint(91, 179), speed, rainbowColor(), (798,606), (3,3))
            bullet3 = Bullet(random.randint(181, 269), speed, rainbowColor(), (798, 2), (3,3))
            bullet4 = Bullet(random.randint(271, 359), speed, rainbowColor(), (2, 2), (3,3))
            self.bulletList.append(bullet1)
            self.bulletList.append(bullet2)
            self.bulletList.append(bullet3)
            self.bulletList.append(bullet4)
        # details
        if self.timer >= 2790 and self.timer <= 3285 and self.timer % 30 == 0:
            bullet = Bullet(direction(400, 304, player.origin[0], player.origin[1]), 1, (255, 255, 255), (400, 304), (3,3))
            self.bulletList.append(bullet)
        if self.timer == 6100:
            self.restart()

        self.timer += 1

    def drawBoss(self, surf):
        for bullet in self.bulletList:
            bullet.move()
            if bullet.outsideScreen():
                self.bulletList.remove(bullet)
            bullet.draw(surf)
    
    def restart(self):
        pygame.mixer.music.rewind()
        for bullet in self.bulletList:
            self.bulletList.remove(bullet)
        self.timer = 0

boss = Boss1()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                movingUp = True
            elif event.key == K_DOWN:
                movingDown = True
            elif event.key == K_LEFT:
                movingLeft = True
            elif event.key == K_RIGHT:
                movingRight = True
        elif event.type == KEYUP:
            if event.key == K_UP:
                movingUp = False
            elif event.key == K_DOWN:
                movingDown = False
            elif event.key == K_LEFT:
                movingLeft = False
            elif event.key == K_RIGHT:
                movingRight = False
        
    if movingUp:
        player.moveUp()
    if movingLeft:
        player.moveLeft()
    if movingRight:
        player.moveRight()
    if movingDown:
        player.moveDown()

    
    surface.fill(backgroundColor)
    player.draw(surface)
    boss.boss()
    boss.drawBoss(surface)
        

    screen.blit(surface, (0,0))

    pygame.display.flip()
    pygame.display.update()

    


