import pygame
#Brought to you by Zachary Hine.
#TO DO: ALL comments in here are by ZDH

class Score:
    def __init__(self, screen_width, screen_height, score):
        self.font = pygame.font.SysFont("Courier New", 15)  # If you want to, you can change the font.
        self.added_score = score
        self.score = 0
        self.score += self.added_score

        # Text
        self.score_score = "Score: " + str(self.score)
        self.score_text = self.font.render(str(self.score_score), False, (255, 255, 0))
        self.score_w = 15
        self.score_h = self.score_text.get_height() / 2

    def add_to_score(self, additive):
        self.added_score = additive
        self.score += self.added_score

    def display_score(self, screen):
        screen.blit(self.score_text, (self.score_w, self.score_h))