# Using what you have learnt about Python programming, you will build a text-based version of the Tic Tac Toe game.
# The game should be playable in the command line just like the Blackjack game we created on Day 11. It should be a
# 2-player game, where one person is "X" and the other plays "O".
#
# TODO: Create a board out of ASCII characters, 3 rows with 3 columns each, which will be stored in a nested list:
#  [[row1], [row2], [row3]]

# board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
import random

def display_board(board):
    for row in board:
        row_text = '----------\n'
        for char in row:
            row_text += char + " | "
        print(row_text[:-2])

def check_win(board):
    # Check Horizontals
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != '-':
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != '-':
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != '-':
        return True

    # Check Verticals
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != '-':
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != '-':
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != '-':
        return True

    # Check Cross
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return True

    else:
        return False

def player_2_move(board):
    for x in [0, 1, 2]:
        for y in [0, 1, 2]:
            if board[x][y] == '-':
                if random.choice([0, 1, 2, 3]) > 1:
                    return True

while True:
    ttt_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    print("Welcome to Tic-Tac-Toe! You are Player 1.")
    while True:
        display_board(ttt_board)
        # Player 1 move
        while True:
            player_move = input('What is your move? row# + col#: 00, 01, 21, etc.:')
            if player_move not in ['00', '01', '02', '10', '11', '12', '20', '21', '22']:
                print("Invalid input.")
            else:
                row = int(player_move[0])
                col = int(player_move[1])
                if ttt_board[row][col] == '-':
                    ttt_board[row][col] = 'x'
                    break
        # Check win condition
        print(check_win(ttt_board))
        if check_win(ttt_board):
            print("Player 1 Wins!")
            display_board(ttt_board)
            print('============================================\n')
            break

        # Player 2 move
        player_2_move(ttt_board)

        # Check board spot

        # Check win condition
        # if check_win(ttt_board):
        #     print("Player 2 Wins!")
        #     break
