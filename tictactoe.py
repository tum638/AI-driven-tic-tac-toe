"""
Tic Tac Toe Player
"""

import math
import copy

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
    X_on_board = []
    O_on_board = []
    if board == initial_state():
        return X
    else:
        for row in board:
            for cell in row:
                if cell == X:
                    X_on_board.append(X)
                elif cell == O:
                    O_on_board.append(O)
        if len(X_on_board) > len(O_on_board):
            return O
        elif len(X_on_board) == len(O_on_board):
            return X
        elif len(O_on_board) > len(X_on_board):
            return X
    return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for row in range(len(board)):
        for cell in range(len(board[row])):
            if board[row][cell] == EMPTY:
                move = (row, cell,)
                possible_moves.add(move)
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    memo = {}
    new_board = copy.deepcopy(board, memo)

    cell = new_board[action[0]][action[1]]
    move = player(board)

    if cell is not EMPTY:
        raise Exception("That move is not allowed")
    else:
        # cell = move
        new_board[action[0]][action[1]] = move
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] != EMPTY:
        winner = board[0][0]
        return winner
    elif board[1][0] == board[1][1] == board[1][2] != EMPTY:
        winner = board[1][0]
        return winner
    elif board[2][0] == board[2][1] == board[2][2] != EMPTY:
        winner = board[2][0]
        return winner
    elif board[0][0] == board[1][0] == board[2][0] != EMPTY:
        winner = board[0][0]
        return winner
    elif board[0][1] == board[1][1] == board[2][1] != EMPTY:
        winner = board[0][1]
        return winner
    elif board[0][2] == board[1][2] == board[2][2] != EMPTY:
        winner = board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] != EMPTY:
        winner = board[0][0]
        return winner
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        winner = board[0][2]
        return winner
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    null_state = []
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell is EMPTY:
                null_state.append(EMPTY)
    if len(null_state) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


# def max_value(board):
#     """
#     Given the AI is "X"(Maximizer), returns the value of the utility if the terminal state has been reached,
#     otherwise return the value of the utility that will result
#     in optimal play.
#     """
#     if terminal(board):
#         return utility(board)

#     else:
#         v = -(math.inf)
#         for action in actions(board):
#             v = max(v, min_value(result(board, action)))
#         return action
def max_value(board):
    """
    Return a tuple (maximal_value, maximal_value_action)
    """
    if terminal(board):
        return utility(board), None

    else:
        values_per_action = [(min_value(result(board, a))[0], a)
                             for a in actions(board)]
        return max(values_per_action)


def min_value(board):
    """
    Given the AI is "O"(Minimizer), returns the value of the utility if the terminal state has been reached,
    otherwise return the value of the utility that will result
    in optimal play.
    """
    if terminal(board):
        return utility(board), None
    else:
        values_per_action = [(max_value(result(board, a))[0], a)
                             for a in actions(board)]
        return min(values_per_action)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        _val, action = max_value(board)

    elif player(board) == O:
        _val, action = min_value(board)
    return action
