import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy2(Sprite):
    X_POS_LIST = [x_pos for x_pos in range(50, SCREEN_WIDTH, 100)] 
    Y_POS_LIST = [y_pos for y_pos in range(-100, 200, 30)]
    SPEED_X = 4
    SPEED_Y = 4
    

    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_2, (40, 40))
        self.type = ENEMY_TYPE
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
         
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y

        self.shooting_time = random.randint(30, 50)# Nos va ayudar controlar cuando hemos disparado la bala    
    
    def update(self, enemies, bullet_manager):
        self.rect.y += self.speed_y
        self.shoot(bullet_manager)    
        if self.rect.y >= SCREEN_HEIGHT:  # Verificar si el avión ha pasado el límite inferior
            #self.rect.y = random.choice(self.Y_POS_LIST) 
            enemies.remove(self)
        
        if self.rect.x > 0:
            self.rect.x -= self.speed_x
            

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks() #reloj
        if self.shooting_time <= current_time:
           bullet_manager.add_bullet(self)
           self.shooting_time += current_time + random.randint(30, 50)    

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
       