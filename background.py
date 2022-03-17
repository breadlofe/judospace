import random
import pygame

class Star :

    def __init__(self, screen_w, speed):
        self.y = 0
        self.x = random.randint(0, screen_w)
        self.speed = speed    # Pixels per Second
        self.color = (255, 255, 0)
        self.radius = 1

    def update(self, dt):
        self.y += self.speed * dt

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (self.x, self.y), self.radius)

class Space :

    def __init__(self, Star_Rate, Speed):
        self.star_list = []
        self.add_rate = 0
        self.star_rate = Star_Rate
        self.speed = Speed

    def update(self, dt, screen_w, screen_h):
        for i in self.star_list:
            i.update(dt)
            if i.y >= screen_h:
                self.star_list.remove(i)

        self.add_rate += 1
        if self.add_rate >= self.star_rate:
            new_star = Star(screen_w, self.speed)
            self.star_list.append(new_star)
            self.add_rate = 0

    def draw(self, surf):
        for i in range(len(self.star_list)):
            self.star_list[i].draw(surf)