def gnome_sort(a: list) -> list:
    """ 
    Gnome sort algorithm.
    
    Parameters
    ----------
    a : list
        Set of numbers to search in.

    Returns
    -------
    list
        The sorted list.
    """

    n = len(a)
    i = 0

    while i < n:

        if i == 0 or a[i] >= a[i - 1]:
            i += 1
        
        else:
            a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1

    return a
