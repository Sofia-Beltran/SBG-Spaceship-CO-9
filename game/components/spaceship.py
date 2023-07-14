import pygame
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite): 
    X_POS = (SCREEN_HEIGHT // 2) + 200
    Y_POS = 500
                                                         #dimensiones
    def __init__(self): #inicializamos todo  #imagen    #ancho  #alto
        self.image = pygame.transform.scale(SPACESHIP, (60, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
    
    def update(self, user_input): #El estado de nuestro objeto
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input [pygame.K_DOWN]:
            self.move_down()
        elif user_input [pygame.K_UP]:
            self.move_up()

         
    def move_left(self): #izquierda
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH
        self.rect.x -= 10

    def move_right(self): #derecha
        if self.rect.right > SCREEN_WIDTH:
                self.rect.x = 0
        self.rect.x += 10

    def move_down(self): #abajo    
        if self.rect.bottom < SCREEN_HEIGHT:       #abajo se incrementa y arriba se disminuye.
            self.rect.y += 10
                
    def move_up(self): #arriba    
        if self.rect.top > SCREEN_HEIGHT //2:
            self.rect.y -= 10

    def draw(self, screen): #Ayudar a dibujar el avion 
        screen.blit(self.image, (self.rect.x, self.rect.y))