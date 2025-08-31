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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX, countO = 0, 0
    for row in board:
        for cell in row:
            if (cell == X):
                countX += 1
            elif (cell == O):
                countO += 1
    if (countX == countO):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                act.add((i, j))
    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (a, b) = action
    if (board[a][b] != EMPTY):
        raise Exception
    
    nextBoard = list()
    for i in range(3):
        l = list()
        for j in range(3):
            l.append(board[i][j])
        nextBoard.append(l)
    
    turn = player(board)
    nextBoard[a][b] = turn
    return nextBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning = [
        [(0,0), (0,1), (0,2)],  # rows
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],  # cols
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],  # diagonals
        [(0,2), (1,1), (2,0)]
    ] # All winning positions
    
    for pos in winning:
        a, b, c = pos[0], pos[1], pos[2]
        x1, y1 = a[0], a[1]
        x2, y2 = b[0], b[1]
        x3, y3 = c[0], c[1]
        if board[x1][y1] is not EMPTY and board[x1][y1] == board[x2][y2] == board[x3][y3]: 
            return board[x1][y1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    hasEmpty = False # Does board has any empty cells?
    for row in board:
        if hasEmpty:
            break
        for cell in row:
            if cell is EMPTY:
                hasEmpty = True
    return not hasEmpty


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winGuy = winner(board)
    if winGuy == X: 
        return 1
    elif winGuy == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    def max_value(board):
        maxi = -float("inf")
        move = None
        if terminal(board):
            return utility(board), None
        
        for act in actions(board):
            val, _ = min_value(result(board, act))
            if (val > maxi):
                maxi, move = val, act
        return maxi, move
            
    def min_value(board):
        mini = float("inf")
        move = None
        if terminal(board):
            return utility(board), None
        
        for act in actions(board):
            val, _ = max_value(result(board, act))
            if (val < mini):
                mini, move = val, act
        return mini, move
    
    currPlayer = player(board)
    if currPlayer == X:
        _, move = max_value(board)
    else :
        _, move = min_value(board)
    return move
