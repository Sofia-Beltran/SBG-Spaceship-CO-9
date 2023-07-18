import pygame
import random


from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, ENEMY_TYPE, SCREEN_WIDTH

LEFT = "left"
RIGHT = "right"


class Enemy(Sprite):
                  #var        #var       #rango  #dese 50 hasta el ancho de mi pantalla
    X_POS_LIST = [x_pos for x_pos in range(50, SCREEN_WIDTH, 50)] #50 ultimo es mi contador que va en cincuenta
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 3


    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_1, (50, 50))
        self.type = ENEMY_TYPE
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement = random.choice([LEFT, RIGHT])
        self.move_x = random.randint(30, 50)
        self.moving_index = 0

        self.shooting_time = random.randint(30, 50)# Nos va ayudar controlar cuando hemos disparado la bala

    def update(self, enemies, bullet_manager):
        self.rect.y += self.speed_y
        self.shoot(bullet_manager)
        if self.movement == RIGHT:
            self.rect.x += self.speed_x
        else:
            self.rect.x -= self.speed_x

        self.update_movement()
        if self.rect.y >= SCREEN_WIDTH:
            enemies.remove(self)

    def update_movement(self):
        self.moving_index += 1
        if self.rect.right >= SCREEN_WIDTH:
            self.movement = LEFT
        elif self.rect.y <= 0:
            self.movement = RIGHT
        
        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if self.movement == RIGHT else RIGHT

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks() #reloj
        if self.shooting_time <= current_time:
           bullet_manager.add_bullet(self)
           self.shooting_time += current_time + random.randint(30, 50)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

