import pygame, sys
from pygame.locals import *

col_white = (255, 255, 255)
col_black = (0, 0, 0)

def main():
    global win_clock, win_display
    pygame.init()
    pygame.display.set_caption("Sudoku Solver")
    win_clock = pygame.time.Clock()
    win_display = pygame.display.set_mode((500, 500))

    running = True
    while running:
        win_display.fill(col_white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        win_clock.tick(5)
    pygame.quit()

if __name__ == "__main__":
    main()
