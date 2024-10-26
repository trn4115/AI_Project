import numpy as np
from game.utils import get_valid_locations, evaluate_window, score_position
from game.board import create_board, drop_piece


# Test retrieving valid columns for placing a piece
def test_get_valid_locations():
    board = create_board()
    valid_locations = get_valid_locations(board)
    # Initially, all columns should be valid since the board is empty
    assert valid_locations == list(range(7))  # 7 columns expected

    # Fill up the first column and check again
    for row in range(6):
        drop_piece(board, row, 0, 1)  # Fill column 0
    valid_locations = get_valid_locations(board)
    # Column 0 should no longer be a valid location
    assert 0 not in valid_locations


# Test evaluating a window of four slots for scoring
def test_evaluate_window():
    # Case 1: Four consecutive pieces for player 1 (a win scenario)
    window = [1, 1, 1, 1]
    assert evaluate_window(window, 1) == 100

    # Case 2: Three consecutive pieces and one empty slot for player 1
    window = [1, 1, 1, 0]
    assert evaluate_window(window, 1) == 5

    # Case 3: Two consecutive pieces and two empty slots for player 1
    window = [1, 1, 0, 0]
    assert evaluate_window(window, 1) == 2

    # Case 4: Opponent (player 2) has three pieces with one empty slot, blocking player 1
    window = [2, 2, 2, 0]
    assert evaluate_window(window, 1) == -4


# Test scoring the entire board for the specified player
def test_score_position():
    board = create_board()
    # Place three consecutive pieces vertically in column 0 for player 1
    for i in range(3):
        drop_piece(board, i, 0, 1)
    # The score for player 1 should be positive, indicating an advantage
    assert score_position(board, 1) > 0
