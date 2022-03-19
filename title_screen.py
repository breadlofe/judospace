import pygame

class Title_Screen:
    def __init__(self, screen_width, screen_height):
        #Title screen
        self.title_x = screen_width / 2
        self.title_y = screen_height / 3
        self.font = pygame.font.SysFont("Courier New", 20)  #If you want to, you can change the font.
        self.title_text = "Judo Space"
        self.title_title = self.font.render(str(self.title_text), False, (250, 250, 0))
        self.button_radius = 32

        #Play button
        self.playbutton_x = screen_width / 2
        self.playbutton_y = screen_width / 2

        #Exit button
        self.playbutton_x = screen_width / 2
        self.playbutton_y = screen_width / 2

        #Credits button
        self.playbutton_x = screen_width / 2
        self.playbutton_y = screen_width / 2

        #Level One
        self.one_text = "Level One"
        self.level_one_display = self.font.render(str(self.one_text), False, (250, 250, 0))

    def draw(self, screen):
        screen.blit(self.title_title, (self.title_x, self.title_y))
        pygame.draw.circle(screen, (255, 120, 0), (self.playbutton_x - (self.button_radius / 2),
                                                   self.playbutton_y), self.button_radius)
        #Would we need a boolean for the title screen blitting? YES.