import pygame
pygame.init()
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("MY GAME")
icon = pygame.image.load('PP2 project/Images/icon.png')
pygame.display.set_icon(icon)
run = True
while run :
    screen.fill((237, 180, 24))
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            run = False