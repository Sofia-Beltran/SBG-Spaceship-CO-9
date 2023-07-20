from game.components.enemies.power_ups.power_up import PowerUp
from game.utils.constants import SHIELD, SHIELD_TYPE, SPACESHIP_SHIELD


class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE, SPACESHIP_SHIELD)
        self.spaceship_image = SPACESHIP_SHIELD
        