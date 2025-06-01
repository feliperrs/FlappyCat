import pygame

from project_code.Cat import Cat
from project_code.Pipe import Pipe
from project_code.Const import PIPE_WIDTH, WIN_HEIGHT, WIN_WIDTH


class Level:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/LevelBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Level.mp3')
        pygame.mixer_music.set_volume(0.15)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        cat = Cat(self.window)
        pipes_list = []
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            clock.tick(60)
            cat.draw()
            cat.update()
            for event in pygame.event.get():
                # checks if the user clicked the X, then closes the window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        cat.pular()
                        
            # add pipes to the pipe list
            if len(pipes_list) == 0 or pipes_list[-1].x < WIN_WIDTH - 200:
                pipes_list.append(Pipe(WIN_WIDTH))

            # update and draws pipes
            for cano in pipes_list[:]:
                cano.update()
                cano.draw()
                if cano.x + PIPE_WIDTH < 0:
                    pipes_list.remove(cano)
                    # pontos += 1

            pygame.display.flip()
