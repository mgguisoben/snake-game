import pygame as pg

from food import Food
from score import ScoreBoard
from snake import Snake

WINDOW_LEN = 600
WINDOW_DIM = (WINDOW_LEN, WINDOW_LEN)
SNAKE_SIZE = 16

pg.init()
pg.display.set_caption("SNEK")

window = pg.display.set_mode(WINDOW_DIM)
clock = pg.time.Clock()
score_board = ScoreBoard(window, SNAKE_SIZE)
snake = Snake(window, SNAKE_SIZE)
food_ = Food(window, WINDOW_LEN, SNAKE_SIZE)

running = True

while running:

    window.fill("white")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        snake.event_handler(event)

    food = food_.create_food()

    score_board.create_border()
    score_board.show_score()
    # print(food)

    snake.draw_snake()
    snake.move_snake()

    # Collision with food
    if snake.head.colliderect(food):
        snake.extend()
        score_board.score += 1
        food_.new_food()
        food = food_.create_food()

    # Collision with self
    if snake.head.collidelist(snake.body[1:]) != -1:
        running = False

    if snake.head.collidelist(score_board.borders) != -1:
        running = False

    pg.display.update()

    clock.tick(10)

pg.quit()
