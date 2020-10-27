import pygame, sys, time
from pygame.locals import *
from random import shuffle, randint

col_white = (255, 255, 255) # rgb white
col_grey = (211, 211,  211) # rgb grey
col_black = (0, 0, 0)       # rgb black
col_green = (173, 255, 47)  # rgb green
win_size = 495  # window size x and y in pixels
big_square_size = win_size // 3 # size of larger squares on board
mini_square_size = big_square_size // 3 # size of smaller sqaues inside of larger squares

board_new =[[0, 0, 0, 0, 0, 0, 0, 0, 0], # empty board holding 0 as blank value
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def valid(board, num, pos): # checks if number enterd is valid compared to, row, column and large sqaure
    for i in range(len(board[0])): # row check
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    for j in range(len(board)): # colum check
        if board[j][pos[1]] == num and pos[0] != j:
            return False
    
    box_x = pos[1] // 3 # check box
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def locate_empty(board): # locates next empty cell on board and returns its y, x.
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # y, x as board is accessed by row then column.
    return False

def sudoku_solve(board): # uses backtracking algorythrm to recursivly solve the board.
    find = locate_empty(board)
    if not find: # if no empty spaces are found returns Ture and method ends.
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve:
                draw_cube(i, row, col)
            if sudoku_solve(board):
                return True
            board[row][col] = 0
    return False

def populate(board):
    num_list = [1,2,3,4,5,6,7,8,9]
    shuffle(num_list)
    board[0] = num_list

def remove_tiles(board):
    #min clues      17 max clues    45
    #max delTiles   64 min delTiles 36
    del_tiles = randint(36, 64)
    while del_tiles !=0:
        row = randint(0,8)
        col = randint(0,8)
        if board[row][col] != 0:
            board[row][col] = 0
            del_tiles -= 1

def display_num(num, position):
        font = pygame.font.SysFont('arial', 50)
        text = font.render(str(num), True, (0, 0, 0))
        win_display.blit(text, position)
        pygame.display.update()

def draw(board):
    win_display.fill(col_white)
    for x in range(0, win_size, mini_square_size):
        pygame.draw.line(win_display, col_grey, (x, 0), (x, win_size))
    for y in range(0, win_size, mini_square_size):
        pygame.draw.line(win_display, col_grey, (0, y), (win_size, y))
    for x in range(165, win_size, big_square_size):
        pygame.draw.line(win_display, col_black, (x, 0), (x, win_size), 2)
    for y in range(165, win_size, big_square_size):
        pygame.draw.line(win_display, col_black, (0, y), (win_size, y), 2)
    draw_nums(board)

def draw_cube(i, row, col):
    pygame.time.delay(50)
    pygame.draw.rect(win_display, col_green, (col*55+2, row*55+2, 53, 53))
    display_num(i, (col*55 + 15, row*55))
    time.sleep(0.1)
    pygame.draw.rect(win_display, col_grey, (col*55+2, row*55+2, 53, 53))
    display_num(i, (col*55 + 15, row*55))
    
def draw_nums(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] != 0):
              display_num(board[i][j], (j*55 + 15, i*55))
            else:
              display_num("", (j*55 + 15, i*55))

def main():
    global win_clock, win_display, solve
    pygame.init()
    pygame.display.set_caption("Sudoku Solve - Press Space to Solve!")
    win_clock = pygame.time.Clock()
    win_display = pygame.display.set_mode((win_size, win_size))
    solve = False
    populate(board_new)
    sudoku_solve(board_new)
    remove_tiles(board_new)
    draw(board_new)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_SPACE]):
            pygame.display.set_caption("Sudoku Solve - Solving...")
            solve = True
            sudoku_solve(board_new)
            pygame.display.set_caption("Sudoku Solve - Solved!")
        pygame.display.update()
        win_clock.tick(5)
    pygame.quit()

if __name__ == "__main__":
    main()