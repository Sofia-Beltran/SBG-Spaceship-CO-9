import pygame

from game.utils.constants import FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDHT = SCREEN_WIDTH // 2

    def __init__(self, message):
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.icon = pygame.transform.scale(ICON, (120, 80))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDHT, self.HALF_SCREEN_HEIGHT -100)
        self.update_message(message)

    def events(self, on_close, on_star):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               on_close() #cuando quieras cerrar el juego me avisas
            elif event.type == pygame.KEYDOWN:
                on_star() # simepre lleva el on por delante

    def draw(self, screen):
        screen.fill((255, 51, 134)) #color como rosado o morado RGB
        screen.blit(self.text, self.text_rect)
        screen.blit(self.icon, self.icon_rect)
        pygame.display.flip()#va actualizar la pantalla o update
        

    def update_message(self, message):
        self.message = message
        self.text = self.font.render(self.message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDHT, self.HALF_SCREEN_HEIGHT)
    