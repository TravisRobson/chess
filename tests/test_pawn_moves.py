from chess.chesstypes import Board, Move, Piece, Player, Position
from chess.moves import find_valid_pawn_moves, get_players_pieces_and_postions


def generate_pawn_moves(board, player):
    pieces, positions = get_players_pieces_and_postions(board, player)

    moves = set()
    for piece, position in zip(pieces, positions):
        if piece == Piece.PAWN:
            moves.union(find_valid_pawn_moves(position, board))

    return moves


def test_white_starting_moves():
    board = Board()

    moves = generate_pawn_moves(board, Player.WHITE)
    expected_moves = set(
        [
            Move("a3", Position("a", 2), Position("a", 3)),
        ]
    )
    assert moves == expected_moves
