import pygame
from Constants import *

class player():
    def __init__(self):
        self.x = start_x
        self.y = start_y
        self.leftImage = pack_L
        self.rightImage = pack_R
        self.afkImage = player_img
        self.counter_L = 0
        self.counter_R = 0


    def move(self, screen):
        """Перемещение влево/вправо и анимация движения персонажа"""
        """Ограничение выхода за пределы окна"""
        key = pygame.key.get_pressed()
        if key[pygame.K_d] == 0 and key[pygame.K_a] == 0:
            screen.blit(self.afkImage, (self.x, self.y))
        if key[pygame.K_a] == 1:
            self.x -= speed
            self.counter_L += 1
            screen.blit(self.leftImage[self.counter_L // 3], (self.x, self.y))
            if self.counter_L == 9:
                self.counter_L = 0
        if key[pygame.K_d]:
            self.x += speed
            self.counter_R += 1
            screen.blit(self.rightImage[self.counter_R // 3], (self.x, self.y))
            if self.counter_R == 9:
                self.counter_R = 0

        if self.x <= 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
        if self.x >= width - 50:
            self.x = width - 50
        if self.y >= height - 80:
            self.y = height - 80

