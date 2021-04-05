def interpolation_search(a: list, r: int, x: int, l: int = 0) -> int:
    """ 
    Interpolation search algorithm.
    
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


    if l <= r and x >= a[l] and x <= a[r]:

        pos = l + ((r - l) // (a[r] - a[l]) * (x - a[l]))
        
        if a[pos] == x:
            return pos

        elif a[pos] < x:
            return interpolation_search(a, l=pos+1, r=r, x=x)

        elif a[pos] > x:
            return interpolation_search(a, l=l, r=pos-1, x=x)

    return -1
