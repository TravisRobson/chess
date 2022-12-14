from chess.boardview import board_to_string
from chess.chesstypes import Board

STARTING_BOARD_STRING = """
+---+---+---+---+---+---+---+---+
| R | N | B | Q | K | B | N | R | 8
+---+---+---+---+---+---+---+---+
| P | P | P | P | P | P | P | P | 7
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 6
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 5
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 4
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 3
+---+---+---+---+---+---+---+---+
| P | P | P | P | P | P | P | P | 2
+---+---+---+---+---+---+---+---+
| R | N | B | Q | K | B | N | R | 1
+---+---+---+---+---+---+---+---+
  a   b   c   d   e   f   g   h
"""


def test_starting_board():
    """Ensure we can reproduce starting board."""
    board = Board()
    board_string = board_to_string(board)
    assert board_string == STARTING_BOARD_STRING
