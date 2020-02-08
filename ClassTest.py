import pygame
pygame.init()

class enemy():
    def __init__(self, image, width, height, speed, x=650, y=50):
        self.image = image
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.status = True

    def enemy_move(self):
        if self.status:
            self.x -= self.speed
        elif not(self.status):
            self.x += self.speed

        if self.x == 710:
            self.status = True
        elif self.x == 0:
            self.status = False


class health():
    def __init__(self, health=100):
        self.health = health

    def minus_health(self, minus=1):
        if self.health > 0:
            self.health -= minus
        return self.health

class Hero():
    """Стандартные атрибуты героя"""
    def __init__(self, hero, name, speed, x, y):
        self.hero = hero
        self.name = name
        self.health = health()
        self.speed = speed
        self.x = x
        self.y = y

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.x -= self.speed
        if key[pygame.K_d]:
            self.x += self.speed
        if key[pygame.K_w]:
            self.y -= self.speed
        if key[pygame.K_s]:
            self.y += self.speed



class jenya():
    def __init__(self, ):

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

            # Тут был main_loop
            

def print_text(text, x, y, font_type = 'font1.ttf', font_color = (0,0,0), font_size = 20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(text, True, font_color)
    display.blit(text, (x, y))


run_game()


