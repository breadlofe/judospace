import pygame

pygame.init()

class Projectile:

    def __init__(self):
        self.bullet_list = []

    def spawn(self, start_x, start_y, lifespan):
        position = [start_x, start_y]
        self.bullet_list.append([position, lifespan])

    def update(self, dt, surf, color):
        for i in range(len(self.bullet_list) - 1, -1, -1):
            print(self.bullet_list[i][0][1])
            self.bullet_list[i][0][1] = self.bullet_list[i][0][1] - 50 * dt
            self.bullet_list[i][1] = self.bullet_list[i][1] - (1 * dt)
            if self.bullet_list[i][1] <= 0:
                print("not")
                self.bullet_list.pop(i)
                print("is")


    def draw(self, surf, color):
        for i in range(len(self.bullet_list)):
            bullet = pygame.draw.circle(surf, color, (self.bullet_list[-i][0][0], self.bullet_list[-i][0][1]), 5)
