import pygame
#Brought to you by Zachary Hine.
#TO DO: ALL comments in here are by ZDH

class Title_Screen:
    def __init__(self, screen_width, screen_height):
        #Title screen
        self.title_x = screen_width / 2
        self.title_y = screen_height / 3
        self.font = pygame.font.SysFont("Courier New", 20)  #If you want to, you can change the font.
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

        #Level One
        self.one_text = "Level One"
        self.level_one_display = self.font.render(str(self.one_text), False, (250, 250, 0))
        self.level_x = screen_width / 2
        self.level_y = screen_height / 2

        #button rectangles      #Check with Clay about making these rectangles disappear.
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
                                    self.button_radius, self.button_radius)    #Back

    def draw(self, screen):
        screen.blit(self.title_title, (self.title_x - (self.title_title.get_width() / 2),
                                       self.title_y - (self.title_title.get_height() / 2)))
        pygame.draw.circle(screen, (255, 120, 0), (self.playbutton_x - (self.button_radius / 2),
                                                   self.playbutton_y), self.button_radius)  #Play
        #pygame.draw.rect(screen, (200, 200, 0), self.circle_rect_p, 1)
        screen.blit(self.play, (self.playbutton_x - self.play.get_width(),
                                                   self.playbutton_y - self.button_radius / 2))
        pygame.draw.circle(screen, (255, 12, 0), (self.exitbutton_x - (self.button_radius / 2),
                                                   self.exitbutton_y), self.button_radius)  #Exit
        #pygame.draw.rect(screen, (200, 200, 0), self.circle_rect_e, 1)
        screen.blit(self.exit, (self.exitbutton_x - self.exit.get_width(),
                                     self.exitbutton_y - self.button_radius / 2))
        pygame.draw.circle(screen, (255, 220, 0), (self.creditsbutton_x - (self.button_radius / 2),
                                                   self.creditsbutton_y), self.button_radius)  #Credits
        #pygame.draw.rect(screen, (200, 200, 0), self.circle_rect_c, 1)
        screen.blit(self.the_credits_button_text,
                    (self.creditsbutton_x - self.the_credits_button_text.get_width(),
                     self.creditsbutton_y - self.button_radius / 2))
        #Would we need a boolean for the title screen blitting? YES!
        #Working out on the quarks reguarding placements...

    def display_level_one(self, screen):
        screen.blit(self.level_one_display,
                    (self.level_x - (self.level_one_display.get_width() / 2),
                     self.level_y - (self.level_one_display.get_height() / 2)))

    def display_credits(self, screen):
        screen.blit(self.credits, (self.credits_x - (self.credits.get_width() / 2),
                                       self.credits_y - (self.credits.get_height() / 2)))
        pygame.draw.circle(screen, (100, 0, 255), (25, 575), self.button_radius / 2)
        #pygame.draw.rect(screen, ((200, 200, 0)), self.credits_back_rect, 1)
        screen.blit(self.back, (25, 575 - self.back.get_height() / 2))