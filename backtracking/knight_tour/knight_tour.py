# Possible moves.
KNIGHT_MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
# Board size.
N = 8
LAST_STEP = (N**2) + 1
MOVES_LENGTH = len(KNIGHT_MOVES)


def is_valid_move(i: int, j: int):
    ''' 
    Function to validate move.

    Parameters
    ----------
    i : int
        First (vertical) coordinate of the step/ move.
    j : int
        Second (horizontal) coordinate of the step/ move.  

    Returns
    -------
    bool
        True if the move is valid.
    '''

    if i >= 0 and  i < N and j >= 0 and j < N:
        
        # Check if it is an 'unstepped' field.
        if board[i][j] == 0:
            return True
    
    return False


def move(step_count: int, i: int, j: int):
    '''
    Function to move the knight on the chess board.

    Parameters
    ----------
    step_count : int
        Represents the valid steps made on the board 
        (the used board positions).
    i : int
        First (vertical) coordinate of the step/ move.
    j : int
        Second (horizontal) coordinate of the step/ move.  

    Returns
    -------
    bool
        True if the calculation is finished, false if it's not possible.
    '''

    # We reached the last field of the board.
    if step_count == LAST_STEP:
        return True

    # Try every possible (8) moves.
    for k in range(MOVES_LENGTH):

        next_i = i + KNIGHT_MOVES[k][0]
        next_j = j + KNIGHT_MOVES[k][1]

        if is_valid_move(next_i, next_j):

            # Put move number into the board.
            board[next_i][next_j] = step_count

            # Validate move.
            if move(step_count + 1, next_i, next_j):
                
                return True

            # Backtracking if the move was invalid.
            board[next_i][next_j] = 0
        
    return False


if __name__ == '__main__':

    # Create an N * N size board.
    board = [[0 for x in range(N)] for x in range(N)]
    
    # Place knight at the starting point.
    board[0][0] = 1   

    if move(2, 0, 0):
        
        # Print the board.
        for i in board:
            line = ','.join(str(x) for x in i)
            print(line)
    else:
        print('Knight tour is not possible.')