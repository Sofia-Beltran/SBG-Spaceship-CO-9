from game.components.enemies.enemy2 import Enemy2

class EnemyManager2:
    def __init__(self):
        self.enemies = []

    def update(self):                                  
        if not self.enemies: # len (self.enemies) == 0 #[] {} 0 "" -->False # [1] {1: 1} 1 -2 "asdf" --> True   
            self.enemies.append(Enemy2())          

        for enemy2 in self.enemies:
            enemy2.update(self.enemies)


    def draw(self, screen):
        for enemy2 in self.enemies:
            enemy2.draw(screen)
             
        
