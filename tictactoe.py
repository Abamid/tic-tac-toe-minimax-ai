import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board — a 3x3 grid of EMPTY.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    X starts first. Then players alternate.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Raises exception if action is invalid.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move")
    
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over (win or tie), False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won, -1 if O has won, 0 for a tie.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action (i, j) for the current player using the Minimax algorithm.
    """
    if terminal(board):
        return None

    current = player(board)

    if current == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)

    return move


def max_value(board):
    """
    Maximizing function for Minimax (X wants highest score).
    """
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_move = None

    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v = min_val
            best_move = action
            if v == 1:
                break  # Prune if best possible outcome found

    return v, best_move


def min_value(board):
    """
    Minimizing function for Minimax (O wants lowest score).
    """
    if terminal(board):
        return utility(board), None

    v = math.inf
    best_move = None

    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v = max_val
            best_move = action
            if v == -1:
                break  # Prune if worst possible outcome found

    return v, best_move
