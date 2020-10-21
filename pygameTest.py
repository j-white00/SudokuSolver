import pygame
pygame.init()

WHITE = (255,255,255)

running = True
while running:
    win = pygame.display.set_mode((500,500))
    win.fill(WHITE)
    for event in pygame.event.get():
        pygame.display.update()
        if event.type == pygame.QUIT:
            running = False
pygame.quit()