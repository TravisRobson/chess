from chesstypes import Piece, Player


def is_game_over(board, whose_turn):
    # TODO implement
    return False


def update_board(board, move):
    # TODO implement
    return board


def __find_valid_king_moves(postion, board):
    # TODO implement
    moves = []

    return moves


def __find_valid_queen_moves(postion, board):
    # TODO implement
    moves = []

    return moves


def __find_valid_rook_moves(postion, board):
    # TODO implement
    moves = []

    return moves


def __find_valid_bishop_moves(postion, board):
    # TODO implement
    moves = []

    return moves


def __find_valid_knight_moves(postion, board):
    # TODO implement
    moves = []

    return moves


def __find_valid_pawn_moves(postion, board):
    # TODO implement
    moves = []

    return moves


def find_valid_moves(board, whose_turn):
    if whose_turn == Player.WHITE:
        pieces = board.white_pieces
        positions = board.white_positions
    else:
        pieces = board.black_pieces
        positions = board.black_positions

    moves = []
    for piece, position in zip(pieces, positions):
        if piece == Piece.KING:
            moves.append(__find_valid_king_moves(position, board))
        elif piece == Piece.QUEEN:
            moves.append(__find_valid_queen_moves(position, board))
        elif piece == Piece.ROOK:
            moves.append(__find_valid_rook_moves(position, board))
        elif piece == Piece.BISHOP:
            moves.append(__find_valid_bishop_moves(position, board))
        elif piece == Piece.KNIGHT:
            moves.append(__find_valid_knight_moves(position, board))
        elif piece == Piece.PAWN:
            moves.append(__find_valid_pawn_moves(position, board))
        else:
            raise TypeError(f"Piece has invalid type {piece}")

    # TODO Remove any moves that puts current player's king in check
    # TODO Are there any stalemate considerations?

    return moves
