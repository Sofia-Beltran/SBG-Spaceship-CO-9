import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet_manager import BulletManager
from game.components.bullets.bullet_manager

from game.utils.constants import PLAYER_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite): 
    X_POS = (SCREEN_HEIGHT // 2) + 200
    Y_POS = 520
                                                         #dimensiones
    def __init__(self): #inicializamos todo  #imagen    #ancho  #alto
        self.image = pygame.transform.scale(SPACESHIP, (60, 50))
        self.type = PLAYER_TYPE
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.shooting_time = random.randint(30, 50)# Nos va ayudar controlar cuando hemos disparado la bala
    
    def update(self, user_input, bullet_manager): #El estado de nuestro objeto
        self.shoot(bullet_manager)
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
    
    def shoot(self, bullet_manager):
        BulletManager(bullet_manager)
        current_time = pygame.time.get_ticks() #reloj
        if self.shooting_time <= current_time:
           bullet_manager.add_bullet(self)
           self.shooting_time += current_time + random.randint(30, 50)

    def draw(self, screen): #Ayudar a dibujar el avion 
        screen.blit(self.image, (self.rect.x, self.rect.y))