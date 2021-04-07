import random


def bogo_sort(a: list) -> list:
    """ 
    Bogo sort algorithm.
    
    Parameters
    ----------
    a : list
        The list to sort.

    Returns
    -------
    list
        The sorted list.

    """

    if is_sorted(a) ==  False:

        random.shuffle(a) # Shuffle the list.
        return bogo_sort(a) # Recursion.

    return a


def is_sorted(a: list) -> bool:
    """ 
    Iterate over the list to see if it already sorted.

    Parameters
    ----------
    a : list
        A list to sort.

    Returns
    -------
    bool
        Is the list already sorted.
    """
    
    n = len(a)

    # Just iterate through to see if it is sorted.
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            return False
        
    return True
