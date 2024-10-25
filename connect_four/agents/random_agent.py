# agents/random_agent.py
import random
from game.utils import get_valid_locations


def random_agent_move(board):
    valid_moves = get_valid_locations(board)
    return random.choice(valid_moves)
