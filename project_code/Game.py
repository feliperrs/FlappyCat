import pygame

from project_code.Menu import Menu
from project_code.Const import WIN_HEIGHT, WIN_WIDTH


class Game:
    def __init__(self):
        # starts the window
        pygame.init()
        # sets the size of the window
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()

