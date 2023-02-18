# A simple python script that emulates a typical game of Tic-Tac-Toe using in-line commands.
# Player 1 plays first as 'x' and Player 2 is 'o' and will be randomly simulated actions.


# I approached the project by first creating an actionable plan of steps that I can logically follow. Such
# as making a list of functionality that need to be coded in order. After following through with the list
# and creating each part, I noted down which sections needed work and what additional work needed to be added
# that was not noticed initially. Each section was tested for correct functionality as soon as they were written.
# After full functionality was achieved, I went back and cleaned up each section and added commentary.
#
# Easiest parts were following through with the action plan and coding section by section. The hard part
# was coming up with a logical plan that could be followed. Future improvements would include updating the
# Player 2 "AI" to make better choices as well as including a score counter. If I were to tackle this project
# again, I would try to simplify/improve the game loop and see if there is a better way other than using
# while loops and breaks.


import random
import time

game_on = True

# Prints out the boards current state
def display_board(board):
    for row in board:
        row_text = '----------\n'
        for char in row:
            row_text += char + " | "
        print(row_text[:-2])

# Checks all possible win conditions
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

# Randomly chooses next move for Player 2 based on current board state
def player_2_move(board):
    possible_moves = []
    for x in [0, 1, 2]:
        for y in [0, 1, 2]:
            if board[x][y] == '-':
                possible_moves.append((x, y))
    player2_move = random.choice(possible_moves)
    return player2_move

# Main game loop while game_on is True
while game_on:
    ttt_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    print("Welcome to Tic-Tac-Toe! You are Player 1.")
    while game_on:
        display_board(ttt_board)
        # Player 1 move
        while True:
            player_move = input('What is your move? row# + col#: 00, 01, 21, etc. or "quit" to stop playing:')
            if player_move == "quit":
                game_on = False
                print("Thank you for playing.")
                break
            if player_move not in ['00', '01', '02', '10', '11', '12', '20', '21', '22']:
                print("Invalid input. Enter 2 valid numbers.")
            else:
                row = int(player_move[0])
                col = int(player_move[1])
                if ttt_board[row][col] == '-':
                    ttt_board[row][col] = 'x'
                    break
                else:
                    print("Invalid input. That spot is taken.")

        # Check win condition
        if check_win(ttt_board):
            print("Player 1 Wins!")
            display_board(ttt_board)
            print('============================================\n')
            time.sleep(2)
            break

        # Player 2 move & win check
        p2_move = player_2_move(ttt_board)
        ttt_board[p2_move[0]][p2_move[1]] = 'o'
        if check_win(ttt_board):
            print("Player 2 Wins! Try again.")
            display_board(ttt_board)
            print('============================================\n')
            time.sleep(2)
            break
