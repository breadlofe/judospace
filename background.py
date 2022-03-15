import random
import pygame

class Star :

    def __init__(self, screen_w):
        self.y = 0
        self.x = random.randint(0, screen_w)
        self.speed = 200    # Pixels per Second
        self.color = (255, 255, 0)
        self.radius = 1

    def update(self, dt, screen_w, screen_h):
        self.y += self.speed * dt

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (self.x, self.y), self.radius)

class Space :

    def __init__(self):
        self.star_list = []



    def draw(self):
        for i in self.star_list:
            pass
