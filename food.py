from random import randrange

from pygame import draw


class Food:

    def __init__(self, window, window_lt, snake_size):
        self.window = window
        self.radius = snake_size / 2
        self.start = snake_size + 16
        self.stop = window_lt - 32

        self.x = 0
        self.y = 0

        self.new_food()

    def create_food(self):
        food = draw.circle(self.window, "red", (self.x, self.y), self.radius)
        return food

    def new_food(self):
        self.x = randrange(self.start, self.stop)
        self.y = randrange(self.start, self.stop)
