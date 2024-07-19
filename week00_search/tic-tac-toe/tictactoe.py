"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


# custom error for invalid move
class InvalidMoveError(Exception): 
    def __init__(self, message="Invalid move"):
        self.message = message
        super().__init__(self.message)


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
    x_count = 0
    o_count = 0

    for row in board:
        for symbol in row:
            if symbol == X:
                x_count += 1
            if symbol == O:
                o_count += 1
    
    if x_count + o_count == 0 or ((x_count + o_count) % 2) == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    current_row = 0
    current_column = 0

    possible_actions = []

    for current_row, row in enumerate(board):
        for current_column, column in enumerate(row):
            if column is None:
                possible_actions.append((current_row, current_column))

    return set(possible_actions)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action == None:
        raise InvalidMoveError("Invalid Action: Move not made.")

    if board[action[0]][action[1]] != EMPTY:
        print("result", action)
        raise InvalidMoveError("Invalid Action: Cell is already occupied.")
        
    
    new_board = copy.deepcopy(board)

    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    lines = []

    # Add rows to lines
    lines.extend(board)

    # Add columns to lines
    lines.extend([[board[row][column] for row in range(len(board))] for column in range(len(board[0]))])

    # Add diagonals to lines
    lines.append([board[i][i] for i in range(len(board))])
    lines.append([board[i][-(i+1)] for i in range(len(board))])

    for line in lines:
        if line[0] is not EMPTY and all(item == line[0] for item in line):
            return line[0]
        
    return None
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True
    

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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    def min_value(board):
        if terminal(board):
            return utility(board)
        value = math.inf
        for move in actions(board):
            value = min(value, max_value(result(board, move)))
        return value

    def max_value(board):
        if terminal(board):
            return utility(board)
        value = -math.inf
        for move in actions(board):
            value = max(value, min_value(result(board, move)))
        return value
    
    best_move = None

    if current_player == X:
        best_value = -math.inf
        for move in actions(board):
            new_board = result(board, move)
            move_value = min_value(new_board)
            if move_value > best_value:
                best_value = move_value
                best_move = move
    else:
        best_value = math.inf
        for move in actions(board):
            new_board = result(board, move)
            move_value = max_value(new_board)
            if move_value < best_value:
                best_value = move_value
                best_move = move

    return best_move

            
