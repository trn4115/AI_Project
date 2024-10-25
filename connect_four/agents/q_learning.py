# agents/q_learning.py
import numpy as np
import random
from game.utils import get_valid_locations
from game.board import drop_piece, get_next_open_row, print_board


class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.95, epsilon=1.0, epsilon_decay=0.995):
        self.q_table = {}
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = 0.01

    # Convert the board into a string format to use as a state key for Q-table
    def get_state(self, board):
        return str(board)

    # Choose action based on the epsilon-greedy policy
    def choose_action(self, board):
        valid_moves = get_valid_locations(board)
        if np.random.random() < self.epsilon:  # Exploration
            return random.choice(valid_moves)
        else:  # Exploitation
            state = self.get_state(board)
            if state not in self.q_table:
                self.q_table[state] = np.zeros(board.shape[1])
            return np.argmax(self.q_table[state])

    # Update Q-table based on the action taken and the reward received
    def learn(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(7)
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(7)

        current_q = self.q_table[state][action]
        max_future_q = np.max(self.q_table[next_state])

        # Q-Learning update rule
        self.q_table[state][action] += self.alpha * (
            reward + self.gamma * max_future_q - current_q
        )

        # Decay epsilon (exploration rate)
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
