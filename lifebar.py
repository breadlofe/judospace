# Dylan Gonzalez

import pygame

class Lifebar:

    def __init__(self):

        self.width = 200
        self.height = 20
        self.x = 400 - (self.width / 2)
        self.y = 600 - (self.height + 10)

        self.shown_value = 0

    def update(self, life_total):
        """
        :param life_total: int or float that represents a life total out of a maximum of 100
        """

        self.True_Value = life_total * 2

        if self.True_Value > self.shown_value:
            self.shown_value += 1
        if self.True_Value < self.shown_value:
            self.shown_value -= 1


    def draw(self, surf):
        pygame.draw.rect(surf, (0, 255, 0), (self.x, self.y, self.shown_value, self.height))
        pygame.draw.rect(surf, (255, 255, 255), (self.x, self.y, self.width, self.height), 3)