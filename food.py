from random import randint

from pygame import draw


class Food:

    def __init__(self, window, window_lt):
        self.window = window
        self.lt = window_lt - 22

        self.x = 0
        self.y = 0

        self.new_food()

    def create_food(self):
        food = draw.circle(self.window, "red", (self.x, self.y), 8, 0, True, True, True, True)
        return food

    def new_food(self):
        self.x = randint(20, self.lt)
        self.y = randint(50, self.lt)
