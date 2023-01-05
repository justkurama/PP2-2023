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

anim_cnt = 0
zhol_x = 0
game_speed = 10
player_y = 215
is_Jump = False
jump_cnt = 7

while True:
    screen.fill((255, 255, 255))
    fps.tick(15)

    screen.blit(dino[anim_cnt], (10, player_y))
    screen.blit(zhol, (zhol_x, 250))
    screen.blit(zhol, (zhol_x+1200, 250))

    keys = pg.key.get_pressed()
    if not is_Jump:
        if keys[pg.K_SPACE]:
            is_Jump = True
    else:
        if jump_cnt >= -7:
            if jump_cnt >= 0:
                player_y -=((jump_cnt ** 2) /2)
            else:
                player_y +=((jump_cnt ** 2) /2)    
            jump_cnt -= 1     
        else:
            is_Jump = False       


    zhol_x -=game_speed
    if zhol_x == -1200:
        zhol_x = 0

    if anim_cnt == 1:
        anim_cnt = 0
    else: anim_cnt +=1   

    pg.display.update()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()