def brick_sort(a: list) -> list:
    """ 
    Brick sort algorithm.
    
    Parameters
    ----------
    a : list
        The list to sort.

    Returns
    -------
    list
        The sorted list.

    """

    n = len(a) - 1
    sorted = False

    while not sorted:

        sorted = True

        # Even.
        for i in range(0, n, 2):
            if a[i] > a[i+1]:
                # Swap.
                a[i], a[i+1] = a[i+1], a[i]
                sorted = False
        
        # Odd.
        for i in range(1, n, 2):
            if a[i] > a[i+1]:
                # Swap.
                a[i], a[i+1] = a[i+1], a[i]
                sorted = False
            
    return a