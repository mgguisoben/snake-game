import pygame as pg

from food import Food
from menu import StartMenu
from score import ScoreBoard
from snake import Snake

WINDOW_LEN = 600
WINDOW_DIM = (WINDOW_LEN, WINDOW_LEN)
SNAKE_SIZE = 16
BG_COLOR = "#184D47"
FONT_FP = "assets/font/Squareworm-ejM6.ttf"
FONT1 = pg.font.Font(FONT_FP, 20)
FONT2 = pg.font.Font(FONT_FP, 400)
FONT3 = pg.font.Font(FONT_FP, 100)

pg.init()
pg.display.set_caption("SNEK")

window = pg.display.set_mode(WINDOW_DIM)
clock = pg.time.Clock()
game_menu = StartMenu(window, FONT2, FONT3)
score_board = ScoreBoard(window, SNAKE_SIZE, FONT1)
snake = Snake(window, SNAKE_SIZE)
food_ = Food(window, WINDOW_LEN, SNAKE_SIZE)

running = False
game_start = False
game_over = False

while not game_start:

    window.fill(BG_COLOR)

    game_menu.show_start_menu()
    score_board.create_border()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            game_start = True

        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            if game_menu.play_button.collidepoint(pos):
                game_start = True
                running = True

    pg.display.update()

while running:

    window.fill(BG_COLOR)

    if not game_over:

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
            game_over = True

        if snake.head.collidelist(score_board.borders) != -1:
            game_over = True

    if game_over:
        game_menu.show_start_menu()
        score_board.create_border()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if game_menu.play_button.collidepoint(pos):
                    score_board.score = 0
                    snake = Snake(window, SNAKE_SIZE)
                    game_over = False

    pg.display.update()

    clock.tick(10)

pg.quit()
