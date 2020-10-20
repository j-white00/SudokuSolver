import turtle
from random import shuffle, randint

myPen = turtle.Turtle

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
            print ("- - - - - - - - - - -")
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
    
def sudoku_solve(board):
    find = locate_empty(board)
    if not find:
        return True
    else:
        row, col = find

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
    del_tiles = randint(36, 64)
    print("  Tiles Missing:", del_tiles, "\n=====================")
    while del_tiles !=0:
        row = randint(0,8)
        col = randint(0,8)
        if board[row][col] != 0:
            board[row][col] = 0
            del_tiles -= 1

populate(board_new)
sudoku_solve(board_new)
print("\n----|| Sudoku! ||----\n=====================")
remove_tiles(board_new)
print_out(board_new)
while True:
    solved = input('\nType "Solve" to reveal solution: ')
    if(solved == "Solve" or solved == "solve"):
        break
print("\n    Solved Board\n=====================")
sudoku_solve(board_new)
print_out(board_new)