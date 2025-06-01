import random

import pygame

from project_code.Const import PIPE_DIST, PIPE_SPEED,WIN_WIDTH, WIN_HEIGHT, C_GREEN


class Pipe:
    def __init__(self, x):
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) 
        self.x = x
        self.altura_topo = random.randint(50, WIN_HEIGHT - PIPE_DIST - 50)
        self.largura = 60
        self.rect_topo = pygame.Rect(self.x, 0, self.largura, self.altura_topo)
        self.rect_base = pygame.Rect(self.x, self.altura_topo + PIPE_DIST, self.largura, WIN_HEIGHT)

    def atualizar(self):
        self.x -= PIPE_SPEED
        self.rect_topo.x = self.x
        self.rect_base.x = self.x

    def desenhar(self):
        pygame.draw.rect(self.window, C_GREEN, self.rect_topo)
        pygame.draw.rect(self.window, C_GREEN, self.rect_base)