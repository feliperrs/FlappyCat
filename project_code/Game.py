import pygame

from project_code.Const import WIN_HEIGHT, WIN_WIDTH


class Game:
    def __init__(self):
        # starts the window
        pygame.init()
        # sets the size of the window
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            # checks for all events
            for event in pygame.event.get():
                # checks if the user clicked the X, then closes the window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
