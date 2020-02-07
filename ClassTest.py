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



width = 800
height = 600
clock = pygame.time.Clock()
display = pygame.display.set_mode((width, height))
model = Hero(pygame.image.load('avatar282060_1.gif.png'), 'Kolyadin', 1, 400, 300)
enemy = enemy(pygame.image.load('avatar282060_2_rotate2.gif.png'), 60, 80, 1)

def run_game():
    game = True
    while game:

        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        if key[pygame.K_ESCAPE]:
            quit()

        display.fill((255, 255, 255))
        display.blit(model.hero, (model.x, model.y))
        model.move()
        display.blit(enemy.image, (enemy.x, enemy.y))
        enemy.enemy_move()
        print_text(str(model.health.health), model.x + 35, model.y - 30)
        clock.tick(330)
        pygame.display.update()


def print_text(text, x, y, font_type = 'font1.ttf', font_color = (0,0,0), font_size = 20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(text, True, font_color)
    display.blit(text, (x, y))

# 124123123
# 125 1-2431203
# 02131023103120


run_game()


