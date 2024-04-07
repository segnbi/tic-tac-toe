"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[X, EMPTY, X],
            [X, O, O],
            [EMPTY, O, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                x_count += 1

            if board[i][j] == O:
                o_count += 1

    if x_count > o_count:
        return O
    
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board):
        if utility(board) == 1:
            return X
        
        if utility(board) == -1:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_count = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                empty_count += 1
    
    if empty_count == 0:
        return True

    for i in range(len(board)):
        x_count = 0
        o_count = 0

        for j in range(len(board)):
            if board[i][j] == X:
                x_count += 1

            if board[i][j] == O:
                o_count += 1

        if x_count > 2 or o_count > 2:
            return True

    for i in range(len(board)):
        x_count = 0
        o_count = 0

        for j in range(len(board)):
            if board[j][i] == X:
                x_count += 1

            if board[j][i] == O:
                o_count += 1

        if x_count > 2 or o_count > 2:
            return True
        
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return True
        
    if (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return True
        
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for i in range(len(board)):
        x_count = 0
        o_count = 0

        for j in range(len(board[i])):
            if board[i][j] == X:
                x_count += 1

            if board[i][j] == O:
                o_count += 1
        
        if x_count > 2:
            return 1
        
        if o_count > 2:
            return -1
        
    for i in range(len(board)):
        x_count = 0
        o_count = 0

        for j in range(len(board[i])):
            if board[j][i] == X:
                x_count += 1

            if board[j][i] == O:
                o_count += 1
        
        if x_count > 2:
            return 1
        
        if o_count > 2:
            return -1
        
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return 1
        
    if (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return -1
        
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        print (max_val(board).a)
        raise NotImplementedError
        return max_val(board)
        
    if player(board) == O:
        print (min_val(board).a)
        raise NotImplementedError
        return min_val(board)  

    raise NotImplementedError


def max_val(board):
    t = Temp(-100, set())

    if terminal(board):
        return Temp(utility(board), set())
    
    for action in actions(board):
        t = max(t, min_val(result(board, action)), action)
        return t


def min_val(board):
    t = Temp(100, set())

    if terminal(board):
        return Temp(utility(board), set())
    
    for action in actions(board):
        t = min(t, max_val(result(board, action)), action)
        return t
    

def min(t, max_t, action):
    if t.v > max_t.v:
        max_t.a = action
        return max_t
    
    return t


def max(t, min_t, action):
    if t.v > min_t.v:
        t.a = action
        return t
    
    return min_t


class Temp():
    def __init__(self, v, a):
        self.v = v
        self.a = a