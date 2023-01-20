import pygame
pygame.init()
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Tic Tac Toe")

board = pygame.Surface((440, 440))
board.fill((161, 104, 53))

fence = pygame.image.load('Tic Tac Toe/Images/fence.png')

running = True
while running :
    screen.fill((255, 231, 209))
    screen.blit(board, (5, 5))
    screen.blit(fence, (5, 5))
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            run = False