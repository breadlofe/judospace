import pygame
import random

class Basic_Enemy:

    def __init__(self, radius, speed, start_x, end_y):
        self.radius = radius
        self.speed = speed
        self.dodge = False
        self.x = start_x
        self.y = radius * -1
        self.end_y = end_y
        self.color = (0, 0, 255)
        self.life_value = 1


        self.dodge_x = start_x + self.radius
        #self.dodge_y




    def update(self, dt):

        if self.dodge == False:
            if self.end_y > self.y:
                self.y += self.speed * dt
            else:
                self.dodge = True
        elif self.dodge == True:
            if self.dodge_x >= 400:
                if self.x <= self.dodge_x:
                    self.x += self.speed * dt
                else:
                    self.dodge_x = 400 - (self.dodge_x - 400)


            elif self.dodge_x < 400:
                if self.x >= self.dodge_x:
                    self.x -= self.speed * dt
                else:
                    self.dodge_x = abs(self.dodge_x - 400) + 400


            # The current idea is self.dodge is to have the object move in a sin and cos manner to evade attacks

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (self.x, self.y), self.radius)


class Control_AI:

    def __init__(self):
        self.AI_List = []

    def add_basic_enemy(self, radius, speed, start_x):
        temp_end = random.randint(100, 300)
        bad_guy = Basic_Enemy(radius, speed, start_x, temp_end)
        self.AI_List.append(bad_guy)

    def update(self, dt):
        for i in self.AI_List:
            i.update(dt)
            if i.life_value == 0:
                self.AI_List.remove(i)

    def draw(self, surf):
        for i in self.AI_List:
            i.draw(surf)