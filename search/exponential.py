from binary import binary_search

def exponential_search(a: list, r: int, x: int) -> int:
    """ 
    Exponential search algorithm. 
    
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
    if a[0] == x:
        return 0
    

    i = 1
    while i < r and a[i] <= x:
        i = i * 2
    
    return binary_search(a=a, l=i // 2, r=min(i, r), x=x)