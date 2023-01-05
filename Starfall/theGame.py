import pygame as pg, sys
fps = pg.time.Clock()
pg.init()

screen = pg.display.set_mode((750, 672))
pg.display.set_caption("Star fall")

bg_music = pg.mixer.Sound('Starfall/sounds/Bright Night.mp3')
bg_music.play()

bg = pg.image.load('Starfall/images/bg.jpg')
player = pg.image.load('Starfall/images/player/player_front.png')
walk_right = [
    pg.image.load('Starfall/images/player/player_right1.png'),
    pg.image.load('Starfall/images/player/player_right2.png'),
    pg.image.load('Starfall/images/player/player_right3.png'),
    pg.image.load('Starfall/images/player/player_right4.png'),
]
walk_left = [
    pg.image.load('Starfall/images/player/player_left1.png'),
    pg.image.load('Starfall/images/player/player_left2.png'),
    pg.image.load('Starfall/images/player/player_left3.png'),
    pg.image.load('Starfall/images/player/player_left4.png'),
]

player_anim_cnt = 0
player_speed = 10
player_x = 350

while True:
    fps.tick(15)
    screen.blit(bg, (0, 0))

    keys = pg.key.get_pressed()
    if keys[pg.K_a] and player_x >25:
        screen.blit(walk_left[player_anim_cnt], (player_x, 595))
        player_x -= player_speed
    elif keys[pg.K_d] and player_x <675:
        screen.blit(walk_right[player_anim_cnt], (player_x, 595))
        player_x += player_speed  
    else:
        screen.blit(player, (player_x, 595))

    if player_anim_cnt == 3:
        player_anim_cnt = 0
    else :
        player_anim_cnt +=1

    pg.display.update()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()