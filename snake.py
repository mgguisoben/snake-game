import pygame as pg


class Snake:

    def __init__(self):
        self.move_speed = 2
        self.move_x = 2
        self.move_y = 0

        self.moving_at_y = False
        self.moving_at_x = True

        # self.body = []
        # self.head = self.body[0]

    def add_snake_body(self):
        pass

    def snake_movements(self, event):

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and not self.moving_at_y:
                self.move_up()
            elif event.key == pg.K_DOWN and not self.moving_at_y:
                self.move_down()
            elif event.key == pg.K_LEFT and not self.moving_at_x:
                self.move_left()
            elif event.key == pg.K_RIGHT and not self.moving_at_x:
                self.move_right()

    def move_up(self):
        self.move_x = 0
        self.move_y = -self.move_speed
        self.moving_at_y = True
        self.moving_at_x = False

    def move_down(self):
        self.move_x = 0
        self.move_y = self.move_speed
        self.moving_at_y = True
        self.moving_at_x = False

    def move_left(self):
        self.move_x = -self.move_speed
        self.move_y = 0
        self.moving_at_y = False
        self.moving_at_x = True

    def move_right(self):
        self.move_x = self.move_speed
        self.move_y = 0
        self.moving_at_y = False
        self.moving_at_x = True
