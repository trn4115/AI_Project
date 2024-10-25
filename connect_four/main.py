# main.py
from game.board import (
    create_board,
    drop_piece,
    is_valid_location,
    get_next_open_row,
    print_board,
    winning_move,
)
from agents.random_agent import random_agent_move
from agents.minimax import minimax
from agents.q_learning import QLearningAgent

import random


def main():
    board = create_board()
    game_over = False
    turn = random.randint(0, 1)  # Randomize who goes first

    q_agent = QLearningAgent()

    while not game_over:
        print_board(board)

        # Player 1 (Random Agent)
        if turn == 0:
            col = random_agent_move(board)
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)
                if winning_move(board, 1):
                    print("Random Agent Wins!")
                    game_over = True

        # Player 2 (Q-Learning Agent)
        else:
            state = str(board)
            col = q_agent.choose_action(board)
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
                if winning_move(board, 2):
                    print("Q-Learning Agent Wins!")
                    game_over = True
                next_state = str(board)
                q_agent.learn(
                    state, col, reward=1 if game_over else 0, next_state=next_state
                )

        turn += 1
        turn = turn % 2


if __name__ == "__main__":
    main()
