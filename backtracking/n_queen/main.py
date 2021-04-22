


def is_position_safe(board, row, col):
    '''
    Check if the upcoming queen is safe to place
    vertically, horizontally and diagonally. 
    
    Parameters
    ----------
    board : list
        The chess board.
    row : int
        First (vertical) coordinate of the step/ move.
    col : int
        Second (horizontal) coordinate of the step/ move.  

    Returns
    -------
    bool
        True if the placement is valid.
    '''

    for i in range(N):
        
        # Check row and col, if a queen present.
        if board[row][i] == 1 or board[i][col]:
            return False

        for j in range(N):
            
            # Check diagonals.
            if i + j == row + col or i - j == row - col:
                if board[i][j] == 1:
                    return False
            
    return True


def place_queens(board, col):
    '''
    Placing queens to the chess board.

    Parameters
    ----------
    board : list
        The chess board.
    col : int
        Second (horizontal) coordinate of the step/ move.  

    Returns
    -------
    bool
        True if all the queens are placed.
    '''

    # All queens placed.
    if col == N:
        return True

    for i in range(N):

        if is_position_safe(board, i, col):
            
            # Put the queen.
            board[i][col] = 1

            # Check if she likes there.
            if place_queens(board, col+1):
                return True

        # Backtrack.
        board[i][col] = 0
    
    return False


if __name__ == '__main__':

    # Board size.
    N = 4

    board = [[0 for x in range(N)] for x in range(N)]

    if place_queens(board, 0):
        
        # Print the board.
        for i in board:
            line = ','.join(str(x) for x in i)
            print(line)
    else:
        print('Knight tour is not possible.')