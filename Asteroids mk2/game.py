import pygame as pg
pg.init()

screenh = 728
screenw = 409
screen = pg.display.set_mode((screenw, screenh))
clock = pg.time.Clock()

icon = pg.image.load('Asteroids mk2/asteroidsPics/asteroid100.png')
pg.display.set_icon(icon)
pg.display.set_caption('Asteroids')

bg = pg.image.load('Asteroids mk2 mk2/asteroidsPics/spacebg.png')
alienImg = pg.image.load('Asteroids mk2/asteroidsPics/alienShip.png')
playerRocket = pg.image.load('Asteroids mk2/asteroidsPics/spaceRocket.png')
star = pg.image.load('Asteroids mk2/asteroidsPics/star.png')
asteroid50 = pg.image.load('Asteroids mk2/asteroidsPics/asteroid50.png')
asteroid100 = pg.image.load('Asteroids mk2/asteroidsPics/asteroid100.png')
asteroid150 = pg.image.load('Asteroids mk2/asteroidsPics/asteroid150.png')

shoot = pg.mixer.Sound('Asteroids mk2/sounds/shoot.wav')
bangLargeSound = pg.mixer.Sound('Asteroids mk2/sounds/bangLarge.wav')
bangSmallSound = pg.mixer.Sound('Asteroids mk2/sounds/bangSmall.wav')
shoot.set_volume(.25) 
bangLargeSound.set_volume(.25)
bangSmallSound.set_volume(.25)

HP = 5
run = True

while run:
    clock.tick(60)



