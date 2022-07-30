import chess

starting_board_string = """
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

def test_board():
    board = chess.Board()
    board_string = chess.board_to_string(board)
    assert board_string == starting_board_string