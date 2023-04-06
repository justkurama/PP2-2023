import time
import pygame as pg
pg.init()

despacitoPath = "c:/pp2/TSIS/Lab/Lab7/sound/Despacito.mp3"
mozzartPath = "c:/pp2/TSIS/Lab/Lab7/sound/TSIS7_Lab7_mp3_DrillRemix.mp3"
boomPath = "c:/pp2/TSIS/Lab/Lab7/sound/TSIS7_Lab7_mp3_3NBSQ2N-explosions.mp3"
sc = pg.display.set_mode((480, 360))
pg.display.set_caption("mp3 player")
clock = pg.time.Clock()
despacito = pg.mixer.music.load(despacitoPath)
musicList = [despacitoPath, mozzartPath, boomPath]
pg.mixer.music.play(-1)

flPlay = False
run = True
index = 0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                flPlay = not flPlay
                if flPlay:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key == pg.K_RIGHT:
                
                index += 1
                if index == len(musicList):
                    index = 0
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(musicList)-1
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()


    pg.display.flip()
    clock.tick(60)