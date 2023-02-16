# Using what you have learnt about Python programming, you will build a text-based version of the Tic Tac Toe game.
# The game should be playable in the command line just like the Blackjack game we created on Day 11. It should be a
# 2-player game, where one person is "X" and the other plays "O".
#
# TODO: Create a board out of ASCII characters, 3 rows with 3 columns each, which will be stored in a nested list:
#  [[row1], [row2], [row3]]

# Player_1 = 0
# Player_2 = 0
# default_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
# board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
game_on = True

def display_board(board):
    for row in board:
        row_text = '----------\n'
        for char in row:
            row_text += char + " | "
        print(row_text[:-2])

# TODO: Create game loop:
#           - Player 1 starts, makes 1st move. Check win condition.
#           - Player 2 makes their move. Check win condition.
#           - If win triggered, update and display score, reset board. Return to step 1.

while game_on:
    # Reset the board:
    Player_1 = 0
    Player_2 = 0
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    print("Welcome to Tic-Tac-Toe! You are Player 1.")
    display_board(board)

    player_move = input("What is your move?")


