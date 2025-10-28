import pytest
from src.main import ChessBoard

def test_move_piece():
    board = ChessBoard()
    start = (6, 0)
    end = (4, 0)
    board.move_piece(start, end)
    assert board.board[4][0] == 'p'