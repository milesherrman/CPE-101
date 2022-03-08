# Project 3 - Tic-Tac-Toe Simulator
# Name: Miles Herrman
# Instructor: S. Einakian 
# Section: 3

import random

#Purpose: Print welcome message/game rules, then take an input for number of players
def welcome() -> int:
    print("")
    print("Hello! Welcome to Tic-Tac-Toe!")
    print("")
    print("How to Play:")
    print("   The game starts with an empty 3x3 grid.")
    print("   Players take turns putting an X or an O in open squares.")
    print("   The first player to get 3 of your own marks in a row is the winner")
    print("   (vertically, horizontally, or diagonally).")
    print("   When a player wins or the board is filled with no winner,")
    print("   the game is over")
    print("")
    num_players = 0
    while num_players != "1" and num_players != "2":
        num_players = input("How many people are playing [1 or 2]? ")
        if num_players != "1" and num_players != "2":
            print("Please enter a valid number of players.")
    return int(num_players)
 
#Purpose: Print out board with gameplay positions in each square + create an empty list to store player moves 
def create_board() -> list:
    starting_marks = ["1","2","3","4","5","6","7","8","9"]
    print(" ")
    print("{1:1s}{0:}{2:1s}{0:}{3:1s}".format(" | ", starting_marks[0], starting_marks[1], starting_marks[2]))
    print("---------")
    print("{1:1s}{0:}{2:1s}{0:}{3:1s}".format(" | ", starting_marks[3], starting_marks[4], starting_marks[5]))
    print("---------")
    print("{1:1s}{0:}{2:1s}{0:}{3:1s}".format(" | ", starting_marks[6], starting_marks[7], starting_marks[8]))
    print(" ")
    starting_marks = [""] * 9
    return starting_marks

#Purpose: Pass it all player moves and print out the current game board
def print_board(game_marks: list): 
    print("{1:1s}{0:}{2:1s}{0:}{3:1s}".format(" | ", game_marks[0], game_marks[1], game_marks[2]))
    print("---------")
    print("{1:1s}{0:}{2:1s}{0:}{3:1s}".format(" | ", game_marks[3], game_marks[4], game_marks[5]))
    print("---------")
    print("{1:1s}{0:}{2:1s}{0:}{3:1s}".format(" | ", game_marks[6], game_marks[7], game_marks[8]))

#Purpose: Ask player to choose a letter
def pick_letter() -> str:
    letter = input("Player 1, choose a letter [X or O]: ").upper()
    while letter != 'X' and letter != 'O':
        print("Please enter a valid letter. ")
        letter = input("Choose a letter [X or O]: ").upper()
    print(" ")
    return letter

#Purpose: Get user input for their next move, check to ensure valid move
def get_input(letter: str, game_marks: list) -> list:
    next_move = int(input("Where do you want to place your next letter? (Enter a value 1-9) "))
    while next_move < 1 or next_move > 9 or game_marks[next_move - 1] != "":
        print("Invalid move! Please try again.")
        next_move = int(input("Where do you want to place your next letter? (Enter a value 1-9) "))
    game_marks[next_move - 1] = letter
    print(" ")
    return game_marks

#Purpose: Randomly select the next move for the computer from a list of available moves
def get_comp_input(letter: str, game_marks: list) -> list:
    list_of_moves = []
    for idx in range(len(game_marks)):
        if game_marks[idx] == "":
            list_of_moves.append(idx + 1)
    if len(list_of_moves) == 1:
        game_marks[list_of_moves[0] - 1] = letter
    else:
        next_move = list_of_moves[random.randrange(0,len(list_of_moves) - 1)]
        game_marks[next_move - 1] = letter
    return game_marks

#Purpose: Check each row for a win
def check_rows(game_marks: list) -> bool:
    if game_marks[0] == game_marks[1] == game_marks[2] != "":
        return True
    elif game_marks[3] == game_marks[4] == game_marks[5] != "":
        return True
    elif game_marks[6] == game_marks[7] == game_marks[8] != "":
        return True
    else: 
        return False

#Purpose: Check each column for a win
def check_cols(game_marks: list) -> bool:
    if game_marks[0] == game_marks[3] == game_marks[6] != "":
        return True
    elif game_marks[1] == game_marks[4] == game_marks[7] != "":
        return True
    elif game_marks[2] == game_marks[5] == game_marks[8] != "":
        return True
    else: 
        return False

#Purpose: Check each diagonal for a win
def check_diags(game_marks: list) -> bool:
    if game_marks[0] == game_marks[4] == game_marks[8] != "":
        return True
    elif game_marks[2] == game_marks[4] == game_marks[6] != "":
        return True
    else: 
        return False

#Purpose:        
def board_full(game_marks: list) -> bool:
    for spot in game_marks:
        if spot == "":
            return False
    return True

#Purpose: Check all possible "win" functions and print result if any of them return true
def check_win(game_marks: list, letter: str) -> bool:
    if check_rows(game_marks) == True or check_cols(game_marks) == True or check_diags(game_marks) == True:
        print(letter, " is the winner!")
        print(" ")
        return True
    elif board_full(game_marks) == True:
        print("It's a draw! You're both losers!")
        print(" ")
        return True
    return False