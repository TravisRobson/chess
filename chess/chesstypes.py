"""Define basic data types for chess"""
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum, IntEnum, unique


@unique
class Player(Enum):
    """Only two players..."""

    WHITE = "White"
    BLACK = "Black"


@unique
class Piece(IntEnum):
    """Integers index into static arrays"""

    KING = 0
    QUEEN = 1
    ROOK = 2
    BISHOP = 3
    KNIGHT = 4
    PAWN = 5


@dataclass(frozen=True)
class Position:
    """Order (col, row) matches standard chess notation"""

    col: str
    row: int


class Board:
    """Intended to be a simple struct-like object"""

    def __init__(self):
        self.white_pieces = [
            Piece.ROOK,
            Piece.KNIGHT,
            Piece.BISHOP,
            Piece.QUEEN,
            Piece.KING,
            Piece.BISHOP,
            Piece.KNIGHT,
            Piece.ROOK,
        ]
        self.white_pieces.extend([Piece.PAWN] * 8)
        assert self.white_pieces.count(Piece.KING) == 1
        assert self.white_pieces.count(Piece.QUEEN) == 1
        assert self.white_pieces.count(Piece.ROOK) == 2
        assert self.white_pieces.count(Piece.BISHOP) == 2
        assert self.white_pieces.count(Piece.KNIGHT) == 2
        assert self.white_pieces.count(Piece.PAWN) == 8
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


@dataclass(frozen=True)
class Move:
    """Frozen so that we can store in a set of moves."""

    algebraic_notation: str
    start_position: Position
    stop_position: Position
