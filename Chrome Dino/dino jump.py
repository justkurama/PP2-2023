import pygame as pg, sys
fps = pg.time.Clock()
pg.init()

screen = pg.display.set_mode((600, 300))
pg.display.set_caption("Dino")
zhol = pg.image.load('Chrome Dino/images/zhol.png')
dino = [
    pg.image.load('Chrome Dino/images/player sprite1.png'),
    pg.image.load('Chrome Dino/images/player sprite2.png'),
]
anim = 0
zhol_x = 0
game_speed = 10
while True:
    screen.fill((255, 255, 255))
    fps.tick(15)
    screen.blit(dino[anim], (0, 215))
    screen.blit(zhol, (zhol_x, 250))
    screen.blit(zhol, (zhol_x+1200, 250))
    zhol_x -=game_speed
    if zhol_x == -1200:
        zhol_x = 0
    if anim == 1:
        anim = 0
    else: anim +=1    
    pg.display.update()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()