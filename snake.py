import pygame as pg

SNAKE_COLOR1 = "#96BB7C"
SNAKE_COLOR2 = "#D6EFC7"



class Snake:

    def __init__(self, window, snake_size):
        self.window = window
        self.lt = self.window.get_width()
        self.size = snake_size
        self.move = self.size
        self.move_x = self.size
        self.move_y = 0

        self.moving_at_y = False
        self.moving_at_x = True

        self.body = []

        self.create_snake_body()

        self.head = self.body[0]

    def create_snake_body(self):
        for i in range(0, -5, -1):
            x_coord = i * self.size + self.lt / 2
            rect = pg.Rect(x_coord, self.lt / 2, self.size, self.size)
            self.body.append(rect)

    def draw_snake(self):
        pg.draw.rect(self.window, SNAKE_COLOR2, self.head, 0, 2)

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
            pg.draw.rect(self.window, SNAKE_COLOR1, self.body[i], 2, 2)

    def extend(self):
        new_rect = pg.Rect(self.body[-1].x, self.body[-1].y, self.size, self.size)
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
        self.move_y = -self.move
        self.moving_at_y = True
        self.moving_at_x = False

    def move_down(self):
        self.move_x = 0
        self.move_y = self.move
        self.moving_at_y = True
        self.moving_at_x = False

    def move_left(self):
        self.move_x = -self.move
        self.move_y = 0
        self.moving_at_y = False
        self.moving_at_x = True

    def move_right(self):
        self.move_x = self.move
        self.move_y = 0
        self.moving_at_y = False
        self.moving_at_x = True
