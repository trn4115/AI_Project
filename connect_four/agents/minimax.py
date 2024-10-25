# agents/minimax.py
import numpy as np
import random
from game.utils import get_valid_locations, score_position
from game.board import is_terminal_node, winning_move, get_next_open_row, drop_piece


def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)

    # If depth is 0 or the game is in a terminal state, return the score
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, 2):  # AI wins
                return (None, 100000000000000)
            elif winning_move(board, 1):  # Opponent wins
                return (None, -10000000000000)
            else:  # Tie
                return (None, 0)
        else:  # Depth is zero
            return (None, score_position(board, 2))  # Evaluate board score

    # Maximizing player (AI)
    if maximizingPlayer:
        value = -np.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, 2)  # AI piece
            new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:  # Pruning
                break
        return column, value

    # Minimizing player (Opponent)
    else:
        value = np.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, 1)  # Opponent piece
            new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:  # Pruning
                break
        return column, value
