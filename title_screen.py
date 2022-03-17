import pygame

class Title_Screen:
    def __init__(self, screen_width, screen_height):   # ,font?
        self.title_x = screen_width / 2
        self.title_y = screen_height / 3
        self.font = pygame.font.SysFont("Courier New", 20)  #If you want to, you can change the font.
        self.text = "Judo Space"
        self.title_title = self.font.render(str(self.text), False, (250, 250, 0))

        self.button_x = screen_width / 2
        self.button_y = screen_width / 2
        self.button_radius = 32

    def draw(self, screen):
        screen.blit(self.title_title, (self.title_x, self.title_y))
        pygame.draw.circle(screen, (255, 120, 0), (self.button_x, self.button_y), self.button_radius)
        #Would we need a boolean for the title screen blitting? YES.