# Project 3 - Tic-Tac-Toe Simulator
# Name: Miles Herrman
# Instructor: S. Einakian 
# Section: 3

from tictactoeFuncs import *

if welcome() == 1:
    who_starts = random.randint(0,1)
    game_marks = create_board()
    play_let = pick_letter()
    if play_let == 'X':
        comp_let = 'O'
    else:
        comp_let = 'X'
    print_board(game_marks)
    print(" ")
    if who_starts == 0:
        letter = play_let
        while True:
            if check_win(game_marks, letter) == False:
                print("It's Player 1's (" + play_let + "'s) turn!")
                print(" ")
                game_marks = get_input(play_let, game_marks)
                print_board(game_marks)
                print(" ")
                letter = play_let
            else:
                break
            if check_win(game_marks, letter) == False:
                print("It's the Computer's (" + comp_let + "'s) turn!")
                print(" ")
                game_marks = get_comp_input(comp_let, game_marks)
                print_board(game_marks)
                print(" ")
                letter = comp_let
            else:
                break
    else:  
        letter = comp_let       
        while True:
            if check_win(game_marks, letter) == False:
                print("It's the Computer's (" + comp_let + "'s) turn!")
                print(" ")
                game_marks = get_comp_input(comp_let, game_marks)
                print_board(game_marks)
                print(" ")
                letter = comp_let
            else:
                break
            if check_win(game_marks, letter) == False:
                print("It's Player 1's (" + play_let + "'s) turn!")
                print(" ")
                game_marks = get_input(play_let, game_marks)
                print_board(game_marks)
                print(" ")
                letter = play_let
            else:
                break
                
else:
    who_starts = random.randint(0,1)
    game_marks = create_board()
    play1_let = pick_letter()
    if play1_let == 'X':
        play2_let = 'O'
    else:
        play2_let = 'X'
    print_board(game_marks)
    print(" ")
    if who_starts == 0:
        letter = play1_let
        while True:
            if check_win(game_marks, letter) == False:
                print("It's Player 1's (" + play1_let + "'s) turn!")
                print(" ")
                game_marks = get_input(play1_let, game_marks)
                print_board(game_marks)
                print(" ")
                letter = play1_let
            else:
                break
            if check_win(game_marks, letter) == False:
                print("It's Player 2's (" + play2_let + "'s) turn!")
                print(" ")
                game_marks = get_input(play2_let, game_marks)
                print_board(game_marks)
                print(" ")
                letter = play2_let
            else:
                break
    else:  
        letter = play2_let       
        while True:
            if check_win(game_marks, letter) == False:
                print("It's Player 2's (" + play2_let + "'s) turn!")
                print(" ")
                game_marks = get_input(play2_let, game_marks)
                print_board(game_marks)
                print(" ")
                letter = play2_let
            else:
                break
            if check_win(game_marks, letter) == False:
                print("It's Player 1's (" + play1_let + "'s) turn!")
                game_marks = get_input(play1_let, game_marks)
                print_board(game_marks)
                print(" ")
                letter = play1_let
            else:
                break