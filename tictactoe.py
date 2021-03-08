"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counter_x = 0
    counter_o = 0

    # Counts how many X's and O's
    for value in board:
        counter_x += value.count(X)
        counter_o += value.count(O)
    
    if counter_x > counter_o:
        return O
    elif counter_x == counter_o:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()

    # Finds an EMPTY slot on the board
    for out_board in range(len(board)):
        for in_board in range(len(board[out_board])):
            if board[out_board][in_board] == EMPTY:
                possible_moves.add((out_board, in_board))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    lst_board = []

    # Applies every possible move on the board
    for moves in action:
        new_board = deepcopy(board)
        new_board[moves[0]][moves[1]] = turn
        lst_board.append(new_board)
    
    return lst_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
