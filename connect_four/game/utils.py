# game/utils.py
import numpy as np
from game.board import winning_move  # Importing the winning_move function


# Get valid locations where a piece can be dropped (for valid moves)
def get_valid_locations(board):
    valid_locations = [col for col in range(board.shape[1]) if board[5][col] == 0]
    return valid_locations


print(get_valid_locations)


# Evaluate a window of four slots for scoring
def evaluate_window(window, piece):
    score = 0
    opp_piece = 1 if piece == 2 else 2

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 4

    return score


# Score the board for the given piece (either player 1 or player 2)
def score_position(board, piece):
    score = 0
    # Score center column
    center_array = [int(i) for i in list(board[:, board.shape[1] // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Score horizontal
    for r in range(board.shape[0]):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(board.shape[1] - 3):
            window = row_array[c : c + 4]
            score += evaluate_window(window, piece)

    # Score vertical
    for c in range(board.shape[1]):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(board.shape[0] - 3):
            window = col_array[r : r + 4]
            score += evaluate_window(window, piece)

    # Score positive sloped diagonal
    for r in range(board.shape[0] - 3):
        for c in range(board.shape[1] - 3):
            window = [board[r + i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Score negative sloped diagonal
    for r in range(3, board.shape[0]):
        for c in range(board.shape[1] - 3):
            window = [board[r - i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score


# Check if the game has reached a terminal state (i.e., win or draw)
def is_terminal_node(board):
    return (
        winning_move(board, 1)
        or winning_move(board, 2)
        or len(get_valid_locations(board)) == 0
    )
