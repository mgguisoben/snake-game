import pygame as pg

pg.font.init()

COLOR = "#96BB7C"
BORDER_WD = 3


class ScoreBoard:

    def __init__(self, window, snake_size, font):
        self.window = window
        self.font = font
        self.lt_1 = snake_size + 8
        self.lt_2 = self.window.get_width() - self.lt_1

        self.borders = []

        self.pts = [(self.lt_1, self.lt_1), (self.lt_1, self.lt_2), (self.lt_2, self.lt_2), (self.lt_2, self.lt_1)]

        self.score = 0

    def create_border(self):
        for i in range(4):
            if i != 3:
                border = pg.draw.line(self.window, COLOR, self.pts[i], self.pts[i + 1], BORDER_WD)
                self.borders.append(border)
            else:
                border = pg.draw.line(self.window, COLOR, self.pts[i], self.pts[0], BORDER_WD)
                self.borders.append(border)

    def show_score(self):
        text = f"S C O R E  :    {self.score}"
        score_text = self.font.render(text, False, COLOR)
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = (24, 2)
        self.window.blit(score_text, score_text_rect)
