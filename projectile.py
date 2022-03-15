import pygame

pygame.init()

class Projectile:
    def __init__(self, start_x, start_y):
        self.position = [start_x, start_y]
        self.bullet_list = []

    def update(self, dt):
        pass

    def draw(self, x, y):
        pass
