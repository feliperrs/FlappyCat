import pygame

from project_code.Level import Level
from project_code.Menu import Menu
from project_code.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH


class Game:
    def __init__(self):
        # starts the window
        pygame.init()
        # sets the size of the window
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()    # get the menu choice
            level = Level()

            # starts the game
            if menu_return == MENU_OPTION[0]:
                level.run()

            # quit the game
            else:
                pygame.quit()
                quit()
