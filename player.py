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
        self.combo_state = False
        self.combo_direction = ""
        self.time_passed = 0
        self.clicks = 0

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

        if click_input.type == pygame.KEYDOWN and (self.x + self.r) < 800:
            if click_input.key == pygame.K_d:
                if self.combo_state:
                    self.clicks = 2
                    self.time_passed = 0
                else:
                    self.clicks = 1
                print("clicked")
                self.combo_state = True
                self.combo_direction = "d"

        if press_input[pygame.K_w] and (self.y - self.r) > 0:
            self.y -= self.player_speed * dt

        if press_input[pygame.K_s] and (self.y + self.r) < 600:
            self.y += self.player_speed * dt

        if click_input == pygame.KEYDOWN:
            pass

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
        if self.combo_state and self.combo_direction == "d" and self.clicks == 1:
            self.time_passed += dt
            if self.clicks == 2 and self.time_passed <= 0.1:
                print("dash")
                self.combo_state = False
                self.time_passed = 0
                self.clicks = 0

            elif self.time_passed > 0.1:
                self.clicks = 0
                self.combo_state = False
                self.time_passed = 0
            print(self.time_passed)
            print(self.clicks)
