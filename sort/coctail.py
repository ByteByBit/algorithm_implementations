def coctail_sort(a: list) -> list:
    """ 
    Cocktail sort algorithm.
    
    Parameters
    ----------
    a : list
        The list to sort.

    Returns
    -------
    list
        The sorted list.
    """

    swapped = True
    start = 0
    end = len(a) -1

    while swapped:

        swapped = False

        # From start to end.
        for i in range(start, end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True

        # No swap happened, it's already sorted.
        if not swapped:
            return a

        swapped = False

        # Last item should be fine, move 1 back.
        end = end -1

        # From end to start, backwards.
        for i in range(end-1, start-1, -1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True

        # Move start 1 forward, as the first one is already the smallest.
        start = start + 1

    return a