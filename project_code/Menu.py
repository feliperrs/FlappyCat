import pygame


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(
            './asset/MenuBg.png').convert_alpha()  # carrega imagem
        self.rect = self.surf.get_rect(left=0, top=0)   # cria retangulo
        
    def run(self):
        #musica do menu
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            # checks for all events
            for event in pygame.event.get():
                # checks if the user clicked the X, then closes the window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            pygame.display.flip()