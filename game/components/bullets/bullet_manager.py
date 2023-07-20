from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, PLAYER_TYPE, SHIELD_TYPE


class BulletManager:
    def __init__(self):
        self.enemy_bullets = []
        self.bullets = []
        

    def update(self, game):
        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    game.score += 1
                 

        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)
            if enemy_bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(enemy_bullet)
                if game.player.power_up_type != SHIELD_TYPE:  
                    game.playing = False
                    game.death_count += 1 
                

        for player_bullet in self.bullets:
            player_bullet.update(self.bullets)

    def draw(self, screen):
        for enemy_bullet in self.enemy_bullets + self.bullets: #combino las listas
            enemy_bullet.draw(screen)
        
        for player_bullet in self.bullets:
            player_bullet.draw(screen)

    def add_bullet(self, spaceschip):
        if spaceschip.type == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(Bullet(spaceschip))
            
        if spaceschip.type == PLAYER_TYPE:
            self.bullets.append(Bullet(spaceschip))

   