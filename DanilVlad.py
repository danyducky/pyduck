import pygame
import random

pygame.init()

width = 1600
height = 900
display = pygame.display.set_mode((width, height), flags=pygame.FULLSCREEN)

clock = pygame.time.Clock()


class Card():
    def __init__(self, image1, image2, x, y):
        self.image1 = image1
        self.image2 = image2
        self.x = x
        self.y = y

    def card_open(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 0:c
            display.blit(self.image2, (self.x, self.y))
        if self.x < mouse[0] < self.x + 180:
            if self.y < mouse[1] < self.y + 252:
                if click[0] == 1:
                    display.blit(self.image1, (self.x, self.y))

 #       def move(self):
  #          mouse = pygame.mouse.get_pos()
   #         click = pygame.mouse.get_pressed()
    #        if self.x < mouse[0] < self.x + 130:
     #           if self.y < mouse[1] < self.y + 202:
      #              if click[0] == 1:
       #                 self.x = 750
        #                self.y = 260

behind = pygame.image.load('behind.jpg')
behind = pygame.transform.scale(behind, (180, 252))

Ten1 = Card(pygame.image.load('first.png'), behind, 300, 200)
Ten2 = Card(pygame.image.load('first.png'), behind, 500, 200)
eight1 = Card(pygame.image.load('second.png'), behind, 300, 550)
eight2 = Card(pygame.image.load('second.png'), behind, 500, 550)
A1 = Card(pygame.image.load('three.png'), behind, 900, 550)
A2 = Card(pygame.image.load('three.png'), behind, 1100, 550)



def run_game():
    game = True

    while game:
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            quit()

        display.fill((50, 0, 120))

        Ten1.card_open()
        Ten2.card_open()
        eight1.card_open()
        eight2.card_open()
        A1.card_open()
        A2.card_open()
        clock.tick(60)
        pygame.display.flip()




run_game()
