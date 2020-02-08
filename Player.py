import pygame
from Constants import *

class Player():
    def __init__(self):
        self.x = start_x
        self.y = start_y
        self.image = player

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.x -= speed
        if key[pygame.K_d]:
            self.x += speed
        if key[pygame.K_s]:
            self.y += speed
        if key[pygame.K_w]:
            self.y -= speed

    def direction(self, screen):
        mouse = pygame.mouse.get_pos()
        if mouse[0] < self.x:
             screen.blit(playerL, (self.x, self.y))