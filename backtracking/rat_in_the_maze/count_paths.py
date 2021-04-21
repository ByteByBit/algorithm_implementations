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

    if x >= 0 and x <= N and \
        y >= 0 and y <= N and \
        maze[x][y] == 1:
        return True
    
    return False


def count_paths(x: int, y: int, count: int):
    '''
    Counts the possible ways to get out of the maze.
    Parameters
    ----------
    x : int
        Next horizontal position in the maze.
    y : int
        Next vertical position in the maze.
    count : int
        Number of possible ways to out.
    Returns
    -------
    int
        Number of possible ways to out.
    '''

    # Reached the end, increase count.
    if x == N - 1 and y == N - 1:
        return count + 1

    # Mark cell as visited.
    visited[x][y] = True

    if is_valid_move(x, y):

        # Down.
        if x + 1 < N and not visited[x + 1][y]:
            count = count_paths(x+1, y, count)

        # Up.
        if x - 1 >= 0 and not visited[x - 1][y]:
            count = count_paths(x-1, y, count)

        # Right.
        if y + 1 < N and not visited[x][y + 1]:
            count = count_paths(x, y+1, count)

        # Left.
        if y - 1 >= 0 and not visited[x][y - 1]:
            count = count_paths(x, y-1, count)

    # Backtrack.
    visited[x][y] = False

    return count

if __name__ == '__main__':

    maze = [
        [ 1, 1, 1, 1] ,
        [ 1, 1, 0, 1] ,
        [ 0, 1, 0, 1] ,
        [ 1, 1, 1, 1]
    ]

    # Maze size.
    N = len(maze)

    count = 0
    visited = [[False for x in range(N)] for y in range(N)]

    count = count_paths(0, 0, count)

    print(count)