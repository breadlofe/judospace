# Dustin Simpkins
import pygame
import random

class Health:
    """
    Creates health drop that randomly spawns and travels horizontally. Can be collected by player.
    """
    def __init__(self):
        """
        Sets start values for health drop that can be picked up by player to regain life.
        """
        self.health_drop_list = []
        self.spawn_x = 0
        self.spawn_y = 0

    def spawn(self):
        pass
