# Dustin Simpkins
import pygame
import time

class Jukebox:
    """
    Handles all music and sound effects.
    """
    def __init__(self):
        """
        Creates global music variables.
        """
        self.enemy_hit = pygame.mixer.Sound('sound//hit_enemy.ogg')
        self.quit = pygame.mixer.Sound('sound//decline.ogg')
        self.got_hit = pygame.mixer.Sound('sound//got_hit.ogg')
        self.menu_click = pygame.mixer.Sound('sound//menu_click.ogg')
        self.parry = pygame.mixer.Sound('sound//parry.ogg')
        self.block = pygame.mixer.Sound('sound//block.ogg')
        self.dash = pygame.mixer.Sound('sound//dash.ogg')
        self.player_shoot = pygame.mixer.Sound('sound//player_shoot.ogg')
        self.enemy_shoot = pygame.mixer.Sound('sound//enemy_shoot.ogg')
        self.health_item_hit = pygame.mixer.Sound('sound//health_item_hit.ogg')
        self.health_item_get = pygame.mixer.Sound('sound//health_item_get.ogg')
        self.level_theme_one = pygame.mixer.Sound('sound//awake10_megaWall.ogg')

    def sfx(self, type):
        """
        Takes string input and returns command to play sound clip.
        :param type: Str representing type of SFX.
        :return: None.
        """
        if isinstance(type, str):
            if type == "parry":
                pygame.mixer.Sound.play(self.parry)
            elif type == "block":
                pygame.mixer.Sound.play(self.block)
            elif type == "dash":
                pygame.mixer.Sound.play(self.dash)
            elif type == "p_hit":
                pygame.mixer.Sound.play(self.got_hit)
            elif type == "p_shoot":
                pygame.mixer.Sound.play(self.player_shoot)
            elif type == "e_hit":
                pygame.mixer.Sound.play(self.enemy_hit)
            elif type == "e_shoot":
                pygame.mixer.Sound.play(self.enemy_shoot)
            elif type == "menu":
                pygame.mixer.Sound.play(self.menu_click)
            elif type == "quit":
                pygame.mixer.Sound.play(self.quit)
                pygame.time.wait(1500)
            elif type == "h_hit":
                pygame.mixer.Sound.play(self.health_item_hit)
            elif type == "h_get":
                pygame.mixer.Sound.play(self.health_item_get)
        else:
            raise TypeError("type must be given in str form.")
