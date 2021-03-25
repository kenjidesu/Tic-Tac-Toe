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
    moves = action
    new_board = deepcopy(board)
    new_board[moves[0]][moves[1]] = turn
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal
    for hor in board:
        if hor[0] != EMPTY:
            if hor.count(hor[0]) == 3:
                return hor[0]

    # Vertical
    for row in range(len(board)):
        check_ver = []
        for ver in range(len(board[row])):
            if board[0][row] != EMPTY:
                check_ver.append(board[ver][row])
        
        if check_ver:
            if check_ver.count(check_ver[0]) == 3:
                return check_ver[0]

    # Diagonal
    for cross in range(len(board)):
        check_diag_l = []
        check_diag_r = []
        helper = 2
        for diag in range(len(board[cross])):
            if board[0][0] != EMPTY:
                check_diag_l.append(board[diag][diag])
                
            if board[0][2] != EMPTY:
                check_diag_r.append(board[diag][helper])
                helper -= 1
        
        if check_diag_l:
            if check_diag_l.count(check_diag_l[0]) == 3:
                return check_diag_l[0]
        
        if check_diag_r:
            if check_diag_r.count(check_diag_r[0]) == 3:
                return check_diag_r[0]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    won = winner(board)
    slo_bool = []
    for slot in range(len(board)):
        for in_slot in range(len(board[slot])):
            slo_bool.append(bool(board[slot][in_slot]))

    if won or all(slo_bool):
         return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        game_winner = winner(board)
        if game_winner == X:
            return 1
        elif game_winner == O:
            return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)

    if terminal(board):
        return None
    else:
        if turn == X:
            mx, act = max_value(board)
            return act
        elif turn == O:
            mn, act = min_value(board)
            return act


def max_value(board):
    if terminal(board):
        return utility(board), None
    v = float('-inf')
    move = None
    for action in actions(board):
        c, act = min_value(result(board, action))
        if c > v:
            v = c
            move = action
            if v == 1:
                return v, move
    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None
    v = float('inf')
    move = None
    for action in actions(board):
        c, act = max_value(result(board, action))
        if c < v:
            v = c
            move = action
            if v == -1:
                return v, move
    return v, move
