"""
Tic Tac Toe Player
"""

import math
import copy

usr = None
pyr = None
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cnt_x = 0
    cnt_y = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == X:
                cnt_x = cnt_x + 1
            elif board[i][j] == O:
                cnt_y = cnt_y + 1
    if cnt_x <= cnt_y:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                action.append((i, j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    state = copy.deepcopy(board)
    if state[action[0]][action[1]] != EMPTY:
        raise Exception
    state[action[0]][action[1]] = player(board)
    return state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0, 3):
        if board[i][0] != EMPTY and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
    for i in range(0, 3):
        if board[0][i] != EMPTY and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] != EMPTY and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != EMPTY and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    cnt = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] != EMPTY:
                cnt = cnt + 1
    if cnt == 9 or winner(board) != EMPTY:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == pyr:
        return 1
    elif winner(board) == usr:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return EMPTY
    now = -3
    taken = ()
    minimum = 0
    action = actions(board)
    for state in action:
        check = min_value(result(board, state), now, minimum)
        if check > now:
            now = check
            taken = state
    return taken


def min_value(board, maximum, minimum):
    if terminal(board):
        return utility(board)
    ans = 3
    action = actions(board)
    for state in action:
        ans = min(ans, max_value(result(board, state), maximum, ans))
        if ans <= maximum:
            break
    return ans


def max_value(board, maximum, minimum):
    if terminal(board):
        return utility(board)
    ans = -3
    action = actions(board)
    for state in action:
        ans = max(ans, min_value(result(board, state), ans, minimum))
        if ans >= minimum:
            break
    return ans
