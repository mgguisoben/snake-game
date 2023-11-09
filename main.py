import pygame as pg

from snake import Snake

WINDOW_SIZE = (600, 600)

pg.init()
pg.display.set_caption("SNEK")

clock = pg.time.Clock()
snake = Snake()

window = pg.display.set_mode(WINDOW_SIZE)

rect = pg.Rect(300, 300, 15, 15)


running = True

while running:

    window.fill("white")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        snake.snake_movements(event)

    rect.x += snake.move_x
    rect.y += snake.move_y

    pg.draw.rect(window, "blue", rect)

    pg.display.update()

    clock.tick(60)

pg.quit()
