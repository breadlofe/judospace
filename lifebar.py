# Dylan Gonzalez (everything else), Dustin Simpkins (alpha key integration)

import pygame
from Color_Dictonary import Color

class Lifebar:

    def __init__(self):

        self.width = 200
        self.height = 20
        self.x = 400 - (self.width / 2)
        self.y = 600 - (self.height + 10)
        self.rgb = (0, 255, 0)
        self.shown_value = 0

    def update(self, life_total):
        """
        :param life_total: int or float that represents a life total out of a maximum of 100
        """

        self.True_Value = life_total * 2

        if self.True_Value > self.shown_value:
            self.shown_value += .2
        if self.True_Value < self.shown_value:
            self.shown_value -= .2

        # Figure out how to change color, at 100 we want (0, 255, 0) at 50 we want (255, 255, 0) and 0 we want (255, 0, 0)
        #temp = round(self.shown_value, 10)
        #self.rgb = Color(self.shown_value)
        #We want lerp.

    def draw(self, surf):
        """
        Takes surf given and creates two rect that are mostly transparent and represent player life.
        :param surf: Surface that rect are to be blit onto.
        :return: None.
        """
        # Inside Bar (DAS + DG)
        size = (max(self.shown_value, 0), self.height)
        inside_bar = pygame.Surface(size)
        inside_bar.set_alpha(100)
        pygame.draw.rect(inside_bar, (self.rgb), inside_bar.get_rect())
        surf.blit(inside_bar, (self.x, self.y))

        # Outline (DAS + DG)
        size_o = (self.width, self.height)
        outline = pygame.Surface(size_o)
        outline.set_alpha(120)
        pygame.draw.rect(outline, (self.rgb), outline.get_rect(), 3)
        surf.blit(outline, (self.x, self.y))

class Boss_Lifebar:

    def __init__(self):
        self.width = 150
        self.height = 20
        self.x = 400 - (self.width / 2)
        self.y = 75 - (self.height + 10)
        self.rgb = (0, 255, 0)
        self.shown_left = 0
        self.shown_middle = 0
        self.shown_right = 0

        self.mid_x = self.x
        self.left_x = self.x - 150
        self.right_x = self.x + 200

    def update_left(self, left_life):
        """
        :param left_life: int or float that represents a life total out of a maximum of 75
        That code can easily be repeated for each update function
        """

        self.True_Left = left_life * 2
        if self.True_Left > self.shown_left:
            self.shown_left += .2
        if self.True_Left < self.shown_left:
            self.shown_left -= .2

    # def update_middle(self, middle_life):
    #     self.True_Middle = middle_life * 2
    #     if self.True_Middle > self.shown_middle:
    #         self.shown_middle += .2
    #     if self.True_Middle < self.shown_middle:
    #         self.shown_middle -= .2
    #
    # def update_right(self, right_life):
    #     self.True_Right = right_life * 2
    #     if self.True_Right > self.shown_right:
    #         self.shown_right += .2
    #     if self.True_Right < self.shown_right:
    #         self.shown_right -= .2

    def draw(self, surf):

        # Left Bar
        # Inside Bar (DAS + DG)
        # size = (self.shown_middle, self.height)
        # inside_bar = pygame.Surface(size)
        # inside_bar.set_alpha(100)
        # pygame.draw.rect(inside_bar, (self.rgb), inside_bar.get_rect())
        # surf.blit(inside_bar, (self.mid_x, self.y))

        size = (self.shown_left, self.height)
        inside_bar = pygame.Surface(size)
        inside_bar.set_alpha(100)
        pygame.draw.rect(inside_bar, (self.rgb), inside_bar.get_rect())
        surf.blit(inside_bar, (self.left_x, self.y))

        # size = (self.shown_right, self.height)
        # inside_bar = pygame.Surface(size)
        # inside_bar.set_alpha(100)
        # pygame.draw.rect(inside_bar, (self.rgb), inside_bar.get_rect())
        # surf.blit(inside_bar, (self.right_x, self.y))



        # Outline (DAS + DG)aaa
        size_o = (self.width * 3, self.height)
        outline = pygame.Surface(size_o)
        outline.set_alpha(120)
        pygame.draw.rect(outline, (self.rgb), outline.get_rect(), 3)
        surf.blit(outline, (self.left_x, self.y))
        # surf.blit(outline, (self.right_x, self.y))
        # surf.blit(outline, (self.mid_x, self.y))