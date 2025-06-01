import pygame
from pygame.font import Font
from project_code.Cat import Cat
from project_code.Menu import Menu
from project_code.Pipe import Pipe
from project_code.Const import C_WHITE, PIPE_WIDTH, WIN_HEIGHT, WIN_WIDTH,C_RED, C_YELLOW


class Level:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/LevelBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.reset_game()
        
        
    def reset_game(self):
        self.pipes_list = []
        self.game_over = False
        self.points = 0
        self.cat = Cat(self.window)
        pygame.mixer_music.load('./asset/Level.mp3')
        pygame.mixer_music.set_volume(0.15)
        pygame.mixer_music.play(-1)
        
    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            for event in pygame.event.get():
                # checks if the user clicked the X, then closes the window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.game_over:
                            self.cat.pular()
                        if self.game_over:
                            self.reset_game()

            if not self.game_over:
                self.cat.update()
                self.cat.draw()
                # add pipes to the pipe list
                if len(self.pipes_list) == 0 or self.pipes_list[-1].x < WIN_WIDTH - 200:
                    self.pipes_list.append(Pipe(WIN_WIDTH))

                 # update and draws pipes
                for cano in self.pipes_list[:]:
                    cano.update()
                    cano.draw()
                    if cano.x + PIPE_WIDTH < 0:
                        self.pipes_list.remove(cano)
                        self.points += 1

            for pipe in self.pipes_list:
                if self.cat.rect.colliderect(pipe.rect_top) or self.cat.rect.colliderect(pipe.rect_base):
                    self.game_over = True

            if self.cat.y > WIN_HEIGHT or self.cat.y < 0:
                self.game_over = True

            if self.game_over:
                self.write_text(50, "GAME", C_RED, ((WIN_WIDTH/2), 20))
                self.write_text(50, "OVER", C_RED, ((WIN_WIDTH/2), 70))
                self.write_text(40, "SCORE:", C_YELLOW,
                                ((WIN_WIDTH/2), 140))
                self.write_text(40, f"{self.points}", C_YELLOW, ((WIN_WIDTH/2), 190))
                self.write_text(30, "PRESS 'SPACE' TO PLAY AGAIN", C_YELLOW, ((WIN_WIDTH/2), 240))
                
            pygame.display.update()
            clock.tick(60)
    # function to write a text in the screen
    def write_text(self, text_size, text, text_color, text_center_pos):
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(
            text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
