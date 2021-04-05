import math


def jump_search(a: list, r:int, x: int) -> int:
    """ 
    Jump search algorithm.
    
    Parameters
    ----------
    a : list
        Set of numbers to search in.
    r : int
        Length of the list.
    x : int
        The value we are looking for.

    Returns
    -------
    int
        The index of the searched value.
    """


    # Define block size.
    step = math.sqrt(r)

    
    prev = 0
    i = int(min(step, r) - 1)

    # Find the block containing the element.
    while a[i] < x:
        
        prev = step
        step += math.sqrt(r)
        i = int(min(step, r)) - 1

        # Not found.
        if prev >= r:
            return -1

    prev = int(prev)

    # Linear search in the give npart of the list.
    while a[prev] < x:

        prev += 1

        if prev == min(step, r):
            return -1

    if a[prev] == x:
        return prev
    
    # Not found.
    return -1