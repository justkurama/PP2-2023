import pygame
pygame.init()

screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("MY GAME")

icon = pygame.image.load('PP2 project/Images/icon.png')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 50))
square.fill((171, 38, 237))

run = True
while run :
    screen.fill((237, 180, 24))

    screen.blit(square, (100, 200))
    pygame.draw.circle(screen, (171, 38, 237), (50, 50), 25)


    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            run = False

    