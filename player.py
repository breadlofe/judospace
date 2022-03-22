# Dustin Simpkins and Dylan G.
import pygame
pygame.init()

class Player:
    """
    Handles player position and drawing player on screen as well as inputs.
    """
    def __init__(self, x, y, r, life):
        """
        Takes x and y values as well as radius and player life point values from main.
        :param x: int or float representing player x-position
        :param y: int or float representing player y-position
        :param r: int representing player radius
        :param life: int or float representing player life points
        """
        self.x = x
        self.y = y
        self.r = r
        self.life = life