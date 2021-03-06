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

        #Boss Warning!
        self.battle_text = "Boss Battle!"
        self.boss_warning = self.font2.render(str(self.battle_text), False, (255, 25, 12))
        self.level_x = screen_width / 2
        self.level_y = screen_height / 2

        #Top of the screen boss text
        self.boss_text = "Boss Level!"
        self.boss_level_display = self.font.render(str(self.boss_text), False, (250, 250, 0))
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
        self.ds1 = "Original idea, player elements, player projectiles, collision,"
        self.ds2 = "the boss battle, and sound effects/music are by Dustin S."
        self.DS1 = self.font.render(str(self.ds1), False, (250, 250, 0))
        self.DS2 = self.font.render(str(self.ds2), False, (250, 250, 0))
        self.dg1 = "Background, level design, enemy AI, enemy projectiles,"
        self.dg2 = "the boss battle, and health bar are by Dylan G."
        self.DG1 = self.font.render(str(self.dg1), False, (250, 250, 0))
        self.DG2 = self.font.render(str(self.dg2), False, (250, 250, 0))
        self.zh1 = "All text, scores, some debugging, the boss battle,"
        self.zh2 = "and keybinding are by Zachary H."
        self.ZH1 = self.font.render(str(self.zh1), False, (250, 250, 0))
        self.ZH2 = self.font.render(str(self.zh2), False, (250, 250, 0))

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
        self.logline_continue_rect = pygame.Rect(self.playbutton_x - (self.button_radius + self.button_radius / 2),
                                            self.playbutton_y - self.button_radius + 80,
                                            self.button_radius * 2, self.button_radius * 2)#The continue button for logline

        self.log1 = "After having his home destroyed by"
        self.log2 = "the greedy and wrathful emperor"
        self.log3 = "Malroe... Josada, our protagonist,"
        self.log4 = "must go on a vengeful adventure to"
        self.log5 = "put an end to Malroe's evil reign..."
        self.logline1 = self.font.render(str(self.log1), False, (250, 250, 0))
        self.logline2 = self.font.render(str(self.log2), False, (250, 250, 0))
        self.logline3 = self.font.render(str(self.log3), False, (250, 250, 0))
        self.logline4 = self.font.render(str(self.log4), False, (250, 250, 0))
        self.logline5 = self.font.render(str(self.log5), False, (250, 250, 0))
        self.contue = "Continue"
        self.continue_continue = self.font.render(str(self.contue), False, (250, 250, 0))

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

    def display_credits(self, screen):
        screen.blit(self.credits, (self.credits_x - (self.credits.get_width() / 2),
                                       self.credits_y - (self.credits.get_height() / 2)))
        pygame.draw.circle(screen, (100, 0, 255), (25, 575), self.button_radius / 2)
        #pygame.draw.rect(screen, ((200, 200, 0)), self.credits_back_rect, 1) #Starfish
        screen.blit(self.back, (50, 575 - self.back.get_height() / 2))

    def display_game_over(self, screen):
        screen.blit(self.game_over, (self.over_x - (self.game_over.get_width() / 2),
                                     self.over_y - (self.game_over.get_height() / 2)))

    def display_thebosswarning(self, screen):
        screen.blit(self.boss_warning, (self.level_x - (self.boss_warning.get_width() / 2),
                                           self.over_y - (self.boss_warning.get_height() / 2)))

    def display_bosslevel(self, screen):
        screen.blit(self.boss_level_display, (self.level_x - (self.boss_level_display.get_width() / 2), 5))

    def display_bossdefeated(self, screen):
        screen.blit(self.boss_defeated, (self.over_x - (self.boss_defeated.get_width() / 2),
                                           self.over_y - (self.boss_defeated.get_height() / 2)))

    def display_logline(self, screen):
        screen.blit(self.logline1, (self.level_x - (self.logline1.get_width() / 2), 100))
        screen.blit(self.logline2, (self.level_x - (self.logline2.get_width() / 2), 140))
        screen.blit(self.logline3, (self.level_x - (self.logline3.get_width() / 2), 180))
        screen.blit(self.logline4, (self.level_x - (self.logline4.get_width() / 2), 220))
        screen.blit(self.logline5, (self.level_x - (self.logline5.get_width() / 2), 260))
        #pygame.draw.rect(screen, (200, 200, 0), self.logline_continue_rect, 1)
        pygame.draw.circle(screen, (155, 220, 0), (self.playbutton_x - (self.button_radius / 2),
                                                   self.playbutton_y + 80), self.button_radius)
        screen.blit(self.continue_continue, (self.playbutton_x - self.continue_continue.get_width() + 31,
                                                   self.playbutton_y + self.button_radius + 80))

    def display_final_credits(self, screen):
        screen.blit(self.credits_title, (self.level_x - (self.credits_title.get_width() / 2), 80))
        screen.blit(self.credits_title_credits,
                    (self.level_x - (self.credits_title_credits.get_width() / 2), 125))
        screen.blit(self.DS1, (self.level_x - (self.DS1.get_width() / 2), 190))
        screen.blit(self.DS2, (self.level_x - (self.DS2.get_width() / 2), 240))
        screen.blit(self.DG1, (self.level_x - (self.DG1.get_width() / 2), 300))
        screen.blit(self.DG2, (self.level_x - (self.DG2.get_width() / 2), 350))
        screen.blit(self.ZH1, (self.level_x - (self.ZH1.get_width() / 2), 410))
        screen.blit(self.ZH2, (self.level_x - (self.ZH2.get_width() / 2), 460))