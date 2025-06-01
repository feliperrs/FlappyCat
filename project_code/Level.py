import pygame
from pygame.font import Font
from project_code.Cat import Cat
from project_code.Pipe import Pipe
from project_code.Const import C_WHITE, PIPE_WIDTH, WIN_HEIGHT, WIN_WIDTH


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
        game_over = False
        points = 0
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            clock.tick(60)
            for event in pygame.event.get():
                # checks if the user clicked the X, then closes the window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        cat.pular()

            if not game_over:
                cat.update()
                cat.draw()
                # add pipes to the pipe list
                if len(pipes_list) == 0 or pipes_list[-1].x < WIN_WIDTH - 200:
                    pipes_list.append(Pipe(WIN_WIDTH))

            # update and draws pipes
            for cano in pipes_list[:]:
                cano.update()
                cano.draw()
                if cano.x + PIPE_WIDTH < 0:
                    pipes_list.remove(cano)
                    points += 1

            for pipe in pipes_list:
                if cat.rect.colliderect(pipe.rect_top) or cat.rect.colliderect(pipe.rect_base):
                    game_over = True

            if cat.y > WIN_HEIGHT or cat.y < 0:
                game_over = True

            if game_over:
                self.write_text(50, "GAME", C_WHITE, ((WIN_WIDTH/2), 70))
                self.write_text(50, "OVER", C_WHITE, ((WIN_WIDTH/2), 120))
                self.write_text(50, "Your Score:", C_WHITE,
                                ((WIN_WIDTH/2), 170))
                self.write_text(50, f"{points}", C_WHITE, ((WIN_WIDTH/2), 220))

            pygame.display.flip()

    # function to write a text in the screen
    def write_text(self, text_size, text, text_color, text_center_pos):
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(
            text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
