import time
import datetime
import pygame

pygame.init()

W, H = 800, 800
x = W//2
y = H//2
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))

mickey = pygame.image.load("c:/pp2/TSIS/Lab/Lab7/images/main-clock.png")
leftHand = pygame.image.load("c:/pp2/TSIS/Lab/Lab7/images/left-hand.png").convert_alpha()
rightHand = pygame.image.load("c:/pp2/TSIS/Lab/Lab7/images/right-hand.png").convert_alpha()
mickeyRect = mickey.get_rect()
def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = center).center)
    surf.blit(rotated_image, new_rect)

minangle = 0
secangle = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    time = datetime.datetime.now()
    minuteTime = time.minute
    secondTime = time.second
    minangle = -(minuteTime*6)
    secangle = -(secondTime*6)

    sc.fill(WHITE)
    sc.blit(mickey, (x, y))
    sc.blit(mickey, mickeyRect)
    
    blitRotateCenter(sc, leftHand, (x,y), secangle) 
    blitRotateCenter(sc, rightHand, (x,y), minangle)
    pygame.display.update()
