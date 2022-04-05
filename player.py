# Dustin Simpkins and Dylan G.
import pygame
pygame.init()

class Player:
    """
    Handles player position and drawing player on screen as well as inputs.
    """
    def __init__(self, x, y, r, life, speed):
        """
        Takes x and y values as well as radius and player life point values from main.
        :param x: int or float representing player x-position
        :param y: int or float representing player y-position
        :param r: int representing player radius
        :param life: int or float representing player life points
        :param speed: int or float representing the speed of the player
        """

        self.player_speed = speed
        self.x = x
        self.y = y
        self.r = r
        self.life = life
        self.rgb = [255, 200, 0]    # Player color is now mutable so that 'animations' can play.
        self.combo_direction = ""
        self.time_passed = 0
        self.dash_speed = 55

    def handle_input(self, press_input, click_input, dt):
        """
        Takes inputs from main and responds to them
        :param press_input: Takes a pygame key press in order to handle different events
        :param click_input: Takes an event.poll in order to handle different events
        :param dt: represents delta_time
        """
        if press_input[pygame.K_a] and (self.x - self.r) > 0:
            self.x -= self.player_speed * dt

        if press_input[pygame.K_d] and (self.x + self.r) < 800:
            self.x += self.player_speed * dt

        if press_input[pygame.K_w] and (self.y - self.r) > 0:
            self.y -= self.player_speed * dt

        if press_input[pygame.K_s] and (self.y + self.r) < 600:
            self.y += self.player_speed * dt

        if click_input.type == pygame.KEYDOWN and (self.x + self.r) < 800:
            if click_input.key == pygame.K_d:
                self.combo_direction = "d"
                if self.time_passed == 0:
                    self.time_passed = 0.001
                elif self.time_passed < 0.5 and self.combo_direction == "d":
                    print("double click right")
                    self.time_passed = 0
            elif click_input.key == pygame.K_a:
                self.combo_direction = "a"
                if self.time_passed == 0:
                    self.time_passed = 0.001
                elif self.time_passed < 0.5 and self.combo_direction == "a":
                    print("double click left")
                    self.time_passed = 0

    def draw(self, surf):
        """
        Draws player on surface as circle.
        :param surf: surface.
        :return: None.
        """
        pygame.draw.circle(surf, self.rgb, (self.x, self.y), self.r)

    def update(self, dt):
        """
        Updates player information primarily to see if player double-clicks.
        :param dt: delta_time.
        :return: None.
        """
        if self.time_passed > 0:
            self.time_passed += dt
            if self.time_passed >= 0.5:
                self.time_passed = 0
                print("too late")
