import pygame
#Brought to you by Zachary Hine.
#TO DO: ALL comments in here are by ZDH

class Title_Screen:
    def __init__(self, screen_width, screen_height):
        #Title screen
        self.title_x = screen_width / 2
        self.title_y = screen_height / 3
        self.font = pygame.font.SysFont("Courier New", 20)  #If you want to, you can change the font.
        self.font2 = pygame.font.SysFont("Courier New", 40)  # If you want to, you can change the font.
        self.button_radius = 32

        #Play button
        self.playbutton_x = screen_width / 2
        self.playbutton_y = screen_width / 2

        #Credits button
        self.creditsbutton_x = screen_width / 2 - screen_height / 3
        self.creditsbutton_y = screen_width / 2

        #Exit button
        self.exitbutton_x = self.creditsbutton_x + self.playbutton_x
        self.exitbutton_y = screen_width / 2

        #Text
        self.title_text = "Judo Space"
        self.title_title = self.font.render(str(self.title_text), False, (250, 250, 0))
        self.credits_text = "Judo Space is created by: Dustin S, Dylan G, and Zachary H."
        self.credits = self.font.render(str(self.credits_text), False, (250, 250, 0))
        self.credits_x = screen_width / 2
        self.credits_y = screen_height / 3
        self.back_back = "Back"
        self.back = self.font.render(str(self.back_back), False, (250, 250, 0))
        self.exit_exit = "Exit"
        self.exit = self.font.render(str(self.exit_exit), False, (250, 250, 0))
        self.play_play = "Play"
        self.play = self.font.render(str(self.play_play), False, (250, 250, 0))
        self.credits_credits = "Credits"
        self.the_credits_button_text = self.font.render(str(self.credits_credits), False, (250, 250, 0))
        self.level1 = "Level One Complete!"
        self.level1_complete = self.font.render(str(self.level1), False, (249, 251, 0))
        self.level2 = "Level Two Complete!"
        self.level2_complete = self.font.render(str(self.level2), False, (249, 251, 0))
        self.level3 = "Level Three Complete!"
        self.level3_complete = self.font.render(str(self.level3), False, (249, 251, 0))
        self.level4 = "Level Four Complete!"
        self.level4_complete = self.font.render(str(self.level4), False, (249, 251, 0))

        #Game Over!
        self.over_over = "Game Over!"
        self.game_over = self.font.render(str(self.over_over), False, (250, 250, 0))
        self.over_x = screen_width / 2
        self.over_y = screen_height / 2

        #Level One
        self.one_text = "Level One"
        self.level_one_display = self.font.render(str(self.one_text), False, (250, 250, 0))
        self.level_x = screen_width / 2
        #self.level_y = screen_height / 2

        #Level Two
        self.two_text = "Level Two"
        self.level_two_display = self.font.render(str(self.two_text), False, (250, 250, 0))
        self.level_x = screen_width / 2
        #self.level_y = screen_height / 2

        #Level Three
        self.three_text = "Level Three"
        self.level_three_display = self.font.render(str(self.three_text), False, (250, 250, 0))
        self.level_x = screen_width / 2
        #self.level_y = screen_height / 2

        #Level Four
        self.four_text = "Level Four"
        self.level_four_display = self.font.render(str(self.four_text), False, (250, 250, 0))
        self.level_x = screen_width / 2
        #self.level_y = screen_height / 2

        #Boss Warning!
        self.battle_text = "Boss Battle!"
        self.boss_warning = self.font2.render(str(self.battle_text), False, (255, 25, 12))
        self.level_x = screen_width / 2
        self.level_y = screen_height / 2

        #Boss Defeated!
        self.boss_d = "Boss Defeated!"
        self.boss_defeated = self.font2.render(str(self.boss_d), False, (120, 25, 255))
        self.level_x = screen_width / 2
        self.level_y = screen_height / 2

        #The credits after the boss
        self.the_credits1 = "Judo Space"
        self.credits_title = self.font.render(str(self.the_credits1), False, (250, 250, 0))
        self.the_credits2 = "Credits:"
        self.credits_title_credits = self.font.render(str(self.the_credits2), False, (250, 250, 0))
        self.ds = "Original idea, player elements, player projectiles, " \
                  "and sound effects/music are by Dustin S."
        self.DS = self.font.render(str(self.ds), False, (250, 250, 0))
        self.dg = "Background, level design, enemy AI, enemy projectiles, " \
                  "collision, and health bar are by Dylan G."
        self.DG = self.font.render(str(self.dg), False, (250, 250, 0))
        self.zh = "All text, scores, some debugging, " \
                  "and keybinding are by Zachary H."
        self.ZH = self.font.render(str(self.zh), False, (250, 250, 0))

        #Button rectangles
        self.circle_rect_c = pygame.Rect(self.creditsbutton_x - (self.button_radius + self.button_radius / 2),
                                    self.creditsbutton_y - self.button_radius,
                                    self.button_radius * 2, self.button_radius * 2)     #Credits
        self.circle_rect_e = pygame.Rect(self.exitbutton_x - (self.button_radius + self.button_radius / 2),
                                    self.exitbutton_y - self.button_radius,
                                    self.button_radius * 2, self.button_radius * 2)     #Exit
        self.circle_rect_p = pygame.Rect(self.playbutton_x - (self.button_radius + self.button_radius / 2),
                                    self.playbutton_y - self.button_radius,
                                    self.button_radius * 2, self.button_radius * 2)     #Play
        self.credits_back_rect = pygame.Rect(25 / 2 - 3.5, 575 - self.button_radius / 2,
                                    self.button_radius, self.button_radius)             #Back
        #self.level_text = ""
        #self.complete = ""

    def level_text_ren(self, level_number):
        self.level_text = f"Level {level_number}"
        self.level_display = self.font.render(str(self.level_text), False, (250, 250, 0))

    def display_level(self, screen):
        screen.blit(self.level_display,
                    (self.level_x - (self.level_display.get_width() / 2), 5))

    def complete_text(self, level_number):
        self.complete = f"Level {level_number} Complete!"
        self.level_complete = self.font.render(str(self.complete), False, (249, 251, 0))

    def display_level_completed(self, screen):
        screen.blit(self.level_complete, (self.over_x - (self.level_complete.get_width() / 2),
                                           self.over_y - (self.level_complete.get_height() / 2)))

    def draw(self, screen):
        screen.blit(self.title_title, (self.title_x - (self.title_title.get_width() / 2),
                                       self.title_y - (self.title_title.get_height() / 2)))
        pygame.draw.circle(screen, (255, 120, 0), (self.playbutton_x - (self.button_radius / 2),
                                                   self.playbutton_y), self.button_radius)  #Play
        #pygame.draw.rect(screen, (200, 200, 0), self.circle_rect_p, 1)
        screen.blit(self.play, (self.playbutton_x - self.play.get_width() + 8,
                                                   self.playbutton_y + self.button_radius))
        pygame.draw.circle(screen, (255, 12, 0), (self.exitbutton_x - (self.button_radius / 2),
                                                   self.exitbutton_y), self.button_radius)  #Exit
        #pygame.draw.rect(screen, (200, 200, 0), self.circle_rect_e, 1)
        screen.blit(self.exit, (self.exitbutton_x - self.exit.get_width() + 8,
                                     self.exitbutton_y + self.button_radius))
        pygame.draw.circle(screen, (255, 220, 0), (self.creditsbutton_x - (self.button_radius / 2),
                                                   self.creditsbutton_y), self.button_radius)  #Credits
        #pygame.draw.rect(screen, (200, 200, 0), self.circle_rect_c, 1)
        screen.blit(self.the_credits_button_text,
                    (self.creditsbutton_x - self.the_credits_button_text.get_width() + 25,
                     self.creditsbutton_y + self.button_radius))
        #Would we need a boolean for the title screen blitting? YES!

    def display_level_one(self, screen):
        screen.blit(self.level_one_display,
                    (self.level_x - (self.level_one_display.get_width() / 2), 5))

    def display_level_two(self, screen):
        screen.blit(self.level_two_display,
                    (self.level_x - (self.level_two_display.get_width() / 2), 5))

    def display_level_three(self, screen):
        screen.blit(self.level_three_display,
                    (self.level_x - (self.level_three_display.get_width() / 2), 5))

    def display_level_four(self, screen):
        screen.blit(self.level_four_display,
                    (self.level_x - (self.level_four_display.get_width() / 2), 5))

    def display_credits(self, screen):
        screen.blit(self.credits, (self.credits_x - (self.credits.get_width() / 2),
                                       self.credits_y - (self.credits.get_height() / 2)))
        pygame.draw.circle(screen, (100, 0, 255), (25, 575), self.button_radius / 2)
        #pygame.draw.rect(screen, ((200, 200, 0)), self.credits_back_rect, 1) #Starfish
        screen.blit(self.back, (50, 575 - self.back.get_height() / 2))

    def display_game_over(self, screen):
        screen.blit(self.game_over, (self.over_x - (self.game_over.get_width() / 2),
                                     self.over_y - (self.game_over.get_height() / 2)))

    def display_level_one_completed(self, screen):
        screen.blit(self.level1_complete, (self.over_x - (self.level1_complete.get_width() / 2),
                                           self.over_y - (self.level1_complete.get_height() / 2)))

    def display_level_two_completed(self, screen):
        screen.blit(self.level2_complete, (self.over_x - (self.level2_complete.get_width() / 2),
                                           self.over_y - (self.level2_complete.get_height() / 2)))

    def display_level_three_completed(self, screen):
        screen.blit(self.level3_complete, (self.over_x - (self.level3_complete.get_width() / 2),
                                           self.over_y - (self.level3_complete.get_height() / 2)))

    def display_level_four_completed(self, screen):
        screen.blit(self.level4_complete, (self.over_x - (self.level4_complete.get_width() / 2),
                                           self.over_y - (self.level4_complete.get_height() / 2)))

    def display_thebosswarning(self, screen):
        screen.blit(self.boss_warning, (self.over_x - (self.boss_warning.get_width() / 2),
                                           self.over_y - (self.boss_warning.get_height() / 2)))

    def display_bossdefeated(self, screen):
        screen.blit(self.boss_defeated, (self.level_x - (self.boss_defeated.get_width() / 2),
                                           self.level_y - (self.boss_defeated.get_height() / 2)))

    # def display_final_credits(self, screen):
    #     screen.blit(self.credits_title, (self.level_x - (self.credits_title.get_width() / 2),
    #                                      80))
    #     screen.blit(self.credits_title_credits, (self.level_x - (self.credits_title_credits.get_width() / 2),
    #                                      125))
    #     screen.blit(self.DS, (self.level_x - (self.DS.get_width() / 2),
    #                                      190))
    #     screen.blit(self.DG, (self.level_x - (self.DG.get_width() / 2),
    #                           240))
    #     screen.blit(self.ZH, (self.level_x - (self.ZH.get_width() / 2),
    #                           290))