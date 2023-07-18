
import pygame
from game.components import spaceship
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, PLAYER_TYPE


class BulletManager:
    def __init__(self):
        self.enemy_bullets = []
        self.player_bullets = []

    def update(self):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)

        for player_bullet in self.player_bullets:
            player_bullet.update(self.player_bullets)

    def draw(self, screen):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(screen)
        
        for player_bullet in self.player_bullets:
            player_bullet.draw(screen)

    def add_bullet(self, spaceschip):
        if spaceschip.type == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(Bullet(spaceschip))
            
        if spaceschip.type == PLAYER_TYPE:
            self.player_bullets.append(Bullet(spaceschip))

    def key_bullet(self, event):    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Llamar al método add_bullet para el jugador
                self.add_bullet(spaceship)