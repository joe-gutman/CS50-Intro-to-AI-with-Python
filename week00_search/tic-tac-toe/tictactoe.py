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

    possible_actions = []

    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column == EMPTY:
                possible_actions.append((i, j))

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
        symbol = EMPTY

        for row in board:
            if row[0] != EMPTY and all(i == row[0] for i in row):
                symbol = row[0]

        for column in range(len(board[0])):
            symbol = board[0][column]
            if symbol != EMPTY:
                for row in board:
                    if symbol != row[column]:
                        break

                

        if symbol != None:
            return symbol
    
    return None
        
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None and len(actions(board)) > 0:
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
    
def utilityToPlayer(utility):
    """
    Converts the utility the equivilant player X is 1, O is -1, or None if 0.
    """

    if utility == 1:
        return X
    elif utility == 0:
        return O
    else: 
        return None


def minimax(board, moves, optimal_moves=None):
    """
    Returns the optimal action for the current player on the board.
    """
    if moves == None:
        moves = []

    if terminal(board):
        utility_winner = utility(board)
        if utilityToPlayer(utility_winner) == player(board):
            if optimal_moves == None or len(optimal_moves) < len(moves):
                print('OPTIMAL MOVE:', optimal_moves)
                return optimal_moves
            
    possible_moves = actions(board)
    print('POSSIBLE MOVES:', possible_moves)
    for move in possible_moves:
        moves.append(moves)
        new_board = result(board, move)

        # next move is the potential optimal move
        # make next move on imaginary board as current player track AI player symbol in minimax inputs)


        return minimax(new_board, moves, optimal_moves)[0]

    