import numpy as np
from game.board import (
    create_board,
    drop_piece,
    is_valid_location,
    get_next_open_row,
    winning_move,
)


# Test the creation of an empty board with the correct shape and initial values
def test_create_board():
    board = create_board()
    # Check that the board has 6 rows and 7 columns
    assert board.shape == (6, 7)
    # Ensure all positions are initialized to 0
    assert np.all(board == 0)


# Test dropping a piece onto the board in a specific location
def test_drop_piece():
    board = create_board()
    drop_piece(board, 0, 0, 1)  # Drop piece for player 1 in the top-left corner
    # Check that the piece was placed correctly
    assert board[0][0] == 1


# Test if a column is a valid location (i.e., not full)
def test_is_valid_location():
    board = create_board()
    # Check that an empty column is considered valid
    assert is_valid_location(board, 0) == True
    # Fill up the first column
    for row in range(6):
        drop_piece(board, row, 0, 1)
    # Check that the column is no longer valid after filling
    assert is_valid_location(board, 0) == False


# Test finding the next open row in a specific column
def test_get_next_open_row():
    board = create_board()
    # Check that the next open row in an empty column is the bottom row (index 0)
    row = get_next_open_row(board, 0)
    assert row == 0
    # Drop a piece in the bottom row
    drop_piece(board, 0, 0, 1)
    # Check that the next open row is now above the previously filled row
    row = get_next_open_row(board, 0)
    assert row == 1


# Test the horizontal winning condition for four consecutive pieces
def test_winning_move_horizontal():
    board = create_board()
    # Place four consecutive pieces horizontally for player 1
    for col in range(4):
        drop_piece(board, 0, col, 1)
    # Check that this results in a winning move
    assert winning_move(board, 1) == True


# Test the vertical winning condition for four consecutive pieces
def test_winning_move_vertical():
    board = create_board()
    # Place four consecutive pieces vertically for player 1
    for row in range(4):
        drop_piece(board, row, 0, 1)
    # Check that this results in a winning move
    assert winning_move(board, 1) == True


# Test the positive diagonal winning condition (bottom-left to top-right)
def test_winning_move_positive_diagonal():
    board = create_board()
    # Place four pieces in a positive diagonal pattern for player 1
    for i in range(4):
        drop_piece(board, i, i, 1)
    # Check that this results in a winning move
    assert winning_move(board, 1) == True


# Test the negative diagonal winning condition (top-left to bottom-right)
def test_winning_move_negative_diagonal():
    board = create_board()
    # Place four pieces in a negative diagonal pattern for player 1
    for i in range(4):
        drop_piece(board, i, 3 - i, 1)
    # Check that this results in a winning move
    assert winning_move(board, 1) == True
