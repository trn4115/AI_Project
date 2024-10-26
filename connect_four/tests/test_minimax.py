import numpy as np
from agents.minimax import minimax
from game.board import create_board, drop_piece
from game.utils import is_terminal_node


# Test the minimax function for a terminal winning state for AI (player 2)
def test_minimax_terminal_win():
    board = create_board()
    # Create a winning condition for player 2 by placing four consecutive pieces in row 0
    for col in range(4):
        drop_piece(board, 0, col, 2)
    # Run minimax with a depth of 4 and maximizing player as True (AI)
    _, score = minimax(
        board, depth=4, alpha=-np.inf, beta=np.inf, maximizingPlayer=True
    )
    # Ensure the minimax score reflects a winning outcome for the AI
    assert score == 100000000000000  # Expected high score for AI win


# Test the minimax function for a terminal losing state for AI (player 2)
def test_minimax_terminal_loss():
    board = create_board()
    # Create a winning condition for player 1 by placing four consecutive pieces in row 0
    for col in range(4):
        drop_piece(board, 0, col, 1)
    # Run minimax with a depth of 4 and maximizing player as False (opponent's turn)
    _, score = minimax(
        board, depth=4, alpha=-np.inf, beta=np.inf, maximizingPlayer=False
    )
    # Ensure the minimax score reflects a losing outcome for the AI
    assert score == -10000000000000  # Expected low score for AI loss
