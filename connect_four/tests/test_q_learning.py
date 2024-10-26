import numpy as np
from agents.q_learning import QLearningAgent
from game.board import create_board, drop_piece


# Test the initialization of the QLearningAgent
def test_q_learning_agent_initialization():
    agent = QLearningAgent()
    # Verify that the initial hyperparameters are set correctly
    assert agent.alpha == 0.1  # Learning rate
    assert agent.gamma == 0.95  # Discount factor
    assert agent.epsilon == 1.0  # Initial exploration rate


# Test the QLearningAgent's ability to choose a valid action
def test_q_learning_agent_choose_action():
    board = create_board()
    agent = QLearningAgent()
    # Choose an action on an empty board
    action = agent.choose_action(board)
    # Ensure the chosen action is within the range of valid columns (0-6)
    assert action in range(7)


# Test the QLearningAgent's learning (Q-table update) function
def test_q_learning_agent_learn():
    agent = QLearningAgent()
    state = "state1"
    next_state = "state2"
    action = 0
    # Perform a learning update with a reward
    agent.learn(state, action, reward=1, next_state=next_state)
    # Check that the Q-value for the state-action pair has been updated
    assert agent.q_table[state][action] != 0
