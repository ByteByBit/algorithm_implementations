def linear_search(a: list, x: int, r: int = 0, l: int = 0) -> int:
    """ 
    Linear search algorithm.

    Parameters
    ----------
    a : list
        Set of numbers to search in.
    l : int
        First index.
    r : int
        Length of the list.
    x : int
        The value we are looking for.

    Returns
    -------
    int
        The index of the searched value.
    """

    for i in range(r):

        if (a[i] == x):
            return i
        
    # Not found.
    return -1