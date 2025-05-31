import pygame

from project_code.Const import GRAVITY, JUMP_STRENGTH, WIN_HEIGHT, WIN_WIDTH


class Cat:
    def __init__(self,window):
        self.window = window
        self.x = 50
        self.y = WIN_HEIGHT // 2
        self.surf = pygame.image.load(
            './asset/cat.png').convert_alpha()
        self.rect = self.surf.get_rect(left=self.x, top=self.y)
        self.speed = 0

    def update(self):
        self.speed += GRAVITY
        self.y += self.speed
        self.rect.centery = self.y

    def pular(self):
        self.speed = JUMP_STRENGTH
        # SOM_PULO.play()

    def draw(self):
        self.window.blit(source=self.surf, dest=self.rect)