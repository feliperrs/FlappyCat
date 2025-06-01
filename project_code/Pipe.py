import random

import pygame

from project_code.Const import PIPE_DIST, PIPE_SPEED, PIPE_WIDTH,WIN_WIDTH, WIN_HEIGHT, C_GREEN


class Pipe:
    def __init__(self, x):
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) 
        self.x = x
        self.top_height = random.randint(50, WIN_HEIGHT - PIPE_DIST - 50)
        self.rect_top = pygame.Rect(self.x, 0, PIPE_WIDTH, self.top_height)
        self.rect_base = pygame.Rect(self.x, self.top_height + PIPE_DIST, PIPE_WIDTH, WIN_HEIGHT)

    def update(self):
        self.x -= PIPE_SPEED
        self.rect_top.x = self.x
        self.rect_base.x = self.x

    def draw(self):
        pygame.draw.rect(self.window, C_GREEN, self.rect_top)
        pygame.draw.rect(self.window, C_GREEN, self.rect_base)