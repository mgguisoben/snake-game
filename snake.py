import pygame as pg

SIZE = 20
MOVE = SIZE


class Snake:

    def __init__(self, window):
        self.window = window
        self.move_x = MOVE
        self.move_y = 0

        self.moving_at_y = False
        self.moving_at_x = True

        self.body = []

        self.create_snake_body()

        self.head = self.body[0]

    def create_snake_body(self):
        for i in range(0, -5, -1):
            x_coord = i * SIZE + 300
            rect = pg.Rect(x_coord, 300, SIZE, SIZE)
            self.body.append(rect)

    def draw_snake(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
            pg.draw.rect(self.window, "blue", self.body[i])

    def extend(self):
        new_rect = pg.Rect(self.body[-1].x, self.body[0].y, SIZE, SIZE)
        self.body.append(new_rect)

    def move_snake(self):
        self.head.x += self.move_x
        self.head.y += self.move_y

    def event_handler(self, event):

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
        self.move_y = -MOVE
        self.moving_at_y = True
        self.moving_at_x = False

    def move_down(self):
        self.move_x = 0
        self.move_y = MOVE
        self.moving_at_y = True
        self.moving_at_x = False

    def move_left(self):
        self.move_x = -MOVE
        self.move_y = 0
        self.moving_at_y = False
        self.moving_at_x = True

    def move_right(self):
        self.move_x = MOVE
        self.move_y = 0
        self.moving_at_y = False
        self.moving_at_x = True
