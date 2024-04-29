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

    for row in board:
        for column in row:
            if column.lower() == EMPTY:
                possible_actions.append((current_row, current_column))
            current_column += 1
        current_row += 1

    return set(possible_actions)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise InvalidMoveError("The move is not valid because the cell is already occupied.")
    
    new_board = copy.deepcopy(board)

    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    move_count = 0

    for row in board:
        for symbol in row:
            if symbol != EMPTY:
                move_count += 1
    
    if move_count < 5:
        return None
    else:
        symbol = None

        for column in range(len(board[0])):
            for row in range(len(board)):
                if all(i == row[0] for i in row) and row[0] != EMPTY:
                    return board[row][0]
                if symbol == None:
                    symbol = board[row][column]
                elif board[row][column] != symbol:
                    break
                

        if symbol != None:
            return symbol
    
    return None
        
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        return False
    else: 
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
    raise NotImplementedError
