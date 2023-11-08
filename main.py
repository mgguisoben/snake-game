import pygame as pg

pg.init()


window = pg.display.set_mode((600, 600))
pg.display.set_caption("SNEK")

running = True

while running:

    window.fill("white")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    pg.display.update()

pg.quit()