#!/usr/bin/env python3
"""Coordinate chess game

Currently, assume human user is always white.
"""
# pylint: disable=missing-function-docstring, import-error

from boardview import display_board
from chesstypes import Board, Player
from moves import find_valid_moves, is_game_over, update_board
from opponent import opponent_choose_move


def ask_user_for_move(valid_moves):
    move_string_invalidated = input("What move do you want to play? ")
    return move_string_invalidated


def switch_turns(whose_turn):
    if whose_turn == Player.WHITE:
        print("Black's turn.")
        return Player.BLACK
    else:
        print("White's turn.")
        return Player.WHITE


def main():
    board = Board()
    display_board(board)
    print("White's turn.")

    whose_turn = Player.WHITE
    infinite_loop_counter = 0
    # One move per loop
    while not is_game_over(board, whose_turn):
        valid_moves = find_valid_moves(board, whose_turn)
        if whose_turn == Player.WHITE:
            move = ask_user_for_move(valid_moves)
        else:
            move = opponent_choose_move(board, valid_moves)

        board = update_board(board, move)
        display_board(board)

        whose_turn = switch_turns(whose_turn)

        infinite_loop_counter += 1
        if infinite_loop_counter > 500:
            raise RuntimeError("Infinite loop detected.")


if __name__ == "__main__":
    main()
