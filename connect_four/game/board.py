# game/board.py
import numpy as np

ROWS = 6
COLS = 7


# Create blank board
def create_board():
    return np.zeros((ROWS, COLS))


# Drop a piece onto the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece


# Check if the column is a valid location (i.e., not full)
def is_valid_location(board, col):
    return board[ROWS - 1][col] == 0


# Get the next available row in a column
def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r


# Print the board (flip it to make the bottom row print first)
def print_board(board):
    print("\n")
    print(np.flip(board, 0))


# Check if a player has won the game
def winning_move(board, piece):
    # Horizontal check
    for c in range(COLS - 3):
        for r in range(ROWS):
            if all([board[r][c + i] == piece for i in range(4)]):
                return True
    # Vertical check
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all([board[r + i][c] == piece for i in range(4)]):
                return True
    # Positive diagonal check
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if all([board[r + i][c + i] == piece for i in range(4)]):
                return True
    # Negative diagonal check
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if all([board[r - i][c + i] == piece for i in range(4)]):
                return True
    return False
