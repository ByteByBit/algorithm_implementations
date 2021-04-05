def binary_search(a: list, r: int, x: int, l: int = 0) -> int:
    """ 
    Binary search algorithm. 
    
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

    if r >= l:

        # Mid point.
        mid = l + (r - l) // 2

        # Mid elem is what we look for.
        if a[mid] == x:
            return mid

        # Search in the left half of the list.
        elif a[mid] > x:
            return binary_search(a=a, l=l, r=mid - 1, x=x)

        # Search in the right half of the list.
        else:
            return binary_search(a=a, l=mid + 1, r=r, x=x)

    # Not found.
    else:
        return -1