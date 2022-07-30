#!/usr/bin/env python3

from copy import deepcopy
from dataclasses import dataclass
from enum import IntEnum, unique
import os

# Whitespace matters in SQUARES
SQUARES = list("""
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 8
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 7
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 6
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 5
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 4
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 3
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 2
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 1
+---+---+---+---+---+---+---+---+
  a   b   c   d   e   f   g   h
""")


def increment_by_row(prev_total):
    total = prev_total + 33 + 2 + 1 # |   |   | 8 and "\n" line
    total += 33 + 1 # +---+ etc and "\n" line
    return total


total = 1 # "\n" is first character in SQUARES
total += 33 + 1 # +---+ etc and "\n" line

ROW_START_INDEX = dict()

for row in range(8, 1, -1):
    ROW_START_INDEX[row] = total
    total = increment_by_row(total)

ROW_START_INDEX[1] = total


@unique
class Piece(IntEnum):
    """Integers index into static arrays"""
    King = 0
    Queen = 1
    Rook = 2
    Bishop = 3
    Knight = 4
    Pawn = 5


def piece_to_string(piece):
    strings = ["K", "Q", "R", "B", "N", "P"]
    return strings[piece]


@dataclass
class Position:
    """Order (col, row) matches standard chess notation"""
    col: str
    row: int


class Board:
    """Intended to be a simple struct-like object"""
    def __init__(self):
        self.white_pieces = [
            Piece.Rook,
            Piece.Knight,
            Piece.Bishop,
            Piece.Queen,
            Piece.King,
            Piece.Bishop,
            Piece.Knight,
            Piece.Rook,
            Piece.Pawn,
            Piece.Pawn,
            Piece.Pawn,
            Piece.Pawn,
            Piece.Pawn,
            Piece.Pawn,
            Piece.Pawn,
            Piece.Pawn,
        ]
        assert self.white_pieces.count(Piece.King) == 1
        assert self.white_pieces.count(Piece.Queen) == 1
        assert self.white_pieces.count(Piece.Rook) == 2
        assert self.white_pieces.count(Piece.Bishop) == 2
        assert self.white_pieces.count(Piece.Knight) == 2
        assert self.white_pieces.count(Piece.Pawn) == 8
        self.black_pieces = deepcopy(self.white_pieces)

        self.white_positions = [
            Position("a", 8),
            Position("b", 8),
            Position("c", 8),
            Position("d", 8),
            Position("e", 8),
            Position("f", 8),
            Position("g", 8),
            Position("h", 8),
            Position("a", 7),
            Position("b", 7),
            Position("c", 7),
            Position("d", 7),
            Position("e", 7),
            Position("f", 7),
            Position("g", 7),
            Position("h", 7),
        ]
        assert len(self.white_positions) == len(self.white_pieces)

        self.black_positions = [
            Position("a", 1),
            Position("b", 1),
            Position("c", 1),
            Position("d", 1),
            Position("e", 1),
            Position("f", 1),
            Position("g", 1),
            Position("h", 1),
            Position("a", 2),
            Position("b", 2),
            Position("c", 2),
            Position("d", 2),
            Position("e", 2),
            Position("f", 2),
            Position("g", 2),
            Position("h", 2),
        ]
        assert len(self.black_positions) == len(self.black_pieces)


def column_to_str_offset(column):
    return 2 + 4 * (ord(column) - ord("a"))


def place_pieces(pieces, positions, board_string):
    for piece, position in zip(pieces, positions):
        index = ROW_START_INDEX[position.row] + column_to_str_offset(position.col)
        assert index < len(SQUARES), \
            f"Index ({index}) exceeds SQUARES str length ({len(SQUARES)})."
        if board_string[index] != " ":
            print(
                (
                    "Attempted to place piece in filled square "
                    f"'{repr(board_string[index])}'."
                )
            )
            board_string[index] = "X"
            print("".join(board_string))
            raise RuntimeError
        board_string[index] = piece_to_string(piece)


def board_to_string(board):
    board_string = deepcopy(SQUARES)

    place_pieces(board.white_pieces, board.white_positions, board_string)
    place_pieces(board.black_pieces, board.black_positions, board_string)

    return "".join(board_string)


def display_board_to_terminal(board):
    os.system("clear") # Clear terminal screen, Unix only
    print(board_to_string(board))


def main():
    board = Board()
    display_board_to_terminal(board)


if __name__ == "__main__":
    main()
