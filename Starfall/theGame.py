import pygame as pg
import sys
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Star fall")
bg = pg.image.load('Starfall/images/bg.png')
while True:
    screen.blit(bg, (0, 0))
    pg.display.update()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()