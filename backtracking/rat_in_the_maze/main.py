# Maze size.
N = 4


def is_valid_move(x: int, y: int):
    ''' 
    Function to validate move in the maze.

    Parameters
    ----------
    x : int
        Next horizontal position in the maze.
    y : int
        Next vertical position in the maze.

    Returns
    -------
    bool
        True if the move is valid.
    '''

    if x >= 0 and x < N and \
        y >= 0 and y < N and \
        maze[x][y] == 1:
        return True
    
    return False


def is_end(x: int, y: int):
    '''
    Checks if the next move is the destination.

    Parameters
    ----------
    x : int
        Next horizontal position in the maze.
    y : int
        Next vertical position in the maze.

    Returns
    -------
    bool
        True if the move is destination.
    '''

    if x == N - 1 and y == N -1 and maze[x][y] == 1:
        return True
    
    return False


def solve(x: int, y: int):
    '''
    Solves the maze problem by moving the rat, right or down.

    Parameters
    ----------
    x : int
        Next horizontal position in the maze.
    y : int
        Next vertical position in the maze.

    Returns
    -------
    bool
        True if the rat is out.
        False if the rat stuck there forever + 1.
    '''

    if is_end(x=x, y=y):
        solution[x][y] = 1
        return True

    if is_valid_move(x=x, y=y):

        # Check if we moved a position, where we've been already once.
        if solution[x][y] == 1:
            return False

        # Mark the new position.
        solution[x][y] = 1

        # Move right.
        if solve(x=x+1, y=y):
            return True

        # Move down.
        if solve(x=x, y=y+1):
            return True

        # Move left.
        if solve(x=x-1, y=y):
            return True

        # Move up.
        if solve(x=x, y=y-1):
            return True

        # Backtrack.
        solution[x][y] = 0

        return False

if __name__ == '__main__':

    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1], 
        [1, 1, 0, 0],
        [0, 1, 1, 1]
        ]

    # Create a solutin matrix.
    solution = [[0 for x in range(N)] for x in range(N)]

    if solve(x=0, y=0):
        # Print the board.
        for i in solution:
            line = ','.join(str(x) for x in i)
            print(line)
    else:
        print('No escape!')
