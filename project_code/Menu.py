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
            self.menu_text(50, "FLAPPY", C_WHITE, ((WIN_WIDTH/2), 70))
            self.menu_text(50, "CAT", C_WHITE, ((WIN_WIDTH/2), 120))
            self.menu_text(13, "Felipe Ribeiro Rodrigues dos Santos - RU: 4695260", C_WHITE, (200, 10))

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
                # checks if a key was pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    # returns the player choice
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

            pygame.display.flip()

    # function to write a text in the screen
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(
            text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
