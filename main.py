# Judo Space Main
# March 15, 2022
# Dustin, Dylan, and Zach



import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Dylan, you can change if you want.
finished = False


class Projectile:
    def __init__(self, start_x, start_y):
        self.position = [start_x, start_y]
        self.bullet_list = []

    def update(self, dt):
        pass

    def draw(self, x, y):
        pass
#while not finished: