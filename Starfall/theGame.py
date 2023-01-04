import pygame as pg, sys
pg.init()

screen = pg.display.set_mode((800, 458))
pg.display.set_caption("Star fall")

bg = pg.image.load('Starfall/images/bg.jpg')
player = pg.image.load('Starfall/images/player/player_front.png')

while True:
    screen.blit(bg, (0, 0))
    screen.blit(player, (380, 300))

    pg.display.update()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()