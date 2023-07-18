import random
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy2 import Enemy2

class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self):                                  
        if not self.enemies: # len (self.enemies) == 0 #[] {} 0 "" -->False # [1] {1: 1} 1 -2 "asdf" --> True   
            choose_method = random.choice([Enemy, Enemy2])
            self.enemies.append(choose_method())   
                
        for enemy in self.enemies:
            enemy.update(self.enemies)


    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

        for enemy2 in self.enemies:
            enemy2.draw(screen)
    
        
            

            



        