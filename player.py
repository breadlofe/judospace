# Dustin Simpkins and Dylan G.
import pygame
import time
import jukebox
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
        self.speed_reset = speed
        self.x = x
        self.y = y
        self.r = r
        self.life = life
        self.rgb = [255, 200, 0]    # Player color is now mutable so that 'animations' can play.

        # Dash Variables
        self.combo_direction = ""
        self.time_passed = 0
        self.dash_speed = 55
        self.dash_time = 1  # second
        self.is_dashing = False

        # Block/Parry Variables
        self.blocking = False
        self.parry = False
        self.chip = 1
        self.parry_time = 0
        self.max_ptime = 0.1
        self.got_hit = False
        self.parried = False
        self.J = jukebox.Jukebox()

        #Getting Hit
        self.damage_timer = 0

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

        if press_input[pygame.K_s]:
            self.blocking = True
            # print("is_blocking")
            self.block()
            if (self.y + self.r) < 600:  # Needed so that player can block on line.
                self.y += self.player_speed * dt

        if not press_input[pygame.K_s]:
            self.blocking = False
            self.block()

        if click_input.type == pygame.KEYDOWN and (self.x + self.r) < 800:
            if click_input.key == pygame.K_d:

                if self.combo_direction == "a":
                    # print("changed direction")
                    self.time_passed = 0
                self.combo_direction = "d"
                if self.time_passed == 0:
                    self.time_passed = 0.001
                elif self.time_passed < 0.5 and self.combo_direction == "d":
                    # print("double click right")
                    self.dash()
                    self.time_passed = 0

            elif click_input.key == pygame.K_a:
                if self.combo_direction == "d":     # Checks to see if other direction was already pressed.
                    # print("changed direction")
                    self.time_passed = 0
                self.combo_direction = "a"
                if self.time_passed == 0:
                    self.time_passed = 0.001
                elif self.time_passed < 0.5 and self.combo_direction == "a":
                    # print("double click left")
                    self.dash()
                    self.time_passed = 0

            elif click_input.key == pygame.K_s:
                if self.parry_time == 0:
                    self.parry_time = 0.00001

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
        clock = pygame.time.Clock()
        if self.time_passed > 0:
            self.time_passed += dt
            if self.time_passed >= 0.25:  # Time between double clicks.
                self.time_passed = 0
                # print("too late")
        if self.dash_time < 1 and self.dash_time > 0:
            self.dash_time -= dt
        elif self.dash_time <= 0:
            # print("reset")
            self.player_speed = self.speed_reset
            self.is_dashing = False

        if self.parry_time > 0:
            self.parry_time += dt
            # print(self.parry_time)
            self.parry = True
            self.block(self.parry)
            if self.parry_time >= self.max_ptime:
                # print("parry over")
                self.parry_time = 0
                self.parry = False
                self.block(self.parry)
        if self.got_hit:
            # print("ouch")
            if self.parry:
                # print("PERFECT PARRY")
                self.J.sfx("parry")
                self.parried = True
            elif self.blocking:
                self.J.sfx("block")
            else:
                self.J.sfx("p_hit")
            if not self.parried: # Checks to see if they parried, and if not then it makes the flash red
                self.rgb = (255, 0, 0)
            else: # If they did, it flashes them white
                self.rgb = (255, 255, 255)
            self.damage_timer = 200
            self.got_hit = False
        if self.is_dashing:
            self.J.sfx("dash")
            self.rgb = [255, 255, 164]


    def dash(self):
        """
        Moves player based on velocity. Increases player_speed to play nicely with walls.
        :return: None.
        """
        velocity = 900
        self.dash_time = 0.2
        # print(self.combo_direction)

        if self.dash_time > 0:
            if self.combo_direction == "d" or self.combo_direction == "a":
                # self.rgb = [0, 0, 250]
                self.player_speed += velocity
                self.is_dashing = True

    def block(self, parry=False):
        """
        Handles blocking boolean
        :return: None.
        """

        # "There was a bug that made it so blocking did nothing, so I rearranged the code so that it won't happen
        # As a result parrying also only happens while you are blocking, and it will immediatly be removed once you stop
        # blocking, regardless of timer." - DG
        if self.blocking:
            if self.parry:
                self.chip = 0
            else:
                self.chip = 0.33
            self.player_speed = self.speed_reset * 0.5
            if self.damage_timer > 0:
                self.damage_timer -= 1 # makes it so you flash red after getting hit for less than normal
            else:
                self.rgb = [140, 140, 0]
            # print("block")

        elif not self.blocking:
            # print("not block")
            self.chip = 1
            if self.damage_timer > 0:
                self.damage_timer -= 1 # Makes it so you flash red after getting hit
            elif not self.is_dashing and not self.got_hit:
                self.rgb = [255, 200, 0]  # return back to yellow if not hit or dashing.

            if not self.is_dashing and not self.got_hit:
                self.player_speed = self.speed_reset # Removes the speed debuff from blocking
