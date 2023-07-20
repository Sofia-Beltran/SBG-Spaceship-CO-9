import random
import pygame
from pygame.sprite import Sprite
import game
from game.utils.constants import DEFAULT_TYPE, PLAYER_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite): 
    X_POS = (SCREEN_HEIGHT // 2) + 200
    Y_POS = 520
                                                         #dimensiones
    def __init__(self): #inicializamos todo  #imagen    #ancho  #alto
        self.type = PLAYER_TYPE
        self.image = pygame.transform.scale(SPACESHIP, (60, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.power_up_type = DEFAULT_TYPE
        self .power_up_time_up = 0
        self.shooting_time = random.randint(30, 50)# Nos va ayudar controlar cuando hemos disparado la bala
    
    def update(self, user_input, bullet_manager): #El estado de nuestro objeto
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input [pygame.K_DOWN]:
            self.move_down()
        elif user_input [pygame.K_UP]:
            self.move_up()
        if user_input [pygame.K_SPACE]:
            self.shoot(bullet_manager)
         
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
        bullet_manager.add_bullet(self)
           

    def draw(self, screen): #Ayudar a dibujar el avion 
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def on_pick_power_up(self, time_up, type, image):
        self.image = pygame.transform.scale(image, (60, 50))  
        self.power_up_time_up = time_up
        self.power_up_type = type

    def draw_power_up(self, game):
        if self.power_up_type != DEFAULT_TYPE:
            time_left = round(self.power_up_time_up - pygame.time.get_ticks() / 1000, 2)
            if time_left >= 0:
                game.menu.draw(game.screen, f"{self.power_up_type.capitalize()} is enabled for {time_left} seconds", y=5, color=(255, 255, 255))
            else: 
                self.power_up_type = DEFAULT_TYPE
                self.image = pygame.transform.scale(SPACESHIP, (60, 50))