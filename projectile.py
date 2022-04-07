# Dustin Simpkins
import pygame


pygame.init()

class Projectile:
    """
    When player hits specified button, said class activates and appends bullet to position that then moves upward.
    """

    def __init__(self):
        """
        Creates bullet list and sounds.
        """
        self.bullet_list = []
        self.shoot_sound = pygame.mixer.Sound('sound//player_shoot.ogg')

    def spawn(self, start_x, start_y, lifespan):
        """
        Creates position variable and appends said position to bullet list.
        :param start_x: int or float of x-value that bullet spawns at.
        :param start_y: int or float of y-value that bullet spawns at.
        :param lifespan: int or float of bullets lifespan in seconds.
        :return: None
        """
        position = [start_x, start_y]
        self.bullet_list.append([position, lifespan])
        pygame.mixer.Sound.play(self.shoot_sound)

    def update(self, dt, surf, color):
        """
        Updates y-value of bullet positively, and ticks down on lifespan.
        :param dt: int or float of delta time.
        :param surf: surface that bullet is drawn on.
        :param color: tuple representing color (R, G, B).
        :return: None
        """
        for b in self.bullet_list:
            b[0][1] = b[0][1] - 500 * dt
            b[1] = b[1] - (1 * dt)
            if b[1] <= 0:
                self.bullet_list.remove(b)


    def draw(self, surf, color):
        """
        Draws bullet onto specified surface.
        :param surf: surface that bullet is drawn on.
        :param color: tuple representing color (R, G, B).
        :return: None
        """
        for i in range(len(self.bullet_list)):
            bullet = pygame.draw.circle(surf, color, (self.bullet_list[-i][0][0], self.bullet_list[-i][0][1]), 5)

class Enemy_Projectile:
    """
    Same as projectile, but the y-value goes down to reflect that enemies come from above.
    """
    def __init__(self):
        """
        Creates bullet list.
        """
        self.bullet_list = []
        self.shoot_sound = pygame.mixer.Sound('sound//enemy_shoot.ogg')

    def spawn(self, start_x, start_y, lifespan):
        """
        Creates position variable and appends said position to bullet list.
        :param start_x: int or float of x-value that bullet spawns at.
        :param start_y: int or float of y-value that bullet spawns at.
        :param lifespan: int or float of bullets lifespan in seconds.
        :return: None
        """
        position = [start_x, start_y]
        self.bullet_list.append([position, lifespan])
        pygame.mixer.Sound.play(self.shoot_sound)

    def update(self, dt, surf, color):
        """
        Updates y-value of bullet positively, and ticks down on lifespan.
        :param dt: int or float of delta time.
        :param surf: surface that bullet is drawn on.
        :param color: tuple representing color (R, G, B).
        :return: None
        """
        for b in self.bullet_list:
            b[0][1] = b[0][1] + 500 * dt
            b[1] = b[1] - (1 * dt)
            if b[1] <= 0:
                self.bullet_list.remove(b)


    def draw(self, surf, color):
        """
        Draws bullet onto specified surface.
        :param surf: surface that bullet is drawn on.
        :param color: tuple representing color (R, G, B).
        :return: None
        """
        for i in range(len(self.bullet_list)):
            bullet = pygame.draw.circle(surf, color, (self.bullet_list[-i][0][0], self.bullet_list[-i][0][1]), 5)
            
class Tracker_Projectile:
    
    def __init__(self):
        self.bullet_list = []
        self.angle = 270
        
    def spawn(self, start_x, start_y, lifespan, hv, vv):
        position = [start_x, start_y]
        h_vel = hv
        v_vel = vv
        velocity = [h_vel, v_vel]
        self.bullet_list.append([position, lifespan, velocity])
        
    def update(self, dt):


        for b in self.bullet_list:
            b[0][0] += b[2][0] * dt
            b[0][1] += b[2][1] * dt
            b[1] -= (1 * dt)
            print(b[1])
            if b[1] <= 0:
                self.bullet_list.remove(b)

    def draw(self, surf, color):
        for i in self.bullet_list:
            pygame.draw.circle(surf, color, (i[0][0], i[0][1]), 5)