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
        self.boss_arm_hit = pygame.mixer.Sound('sound//arm_hit.ogg')

    def sfx(self, sfx):
        """
        Takes string input and returns command to play sound clip.
        :param sfx: Str representing type of SFX.
        :return: None.
        """
        if isinstance(sfx, str):
            if sfx == "parry":
                pygame.mixer.Sound.play(self.parry)
            elif sfx == "block":
                pygame.mixer.Sound.play(self.block)
            elif sfx == "dash":
                pygame.mixer.Sound.play(self.dash)
            elif sfx == "p_hit":
                pygame.mixer.Sound.play(self.got_hit)
            elif sfx == "p_shoot":
                pygame.mixer.Sound.play(self.player_shoot)
            elif sfx == "e_hit":
                pygame.mixer.Sound.play(self.enemy_hit)
            elif sfx == "e_shoot":
                pygame.mixer.Sound.play(self.enemy_shoot)
            elif sfx == "menu":
                pygame.mixer.Sound.play(self.menu_click)
            elif sfx == "quit":
                pygame.mixer.Sound.play(self.quit)
                pygame.time.wait(1500)
            elif sfx == "h_hit":
                pygame.mixer.Sound.play(self.health_item_hit)
            elif sfx == "h_get":
                pygame.mixer.Sound.play(self.health_item_get)
            elif sfx == "b_a_hit":
                pygame.mixer.Sound.play(self.boss_arm_hit)
        else:
            raise TypeError("sfx must be given in str form.")

    def music(self, song):
        """
        Takes in songs and loops them over a period. Must be terminated to end.
        :param song: Str.
        :return: None.
        """
        if isinstance(song, str):
            if song == "level_one":
                pygame.mixer.music.load('sound//awake10_megaWall.ogg')
            if song == "menu":
                pygame.mixer.music.load("sound//8bit_Bossa.ogg")
            pygame.mixer.music.play(-1)
        else:
            raise TypeError("song must be given in str form.")
