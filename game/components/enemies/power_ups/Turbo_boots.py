import pygame
from game.components.enemies.power_ups.power_up import PowerUp
from game.utils.constants import TURBO, TURBO_TYPE, SPACESHIP_TURBO

class TurboBoots(PowerUp):
    def __init__(self):
        super().__init__(TURBO, TURBO_TYPE, SPACESHIP_TURBO)
        self.spaceship_image = SPACESHIP_TURBO
        
        
        

