from agents.random_agent import random_agent_move
from game.board import create_board, drop_piece
from game.utils import get_valid_locations


# Test the random agent's move selection to ensure it selects a valid column
def test_random_agent_move():
    board = create_board()
    # Use random_agent_move to select a move on an empty board
    move = random_agent_move(board)
    # Check that the chosen move is within the list of valid columns
    assert move in get_valid_locations(board)  # Should be a valid move
