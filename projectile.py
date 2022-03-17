import pygame

pygame.init()

class Projectile:

    def __init__(self, start_x, start_y, lifespan):
        self.px = start_x
        self.py = start_y
        self.lifespan = lifespan
        self.position = [self.px, self.py]
        self.bullet_list = []
        self.bullet_list.append([self.position, self.lifespan])

    def update(self, dt, surf, color):
        for i in range(len(self.bullet_list)):
            draw(surf, color, self.bullet_list[-i][0][0], self.bullet_list[-i][0][1])
            self.bullet_list[-i][0][1] = self.bullet_list[-i][0][1] - 5 * dt
            self.bullet_list[-i][1] = self.bullet_list[-i][1] - (1 * dt)
            if self.bullet_list[-i][1] <= 0:
                self.bullet_list.pop(-i)


def draw(self, surf, color, x, y):
    bullet = pygame.draw.circle(surf, color, (x, y), 5)
