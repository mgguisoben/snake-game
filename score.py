import pygame as pg

pg.font.init()

BORDER_WD = 3
FONT = pg.font.SysFont("Arial", 20, "bold")


class ScoreBoard:

    def __init__(self, window, snake_size):
        self.window = window
        self.lt_1 = snake_size + 8
        self.lt_2 = self.window.get_width() - self.lt_1

        self.borders = []

        self.pts = [(self.lt_1, self.lt_1), (self.lt_1, self.lt_2), (self.lt_2, self.lt_2), (self.lt_2, self.lt_1)]

        self.score = 0

    def create_border(self):
        for i in range(4):
            if i != 3:
                border = pg.draw.line(self.window, "black", self.pts[i], self.pts[i + 1], BORDER_WD)
                self.borders.append(border)
            else:
                border = pg.draw.line(self.window, "black", self.pts[i], self.pts[0], BORDER_WD)
                self.borders.append(border)

    def show_score(self):
        text = f"Score: {self.score}"
        score_text = FONT.render(text, False, "black")
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = (24, 2)
        self.window.blit(score_text, score_text_rect)
