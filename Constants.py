import pygame
width = 700
height = 600

start_x = 100
start_y = 100
speed = 1

background = pygame.image.load('data/background.jpg')
player = pygame.image.load('data/player.png')
player = pygame.transform.scale(player, (50, 80))
playerL = pygame.image.load('data/playerL.png')
playerL = pygame.transform.scale(playerL, (50, 80))

