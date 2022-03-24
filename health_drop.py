# Dustin Simpkins
import pygame
import math
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
        self.amp = 5
        self.cspeed = 0.1

    def spawn(self, radius, hit_point, heal_amount):
        """
        Takes spawn position, hit point, amount it heals, and radius into the local variable list.
        :param radius: int representing radius of circle.
        :param hit_point: int representing how much item needs to be shot to drop health item.
        :param heal_amount: int representing how much health item replenishes.
        :return: None, but appends to health_drop_list.
        """
        spawn_x = 0 - radius
        spawn_y = random.randint(170, 400)
        position = [spawn_x, spawn_y]
        can_get = False
        color = (0,210,0)
        self.health_drop_list.append([position, hit_point, heal_amount, radius, spawn_y, can_get, color])

    def update(self, dt):
        """
        Updates position of health object
        :param dt: delta_time.
        :return: None.
        """
        for h in self.health_drop_list:
            if h[1] != 0:
                h[0][0] += 50 * dt
                h[0][1] = self.amp * math.sin(h[0][0] * self.cspeed) + h[4]
            else:
                h[5] = True

    def draw(self, surf):
        """
        Draws health item onto given surf.
        :param surf: Given pygame surf.
        :return: None, but draws circle.
        """
        for i in range(len(self.health_drop_list)):
            pygame.draw.circle(surf, [-i][6], (self.health_drop_list[-i][0][0], self.health_drop_list[-i][0][1]),
                               self.health_drop_list[-i][3])

