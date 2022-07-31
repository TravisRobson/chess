#!/usr/bin/env python3
"""Coordinate chess game"""
# pylint: disable=missing-function-docstring, import-error

from boardview import display_board
from chesstypes import Board


def main():
    board = Board()
    display_board(board)


if __name__ == "__main__":
    main()
