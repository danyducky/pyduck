import pygame
from Constants import *


class Main():
    """Основной класс"""
    def __init__(self, screen):
        self.screen = screen
        self.run_game = True
        self.x = start_x
        self.y = start_y
        self.background = pygame.image.load(background)
        self.main_loop()

    def render(self):
        """Прорисовка всего-всего"""
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()


    def main_loop(self):
        """Основной цикл игры"""
        while self.run_game == True:
            self.render() # пока идёт игра - будем прорисовывать все объекты из метода render
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_game = False
                if event.type == pygame.K_ESCAPE:
                    self.run_game = False






pygame.init()
screen = pygame.display.set_mode((width, height))
game = Main(screen)