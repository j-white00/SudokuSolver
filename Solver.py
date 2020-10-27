import pygame, sys
from pygame.locals import *
from random import shuffle, randint

col_white = (255, 255, 255)
col_grey = (211, 211,  211)
col_black = (0, 0, 0)
col_green = (173, 255, 47)
win_size = 495
big_square_size = win_size // 3
mini_square_size = big_square_size // 3

board_new =[[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def print_out(board):
    for i in range(len(board)):
        if i!=0 and i%3 == 0:
            print ("- - - + - - - + - - -")
        for j in range(len(board[0])):
            if j !=0 and j % 3 == 0:
                print ("| ", end = "")
            if j == 8:
                 print(board[i][j])
            else:
                 print(str(board[i][j]) + " ", end="")

def valid(board, num, pos):
    # row check
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    # colum check
    for j in range(len(board)):
        if board[j][pos[1]] == num and pos[0] != j:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def locate_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # y, x
    return False

# def display_cube(row, col):
#     if prev_pos:
#         win_display.blit(bk_sq, prev_pos)
#     prev_pos = (row, col)
#     bk_sq.blit(win_display, (0, 0), (*prev_pos, 55, 55))
#     pygame.draw.rect(win_display, col_green, (row, col, 10, 10))

def sudoku_solve(board):
    find = locate_empty(board)
    if not find:
        return True
    else:
        row, col = find
        #display a cube and copy a backup of board without select square, alsom update board backup with correct numbers but no select square.
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

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
    del_tiles = randint(36, 40)
    #del_tiles = randint(36, 64)
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
    for x in range(0, win_size, mini_square_size):
        pygame.draw.line(win_display, col_grey, (x, 0), (x, win_size))

    for y in range(0, win_size, mini_square_size):
        pygame.draw.line(win_display, col_grey, (0, y), (win_size, y))

    for x in range(165, win_size, big_square_size):
        pygame.draw.line(win_display, col_black, (x, 0), (x, win_size), 2)

    for y in range(165, win_size, big_square_size):
        pygame.draw.line(win_display, col_black, (0, y), (win_size, y), 2)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] != 0):
                display_num(board[i][j], (i*55 + 15, j*55))
            else:
                display_num("", (i*55 + 16, j*55))

def main():
    global win_clock, win_display
    populate(board_new)
    sudoku_solve(board_new)
    remove_tiles(board_new)
    pygame.init()
    pygame.display.set_caption("Sudoku Solve")
    win_clock = pygame.time.Clock()
    win_display = pygame.display.set_mode((win_size, win_size))
    win_display.fill(col_white)
    draw(board_new)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        win_clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()

# sudoku_solve(board_new)
# print_out(board_new)
