import pygame
width = 900
height = 400

start_x = 100
start_y = 272
speed = 3
clock = pygame.time.Clock()

background = pygame.image.load('data/background1.jpg')
background = pygame.transform.scale(background, (width, height))
player_img = pygame.image.load('data/player.png')


pack_L = []
packL = [pygame.image.load('data/playerL.png'), pygame.image.load('data/playerL1.png'),
         pygame.image.load('data/playerL2.png'), pygame.image.load('data/playerL3.png')]
for img in packL:
    img = pygame.transform.scale(img, (50, 80))
    pack_L.append(img)

pack_R = []
packR = [pygame.image.load('data/player.png'), pygame.image.load('data/player1.png'),
         pygame.image.load('data/player2.png'), pygame.image.load('data/player3.png')]
for imgR in packR:
    imgR = pygame.transform.scale(imgR, (50, 80))
    pack_R.append(imgR)