import pygame
from pygame.font import Font

from project_code.Const import C_WHITE, C_YELLOW, MENU_OPTION, WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(
            './asset/MenuBg.png').convert_alpha()  # carrega imagem
        self.rect = self.surf.get_rect(left=0, top=0)   # cria retangulo

    def run(self):
        # starts the menu option
        menu_option = 0
        # menu music
        pygame.mixer_music.load('./asset/Menu.wav')
        # turn the volume down
        pygame.mixer_music.set_volume(0.3)
        # plays it in a loop
        pygame.mixer_music.play(-1)
        while True:
            # draws the backgound
            self.window.blit(source=self.surf, dest=self.rect)

            # writes Flappy Cat
            self.menu_text(50, "Flappy", C_WHITE, ((WIN_WIDTH/2), 70))
            self.menu_text(50, "Cat", C_WHITE, ((WIN_WIDTH/2), 120))

            # menu selection
            for i in range(len(MENU_OPTION)):
                # change the color when a option is selected
                if i == menu_option:
                    self.menu_text(
                        20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH/2), 200+35*i))
                else:
                    self.menu_text(
                        20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH/2), 200+35*i))

            # checks for all events
            for event in pygame.event.get():
                # checks if the user clicked the X, then closes the window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.flip()

    # function to write a text in the screen
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(
            text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
