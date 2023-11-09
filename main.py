import pygame as pg

from snake import Snake
from food import Food
from score import ScoreBoard

WINDOW_LEN = 600
WINDOW_DIM = (WINDOW_LEN, WINDOW_LEN)

pg.init()
pg.display.set_caption("SNEK")

window = pg.display.set_mode(WINDOW_DIM)
clock = pg.time.Clock()
score_board = ScoreBoard(window, WINDOW_LEN)
snake = Snake(window)
food_ = Food(window, WINDOW_LEN)


running = True

while running:

    window.fill("white")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        snake.event_handler(event)

    food = food_.create_food()

    border = score_board.create_border()

    snake.draw_snake()
    snake.move_snake()

    # Collision with food
    if snake.head.colliderect(food):
        snake.extend()
        food_.new_food()
        food = food_.create_food()

    # Collision with self
    if snake.head.collidelist(snake.body[1:]) != -1:
        print("COLLISION")
        running = False

    pg.display.update()

    clock.tick(10)

pg.quit()
