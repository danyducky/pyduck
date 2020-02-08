import pygame
from Constants import *
from Player import *
pygame.init()

class main():
    def __init__(self, display):
        self.display = display
        self.player = Player('danyducky')
        self.background = pygame.image.load('background.jpg')
        self.run_game = True
        self.main_loop()

    def render(self):
        """Прорисовка всех объектов и персонажа"""
        self.display.blit(self.background, (0, 0))
        self.player.render(display)
        pygame.display.flip()

    def main_loop(self):
        """Основной цикл игры"""
        while self.run_game == True:
            self.render()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                quit()


display = pygame.display.set_mode((width, height))
game = main(display)

