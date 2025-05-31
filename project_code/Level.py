import pygame

from project_code.Cat import Cat
from project_code.Const import WIN_HEIGHT, WIN_WIDTH


class Level:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/LevelBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Level.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        cat = Cat(self.window)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            clock.tick(60)
            cat.draw()
            for event in pygame.event.get():
                # checks if the user clicked the X, then closes the window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.flip()
