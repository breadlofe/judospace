import pygame
import random
import matrix
import vector
import shape_matrix as sm

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

# Below is the Boss Body and the Boss Hand class

class Boss_Body:

    def __init__(self, start_x, radius):
        self.radius = radius
        self.Dog_Tag = "Boss Body"
        self.x = start_x
        self.y = self.radius * -1
        self.end_y = 100
        self.speed = 300
        self.aggression = 5
        self.x_vel = 0
        self.y_vel = 0
        self.life_value = 500
        self.color = (75, 250, 186)
        self.direction = 1

        self.dodge = False

    def update(self, dt):
        if self.end_y > self.y and not self.dodge:
            self.y += self.speed * dt
        else:
            self.dodge = True

        # Self.direction = 1 (Going Right) and Self.direction = -1 (Going Left)
        # self.direction = -1

        if self.dodge:
            if self.direction == 1:
                if self.x < 700:
                    self.x += self.speed * dt
                else:
                    self.direction = -1
            if self.direction == -1:
                if self.x > 100:
                    self.x -= self.speed * dt
                else:
                    self.direction = 1



    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (self.x, self.y), self.radius)


class Boss_Arms:

    def __init__(self, tag, start_x, start_y, life_value):
        """"
        :param tag: Determines which hand this instance is
        :param start_x: Int or float representing x-position of middle tip of triangle:
        2*----*3
        \    /
         \ /
          1*  <--- this one (order of points in shape matrix indicated by number as well).
        :param start_y: Int or float representing y-position of point highlighted above.
        :param life_value: Int or float representing life value of each arm.
        """
        self.Dog_Tag = tag
        self.proj_radius = 5
        self.x_r = start_x
        self.y_r = start_y
        self.x_l = start_x + 400
        self.y_l = start_y  # Is redundant for now, but wll come in handy once triangles start to rotate.
        self.x_change = 100  # How much the other points are offset from the first point.
        self.y_change = 150
        self.life_r = life_value
        self.life_l = life_value
        self.rgb_r = [255, 0, 0]
        self.rgb_l = [255, 0, 0]  # Same thing here. Will come in handy in the future.
        self.right_arm = matrix.Matrix(vector.Vector(self.x_r, self.y_r),
                                       vector.Vector(self.x_r - self.x_change, self.y_r - self.y_change),
                                       vector.Vector(self.x_r + self.x_change, self.y_r - self.y_change))
        self.right_arm_bounder = self.right_arm + matrix.Matrix(vector.Vector(self.proj_radius, self.proj_radius),
                                                                vector.Vector(self.proj_radius, self.proj_radius),
                                                                vector.Vector(self.proj_radius, self.proj_radius))
        self.left_arm = matrix.Matrix(vector.Vector(self.x_l, self.y_l),
                                      vector.Vector(self.x_l - self.x_change, self.y_l - self.y_change),
                                      vector.Vector(self.x_l + self.x_change, self.y_l - self.y_change))
        self.left_arm_bounder = self.left_arm + matrix.Matrix(vector.Vector(self.proj_radius, self.proj_radius),
                                                              vector.Vector(self.proj_radius, self.proj_radius),
                                                              vector.Vector(self.proj_radius, self.proj_radius))
        # NOTE: The right arm bounder creates hit-triangle for arm that accounts for projectile radius.

    def draw_right(self, surf):
        """
        Draws the right boss arm on to given surface.
        :param surf: Pygame.Surface
        :return: None
        """
        pygame.draw.polygon(surf, self.rgb_r, sm.convert(self.right_arm))

    def draw_left(self, surf):
        """
        Draws the left boss arm on to given surface
        :param surf: Pygame.Surface
        :return: None
        """
        pygame.draw.polygon(surf, self.rgb_l, sm.convert(self.left_arm))




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

    def spawn_boss(self):
        radius = 50
        start_x = 450 - radius
        boss_body = Boss_Body(start_x, radius)
        self.AI_List.append(boss_body)

    def update(self, dt):
        for i in self.AI_List:
            i.update(dt)
            if i.life_value <= 0:
                self.AI_List.remove(i)

    def draw(self, surf):
        for i in self.AI_List:
            i.draw(surf)