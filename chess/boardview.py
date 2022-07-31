"""Display chess board to terminal"""
import os
from copy import deepcopy

# Whitespace matters in SQUARES
BLANK_BOARD = list(
    """
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
"""
)


def __increment_by_row(prev_total):
    """Increment index so that cursor is on next board row."""
    total = prev_total + 33 + 2 + 1  # |   |   | 8 and "\n" line
    total += 33 + 1  # +---+ etc and "\n" line
    return total


ROW_START_TO_BOARD_STR_INDEX = {}


def __map_row_start_to_indices():
    total = 1  # "\n" is first character in SQUARES
    total += 33 + 1  # +---+ etc and "\n" line

    for row in range(8, 1, -1):
        ROW_START_TO_BOARD_STR_INDEX[row] = total
        total = __increment_by_row(total)

    ROW_START_TO_BOARD_STR_INDEX[1] = total


__map_row_start_to_indices()


def __piece_to_string(piece):
    strings = ["K", "Q", "R", "B", "N", "P"]
    return strings[piece]


def __column_to_str_offset(column):
    return 2 + 4 * (ord(column) - ord("a"))


def __place_pieces(pieces, positions, board_string):
    for piece, position in zip(pieces, positions):
        index = ROW_START_TO_BOARD_STR_INDEX[position.row] + __column_to_str_offset(
            position.col
        )
        assert index < len(
            BLANK_BOARD
        ), f"Index ({index}) exceeds SQUARES str length ({len(BLANK_BOARD)})."
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
        board_string[index] = __piece_to_string(piece)


def board_to_string(board):
    """Create string for board with pieces"""
    board_string = deepcopy(BLANK_BOARD)

    __place_pieces(board.white_pieces, board.white_positions, board_string)
    __place_pieces(board.black_pieces, board.black_positions, board_string)

    return "".join(board_string)


def display_board(board):
    """Display board to terminal."""
    # Clear terminal screen, Unix only
    os.system("clear")  # nosec B605, B607
    print(board_to_string(board))
