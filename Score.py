import pygame
#Brought to you by Zachary Hine.
#TO DO: ALL comments in here are by ZDH

class Score:
    def __init__(self, screen_width, screen_height, score):
        self.font = pygame.font.SysFont("Courier New", 15)  # If you want to, you can change the font.
        self.added_score = score
        self.score = 0
        self.score += self.added_score
        self.fp = open("data//high_score.txt", "r")
        self.perma_score = self.fp.readline()
        self.fp.close()
        if self.perma_score != "":
            self.perma_score = int(self.perma_score)
        else:
            self.perma_score = 0

        #Text
        self.score_score = "Score: " + str(self.score)
        self.score_text = self.font.render(str(self.score_score), False, (255, 255, 0))
        self.score_w = 15
        self.score_h = self.score_text.get_height() / 2
        self.high = "High Score: " + str(self.perma_score)
        self.high_score = self.font.render(str(self.high), False, (255, 255, 0))

    def add_to_score(self, additive):
        self.added_score = additive
        self.score += self.added_score

        #Text
        self.score_score = "Score: " + str(self.score)
        self.score_text = self.font.render(str(self.score_score), False, (255, 255, 0))
        self.score_w = 15
        self.score_h = self.score_text.get_height() / 2

    def permanent_score(self, new_score):
        if new_score > self.perma_score:
            self.perma_score = new_score
            self.fp = open("data//high_score.txt", "w")
            self.fp.write(str(self.perma_score))
            self.fp.close()
            self.high = "High Score: " + str(self.perma_score)
            self.high_score = self.font.render(str(self.high), False, (255, 255, 0))
            self.score = 0

    def display_score(self, screen):
        screen.blit(self.score_text, (self.score_w, self.score_h))
        screen.blit(self.high_score, (self.score_w, self.score_h * 3))