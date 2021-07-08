from random import randrange
import time

# create logical board
options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board_squares = [[i for i in range(3)] for j in range(3)]  # create a 3 by 3 list
square = 0  # variable to hold list assignment
for i in range(3):
    for j in range(3):
        square += 1
        board_squares[i][j] = square  # update list with numbers from 1 - 9


# creates 3x3 board and fill with numbers from list named board_squares
def display_board():
    for i in range(3):
        print('+-----------' * 3, end='+\n')
        print('|           ' * 3, end='|\n|')
        for j in range(3):
            a = '     ' + str(board_squares[i][j]) + '     |'  # creates middle line with numbers
            print(a, end='')
        print()
        print('|           ' * 3, end='|\n')
    print('+-----------' * 3, end='+\n')


# Takes input from user and writes to the game board
def user_move():
    move = int(input('Please enter the corresponding number to the box on the board: '))
    while move not in options:
        move = int(input('NOT AN OPTION!!!\nPlease enter the corresponding number to the box on the board: '))
    int(move)
    for i in range(3):
        for j in range(3):
            if board_squares[i][j] == move:
                board_squares[i][j] = 'O'  # updates game board
                options[move - 1] = 'O'  # updates options left
    display_board()


# chooses a random number and ensures it it a valid number and writes to the game board
def computer_move():
    move = 0
    while move not in options:  # checks if number is in list
        for i in range(10):
            move = randrange(8)  # chooses random number between 1 and 9
    for i in range(3):
        for j in range(3):
            if board_squares[i][j] == move:
                board_squares[i][j] = 'X'  # updates game board
                options[move - 1] = 'X'  # updates options left
    display_board()


def board_status():
    for i in range(3):
        if board_squares[i][0] == board_squares[i][1] == board_squares[i][2]:
            return 'Winner'
    for i in range(3):
        if board_squares[0][i] == board_squares[1][i] == board_squares[2][i]:
            return 'Winner'
    if board_squares[0][0] == board_squares[1][1] == board_squares[2][2] or \
            board_squares[2][0] == board_squares[1][1] == board_squares[0][2]:
        return 'Winner'


while True:
    #  display_board()
    time.sleep(1)
    computer_move()
    if board_status() == 'Winner':
        print('You LOST game over!!!!!')
        break
    user_move()
    if board_status() == 'Winner':
        print('You WON game over!!!!!')
        break
