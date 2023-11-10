import pygame as pg

COLOR = "#96BB7C"


class StartMenu:

    def __init__(self, window, font1, font2):
        self.window = window
        self.font1 = font1
        self.font2 = font2
        self.play_button = None

    def show_start_menu(self):
        text1 = "SNAKE"
        start_text = self.font1.render(text1, False, COLOR)
        start_text_rect = start_text.get_rect()
        start_text_rect.center = (310, 300)
        self.window.blit(start_text, start_text_rect)

        text2 = "PLAY"
        play_text = self.font2.render(text2, False, COLOR)
        play_text_rect = play_text.get_rect()
        play_text_rect.center = (310, 500)
        self.window.blit(play_text, play_text_rect)

        play_box = pg.Rect(240, 435, 135, 105)
        self.play_button = pg.draw.rect(self.window, COLOR, play_box, 5, 2)


    def game_over(self):
        pass
