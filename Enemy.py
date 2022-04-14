import pygame
import random

class Basic_Enemy:

    def __init__(self, radius, speed, start_x, end_y):
        self.radius = radius
        self.speed = speed
        self.x = start_x
        self.y = radius * -1
        self.end_y = end_y
        self.color = (0, 0, 255)
        self.life_value = 1
        self.aggression = 3
        self.dodge = False
        self.dodge_x = start_x + self.radius
        self.dodge_y = end_y
        self.y_dodge_value = random.randint(30, 70)

        self.Dog_Tag = "Basic"

    def update(self, dt):

        # all 400s are repr esentative of the equation (SCREEN_W / 2)
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

            if self.dodge_y == self.end_y:
                if self.y > self.dodge_y:
                    self.y -= (self.speed / 2) * dt
                else:
                    self.dodge_y += self.y_dodge_value
            else:
                if self.y <= self.dodge_y:
                    self.y += (self.speed / 2) * dt
                else:
                    self.dodge_y = self.end_y


            # The current idea is self.dodge is to have the object move in a sin and cos manner to evade attacks

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (self.x, self.y), self.radius)

    def gethurt(self):
        pass

class Tracker_Enemy:

    def __init__(self, radius, start_x, lv, end_y, name_tag, color):
        self.radius = radius
        self.speed = 75
        self.x = start_x
        self.y = radius * -1
        self.life_value = lv
        self.end_y = end_y
        self.color = color
        self.aggression = 5
        self.gattling_track = 0
        self.Dog_Tag = name_tag

        # Dodge in this context is just a name convention for when the 'Tracker' has reached the end of its spawn start
        self.dodge = False

    def update(self, dt):
        if self.end_y > self.y:
            self.y += self.speed * dt
        else:
            self.dodge = True

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (self.x, self.y), self.radius)

class Control_AI:

    def __init__(self):
        self.AI_List = []

    def add_basic_enemy(self, radius, speed, start_x):
        temp_end = random.randint(100, 300)
        bad_guy = Basic_Enemy(radius, speed, start_x, temp_end)
        self.AI_List.append(bad_guy)

    def add_tracker(self, radius, start_x, lv):
        temp_end = random.randint(50, 150)
        color = (255, 150, 0)
        bad_guy = Tracker_Enemy(radius, start_x, lv, temp_end, "Tracker", color)
        self.AI_List.append(bad_guy)

    def add_elite(self, radius, start_x, lv):
        temp_end = random.randint(50, 150)
        color = (82, 0, 0)
        bad_guy = Tracker_Enemy(radius, start_x, lv, temp_end, "Elite", color)
        self.AI_List.append(bad_guy)

    def update(self, dt):
        for i in self.AI_List:
            i.update(dt)
            if i.life_value <= 0:
                self.AI_List.remove(i)

    def draw(self, surf):
        for i in self.AI_List:
            i.draw(surf)