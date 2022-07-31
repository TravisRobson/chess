#!/usr/bin/env python3

"""
Currently, assume human user is always white.
"""

from boardview import display_board
from chesstypes import Board, Player
from moves import is_game_over, find_valid_moves, update_board
from opponent import opponent_choose_move


def ask_user_for_move(valid_moves):
    move_string_invalidated = input("What move do you want to play?")
    return move_string_invalidated


def main():
    board = Board()
    display_board(board)
    print("White's turn.")

    whose_turn = Player.WHITE
    while not is_game_over(board, whose_turn):

        valid_moves = find_valid_moves(board, whose_turn)
        if whose_turn == Player.WHITE:
            move = ask_user_for_move(valid_moves)
        else:
            move = opponent_choose_move(valid_moves)

        board = update_board(board, move)
        display_board(board)

        if whose_turn == Player.WHITE:
            whose_turn = Player.BLACK
            print("Black's turn.")
        else:
            whose_turn = Player.WHITE
            print("White's turn.")


if __name__ == "__main__":
    main()
