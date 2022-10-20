import pygame
import sys
import time
import random

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

class Player:

    playerSpeed = 1
    
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


    
player = Player()

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

    screen.blit(surface, (0,0))

    pygame.display.flip()
    pygame.display.update()

    


